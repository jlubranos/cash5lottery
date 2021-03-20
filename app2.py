import pandas as pd
import datetime
import json
import random
from flask import Flask, render_template, request, jsonify
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

ENV ='dev'

cash5db='postgresql://postgres:postgres@localhost/cash5'

if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = cash5db
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)

engine=create_engine(app.config['SQLALCHEMY_DATABASE_URI']) 

class cash5numbers(db.Model):
    __tablename__ = 'numbers'
    pick_date = db.Column(db.Date, primary_key = True, unique = True)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)
    num3 = db.Column(db.Integer)
    num4 = db.Column(db.Integer)
    num5 = db.Column(db.Integer)
    winning_payout = db.Column(db.String(20))

    def __init__ (self,pick_date,num1,num2,num3,num4,num5,winning_payout):
        self.pick_date = pick_date
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.winning_payout = winning_payout

class suggested_picks(db.Model):
    __tablename__='picks_suggested'
    suggested_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    suggested_date = db.Column(db.Date)
    method_name = db.Column(db.String(100))
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)
    num3 = db.Column(db.Integer)
    num4 = db.Column(db.Integer)
    num5 = db.Column(db.Integer)

    def __init__ (self, suggested_date, method_name, num1, num2, num3, num4, num5):
        self.suggested_date = suggested_date
        self.method_name = method_name
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5

def exists(numbers,results):
    row=0
    while (numbers.index[row] in results):
        row+=1
    results=results.append(numbers.index[row])
    return results

def oddeven(numbers,results,length,odd,even,count):
    row=0
    oddcount=0
    evencount=0
    if (count):
        for number in results:
            if (number % 2 >0):
                oddcount+=1
            else:
                evencount+=1
    while (len(results)<length):
        if (numbers.index[row] % 2 > 0 and oddcount<odd and not(numbers.index[row] in results)):
            oddcount+=1
            results.append(numbers.index[row])
        elif (numbers.index[row] % 2 ==0 and evencount<even and not(numbers.index[row] in results)):
            evencount+=1
            results.append(numbers.index[row])
        row+=1
    return results

def generatecombo(odd,even,flag):
    
# flag=0 signifies that the odd numbers will be low <=22
# flag=1 signifies that the odd numbers will be high >=23

    ocount=0
    ecount=0
    results=[]
    
    while (len(results)<5):
        number=random.randint(1,45)
        if (flag==0):
            if ((number % 2 > 0) and (number <=22) and (ocount<odd) and not(number in results)):
                ocount+=1
                results.append(number)
            elif ((number % 2 == 0) and (number>=23) and (ecount<even) and not(number in results)):
                ecount+=1
                results.append(number)
        else:
            if ((number % 2 > 0) and (number>=23) and (ocount<odd) and not(number in results)):
                ocount+=1
                results.append(number)
            elif ((number % 2 ==0) and (number<=22) and (ecount<even) and not(number in results)):
                ecount+=1
                results.append(number)
    results.sort()
    return results   


