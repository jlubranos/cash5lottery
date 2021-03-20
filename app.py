import json
import random
import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, jsonify
# Flask Setup
app =  Flask(__name__)

def read_cash5csv(cash5_df):
    try:
        cash5_df=pd.read_csv('cash5numbers.csv', index_col='date')
        return cash5_df
    except:
        return cash5_df

def create_cash5csv():

    cash5_df=pd.DataFrame(columns=['date','num1','num2','num3','num4','num5'])
    executable_path = {"executable_path": "C:/Users/jlubr/bin/chromedriver_win32/chromedriver"}
    browser=Browser('chrome',**executable_path, headless=False)
    url='https://www.njlottery.com/en-us/drawgames/jerseycash.html'
    browser.visit(url)
    time.sleep(5)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    winning_dates=soup.find_all('tr',{'data-toggle':['tableWinningNumbers']})
    for winning_date in winning_dates:
        date=winning_date.find('td',{'title':['date']})
        numbers=winning_date.find_all('i',{'class':[""]})
        cash5numbers=[]
        for number in numbers:
            cash5numbers.append(number.text)
        cash5_df=cash5_df.append({
                'date':date.text,
                'num1':cash5numbers[0],
                'num2':cash5numbers[1],
                'num3':cash5numbers[2],
                'num4':cash5numbers[3],
                'num5':cash5numbers[4],
        },ignore_index=True)
    cash5_df=cash5_df.set_index('date')
    cash5_df.to_csv("cash5numbers.csv", index=True, index_label='date')
    browser.quit()
    return cash5_df        

def update_cash5csv(cash5_df):
    
    executable_path = {"executable_path": "C:/Users/jlubr/bin/chromedriver_win32/chromedriver"}
    browser=Browser('chrome',**executable_path, headless=False)
    url='https://www.njlottery.com/en-us/drawgames/jerseycash.html'
    browser.visit(url)
    time.sleep(5)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    winning_dates=soup.find_all('tr',{'data-toggle':['tableWinningNumbers']})
    for winning_date in winning_dates:
        date=winning_date.find('td',{'title':['date']})
        try:
            rec=cash5_df.loc[date.text]
            break
        except:
            numbers=winning_date.find_all('i',{'class':[""]})
            cash5numbers=[]
            for number in numbers:
                cash5numbers.append(number.text)
            rec=pd.DataFrame({
                'num1':cash5numbers[0],
                'num2':cash5numbers[1],
                'num3':cash5numbers[2],
                'num4':cash5numbers[3],
                'num5':cash5numbers[4],
            },index=[date.text])
            cash5_df = pd.concat([rec, cash5_df], ignore_index=False) 
    cash5_df.to_csv("cash5numbers.csv", index=True, index_label='date')
    browser.quit()
    return cash5_df    

def exists(numbers,results):
    row=0
    while (numbers.index[row] in results):
        row+=1
    results=results.append(numbers.index[row])
    return results

def oddeven(numbers,results,length,odd,even,count):
    row=0;
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

@app.route('/')
def home():

    return render_template("index.html")

@app.route("/cash5")
def cash5():
    cash5_df=[]
    cash5_df=read_cash5csv(cash5_df)
    if (len(cash5_df)==0):
        cash5_df=create_cash5csv()
    else:
        cash5_df=update_cash5csv(cash5_df)

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
    return jsonify(allresults_dict)
    
if __name__=="__main__":
    app.run(debug=True)