@app.route('/', methods=["GET", "POST"])
def home():
    session = Session(bind=engine)
    executable_path={'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)
    url = 'https://www.njlottery.com/en-us/drawgames/jerseycash.html'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    winning_dates=soup.find_all('tr',{'data-toggle':['tableWinningNumbers']})
    est_jackpot=soup.find('div',{'class':['amount']}).text
    est_jackpot=est_jackpot.lstrip()
    winning_numbers=[]
    for winning_date in winning_dates:
        date=winning_date.find('td',{'title':['date']})
        payout=winning_date.find('td',{'title':['5/5 Payout']})
        payout=payout.find('span',{'class':['text-nowrap']}).text
        numbers=winning_date.find_all('i',{'class':[""]})
        cash5nbrs=[]
        for number in numbers:
            cash5nbrs.append(number.text)
        date_str = date.text 
        format_str = '%m/%d/%Y'
        datetime_obj = datetime.datetime.strptime(date_str, format_str).date()
        result = db.session.query(cash5numbers).get(datetime_obj)
        if (len(winning_numbers)==0):
            winning_numbers.append(int(cash5nbrs[0]))
            winning_numbers.append(int(cash5nbrs[1]))
            winning_numbers.append(int(cash5nbrs[2]))
            winning_numbers.append(int(cash5nbrs[3]))
            winning_numbers.append(int(cash5nbrs[4]))
            winning_numbers.append(str(payout))
        if (result == None):
            data = cash5numbers(pick_date=datetime_obj,
                num1=int(cash5nbrs[0]),
                num2=int(cash5nbrs[1]),
                num3=int(cash5nbrs[2]),
                num4=int(cash5nbrs[3]),
                num5=int(cash5nbrs[4]),
                winning_payout=str(payout))
            db.session.add(data)
            db.session.commit()
    session.close()
    return render_template("index.html", est_jackpot=est_jackpot, winning_numbers=winning_numbers)

@app.route("/cash5", methods = ["GET", "POST"])
def cash5():

    session = Session(bind=engine)
    cash5_df=[]
    cash5_df = pd.read_sql_query('SELECT * from "numbers" ORDER BY "pick_date" DESC',con=engine)
    patterns_df=pd.DataFrame(
        [['05',0],
        ['14',0],
        ['23',0],
        ['32',0],
        ['41',0],
        ['50',0]],
        columns=['oddeven','count'])
    patterns_df=patterns_df.set_index('oddeven')

    lowhigh_df=pd.DataFrame(
        [['05',0],
        ['14',0],
        ['23',0],
        ['32',0],
        ['41',0],
        ['50',0]],
        columns=['lowhigh','count'])
    lowhigh_df=lowhigh_df.set_index('lowhigh')
    highest_cash5_number=45
    frequency_df=pd.DataFrame(columns=['num','count'])
    first_df=frequency_df
    second_df=frequency_df
    third_df=frequency_df
    fourth_df=frequency_df
    fifth_df=frequency_df
    for number in range(highest_cash5_number):   
        frequency_df=frequency_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
        first_df=first_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
        second_df=second_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
        third_df=third_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
        fourth_df=fourth_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
        fifth_df=fifth_df.append({
            'num':number+1,
            'count':0,
        },ignore_index=True)
    frequency_df=frequency_df.set_index('num')
    first_df=first_df.set_index('num')
    second_df=second_df.set_index('num')
    third_df=third_df.set_index('num')
    fourth_df=fourth_df.set_index('num')
    fifth_df=fifth_df.set_index('num')

    todd=0
    teven=0
    for date in cash5_df.index:
        odd=0
        even=0
        low=0
        high=0
        frequency_df['count'][int(cash5_df['num1'][date])]+=1
        frequency_df['count'][int(cash5_df['num2'][date])]+=1
        frequency_df['count'][int(cash5_df['num3'][date])]+=1
        frequency_df['count'][int(cash5_df['num4'][date])]+=1
        frequency_df['count'][int(cash5_df['num5'][date])]+=1
        first_df['count'][int(cash5_df['num1'][date])]+=1
        second_df['count'][int(cash5_df['num2'][date])]+=1
        third_df['count'][int(cash5_df['num3'][date])]+=1
        fourth_df['count'][int(cash5_df['num4'][date])]+=1
        fifth_df['count'][int(cash5_df['num5'][date])]+=1

        if (int(cash5_df['num1'][date]) % 2) >0 :
            odd+=1
        else:
            even+=1
        if (int(cash5_df['num2'][date]) % 2) >0 :
            odd+=1
        else:
            even+=1
        if (int(cash5_df['num3'][date]) % 2) >0 :
            odd+=1
        else:
            even+=1
        if (int(cash5_df['num4'][date]) % 2) >0 :
            odd+=1
        else:
            even+=1
        if (int(cash5_df['num5'][date]) % 2) >0 :
            odd+=1
        else:
            even+=1
        key=str(odd)+str(even)
        patterns_df['count'][key]+=1
        todd=todd+odd
        teven=teven+even
        
        if (int(cash5_df['num1'][date]) <=22):
            low+=1
        else:
            high+=1
        if (int(cash5_df['num2'][date]) <=22):
            low+=1
        else:
            high+=1
        if (int(cash5_df['num3'][date]) <=22):
            low+=1
        else:
            high+=1
        if (int(cash5_df['num4'][date]) <=22):
            low+=1
        else:
            high+=1
        if (int(cash5_df['num5'][date]) <=22):
            low+=1
        else:
            high+=1

        key=str(low)+str(high)
        lowhigh_df['count'][key]+=1
        
    patterns_df=patterns_df.sort_values(by=['count'], ascending=False)
    lowhigh_df=lowhigh_df.sort_values(by=['count'], ascending=False)
    frequency_df=frequency_df.sort_values(by=['count'], ascending=False)

    results=[]
    allresults=[]
    odd1=int(patterns_df.index[0][0])
    even1=int(patterns_df.index[0][1])
    allresults.append(oddeven(frequency_df,results,5,odd1,even1,0))

    results=[]
    odd2=int(patterns_df.index[1][0])
    even2=int(patterns_df.index[1][1])
    allresults.append(oddeven(frequency_df,results,5,odd2,even2,0))

    results[0]=frequency_df.index[0]
    results[1]=frequency_df.index[1]
    results[2]=frequency_df.index[2]
    results[3]=frequency_df.index[3]
    results[4]=frequency_df.index[4]
    results.sort()
    allresults.append(results)

    first_df=first_df.sort_values(by=['count'], ascending=False)
    second_df=second_df.sort_values(by=['count'], ascending=False)
    third_df=third_df.sort_values(by=['count'], ascending=False)
    fourth_df=fourth_df.sort_values(by=['count'], ascending=False)
    fifth_df=fifth_df.sort_values(by=['count'], ascending=False)

    results=[]
    exists(first_df,results)
    exists(second_df,results)
    exists(third_df,results)
    exists(fourth_df,results)
    exists(fifth_df,results)
    results.sort()
    allresults.append(results)

    results=[]
    results=oddeven(first_df,results,1,odd1,even1,1)
    results=oddeven(second_df,results,2,odd1,even1,1)
    results=oddeven(third_df,results,3,odd1,even1,1)
    results=oddeven(fourth_df,results,4,odd1,even1,1)
    allresults.append(oddeven(fifth_df,results,5,odd1,even1,1))

    allresults.append((generatecombo(odd1,even1,0)))
    allresults.append((generatecombo(odd1,even1,1)))
    allresults.append((generatecombo(odd2,even2,0)))
    allresults.append((generatecombo(odd2,even2,1)))

    low_odd_nbrs=[1,3,5,7,9,11,13,15,17,19,21]
    low_even_nbrs=[2,4,6,8,10,12,14,16,18,20,22]
    high_odd_nbrs=[23,25,27,29,31,33,35,37,39,41,43,45]
    high_even_nbrs=[24,26,28,30,32,34,36,38,40,42,44]

    pattern={'num1':{'odd':0,'even':0,'low':0,'high':0},
            'num2':{'odd':0,'even':0,'low':0,'high':0},
            'num3':{'odd':0,'even':0,'low':0,'high':0},
            'num4':{'odd':0,'even':0,'low':0,'high':0},
            'num5':{'odd':0,'even':0,'low':0,'high':0}}

    test_df=cash5_df.reset_index(drop=True)
    test_df.head(10)
    for row in range(len(test_df)-1):
        for number in (['num1', 'num2', 'num3','num4','num5']):
            nbr=int(test_df.iloc[row, [test_df.columns.get_loc(number)]])
            if (nbr % 2 != 0):
                if (nbr <=21):
                    pattern[number]['odd']+=1
                    pattern[number]['low']+=1

                else:
                    pattern[number]['odd']+=1
                    pattern[number]['high']+=1
            else:
                if (nbr<=22):
                    pattern[number]['even']+=1
                    pattern[number]['low']+=1
                else:
                    pattern[number]['even']+=1
                    pattern[number]['high']+=1

    for pick in range(5):
        result=[]
        for number in (['num1','num2','num3','num4','num5']):
            if (pattern[number]['odd'] >= pattern[number]['even']): 
                if (pattern[number]['low'] >= pattern[number]['high']):
                    nbr=random.sample(low_odd_nbrs,1)
                    result.append(nbr[0])
                    low_odd_nbrs.remove(nbr[0])
                else:
                    nbr=random.sample(high_odd_nbrs,1)
                    result.append(nbr[0])
                    high_odd_nbrs.remove(nbr[0])
            else:
                if (pattern[number]['low'] > pattern[number]['high']):
                    nbr=random.sample(low_even_nbrs,1)
                    result.append(nbr[0])
                    low_even_nbrs.remove(nbr[0])
                else:
                    nbr=random.sample(high_even_nbrs,1)
                    result.append(nbr[0])
                    high_even_nbrs.remove(nbr[0])
        allresults.append(result)

    info={}
    allresults_dict=[]
    for result in allresults:
        result.sort()
        info = {
            "first":str(result[0]),
            "second":str(result[1]),
            "third":str(result[2]),
            "fourth":str(result[3]),
            "fifth":str(result[4]),
        }
        allresults_dict.append(info)
    session.close()
    return jsonify(allresults_dict)

@app.route("/cash5/savenumbers/<results>", methods = ['GET','POST'])
def savenumbers(results):

    methods = [
        ['First Highest Odd/Even Pattern Frequent Numbers'],
        ['Second Highest Odd/Even Pattern Frequent Numbers'],
        ['Top 5 Frequent Picked Numbers'],
        ['Top 5 Frequent Numbers in Pick Postions'],
        ['First Highest Odd/Even Pattern with Most Frequent Numbers in Pick Position'],
        ['First Highest Odd/Even Pattern Random Numbers Odd Dominating'],
        ['Second Highest Odd/Even Pattern Random Numbers Odd Dominating'],
        ['First Highest Odd/Even Pattern Random Numbers Even Dominating'],
        ['Second Highest Odd/Even Pattern Random Numbers Even Dominating'],
        ['Random Selection One Top Odd-low, Odd-high, Even-low, Even-high per position'],
        ['Random Selection Two Top Odd-low, Odd-high, Even-low, Even-high per position'],
        ['Random Selection Three Top Odd-low, Odd-high, Even-low, Even-high per position'],
        ['Random Selection Four Top Odd-low, Odd-high, Even-low, Even-high per position'],
        ['Random Selection Five Top Odd-low, Odd-high, Even-low, Even-high per position']]

    session = Session(bind=engine)
    result_dict=json.loads(results)
    date_today = datetime.date.today()
    found = session.query(suggested_picks.suggested_date).filter(suggested_picks.suggested_date==date_today).count()
    print("found :",found)
    if (found == 0):
        status='Successful'
        method_num=0
        for result in result_dict:
            data = suggested_picks(suggested_date=date_today,
                    method_name=methods[method_num],
                    num1=int(result['num1']),
                    num2=int(result['num2']),
                    num3=int(result['num3']),
                    num4=int(result['num4']),
                    num5=int(result['num5']))
            method_num+=1
            db.session.add(data)
            db.session.commit()
    else:
        status='Unsuccessful'
    session.close()
    return jsonify(status)

if __name__=="__main__":
    app.run(debug=True)    