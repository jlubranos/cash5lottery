function getNumbers() {
    d3.json(`/cash5`).then((response)=>{
        var Number=d3.select("#conefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[3].first)

        var Number=d3.select("#conesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[3].second)

        var Number=d3.select("#conethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[3].third)

        var Number=d3.select("#conefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[3].fourth)

        var Number=d3.select("#conefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[3].fifth)

        var Number=d3.select("#ctwofirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[5].first)

        var Number=d3.select("#ctwosecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[5].second)

        var Number=d3.select("#ctwothird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[5].third)

        var Number=d3.select("#ctwofourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[5].fourth)

        var Number=d3.select("#ctwofifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[5].fifth)

        var Number=d3.select("#cthreefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[6].first)

        var Number=d3.select("#cthreesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[6].second)

        var Number=d3.select("#cthreethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[6].third)

        var Number=d3.select("#cthreefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[6].fourth)

        var Number=d3.select("#cthreefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[6].fifth)

        var Number=d3.select("#cfourfirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[7].first)

        var Number=d3.select("#cfoursecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[7].second)

        var Number=d3.select("#cfourthird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[7].third)

        var Number=d3.select("#cfourfourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[7].fourth)

        var Number=d3.select("#cfourfifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[7].fifth)

        var Number=d3.select("#cfivefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[8].first)

        var Number=d3.select("#cfivesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[8].second)

        var Number=d3.select("#cfivethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[8].third)

        var Number=d3.select("#cfivefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[8].fourth)

        var Number=d3.select("#cfivefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[8].fifth)  

        var Number=d3.select("#ronefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[9].first)

        var Number=d3.select("#ronesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[9].second)

        var Number=d3.select("#ronethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[9].third)

        var Number=d3.select("#ronefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[9].fourth)

        var Number=d3.select("#ronefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[9].fifth)

        var Number=d3.select("#rtwofirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[10].first)

        var Number=d3.select("#rtwosecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[10].second)

        var Number=d3.select("#rtwothird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[10].third)

        var Number=d3.select("#rtwofourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[10].fourth)

        var Number=d3.select("#rtwofifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[10].fifth)

        var Number=d3.select("#rthreefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[11].first)

        var Number=d3.select("#rthreesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[11].second)

        var Number=d3.select("#rthreethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[11].third)

        var Number=d3.select("#rthreefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[11].fourth)

        var Number=d3.select("#rthreefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[11].fifth)

        var Number=d3.select("#rfourfirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[12].first)

        var Number=d3.select("#rfoursecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[12].second)

        var Number=d3.select("#rfourthird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[12].third)

        var Number=d3.select("#rfourfourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[12].fourth)

        var Number=d3.select("#rfourfifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[12].fifth)

        var Number=d3.select("#rfivefirst");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[13].first)

        var Number=d3.select("#rfivesecond");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[13].second)

        var Number=d3.select("#rfivethird");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[13].third)

        var Number=d3.select("#rfivefourth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[13].fourth)

        var Number=d3.select("#rfivefifth");
        var h1=Number.selectAll("h1");
        h1.remove();
        Number.append("h1").text(response[13].fifth)         
    });
}

function saveNumbers() {
    var results=[];
    var pick5={};
    $(document).ready(function(){
        pick5['num1'] = $(this).find("#conefirst").children().text();
        pick5['num2'] = $(this).find("#conesecond").children().text();
        pick5['num3'] = $(this).find("#conethird").children().text();
        pick5['num4'] = $(this).find("#conefourth").children().text();
        pick5['num5'] = $(this).find("#conefifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#ctwofirst").children().text();
        pick5['num2'] = $(this).find("#ctwosecond").children().text();
        pick5['num3'] = $(this).find("#ctwothird").children().text();
        pick5['num4'] = $(this).find("#ctwofourth").children().text();
        pick5['num5'] = $(this).find("#ctwofifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#cthreefirst").children().text();
        pick5['num2'] = $(this).find("#cthreesecond").children().text();
        pick5['num3'] = $(this).find("#cthreethird").children().text();
        pick5['num4'] = $(this).find("#cthreefourth").children().text();
        pick5['num5'] = $(this).find("#cthreefifth").children().text();
        results.push(pick5);
        
        pick5={};
        pick5['num1'] = $(this).find("#cfourfirst").children().text();
        pick5['num2'] = $(this).find("#cfoursecond").children().text();
        pick5['num3'] = $(this).find("#cfourthird").children().text();
        pick5['num4'] = $(this).find("#cfourfourth").children().text();
        pick5['num5'] = $(this).find("#cfourfifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#cfivefirst").children().text();
        pick5['num2'] = $(this).find("#cfivesecond").children().text();
        pick5['num3'] = $(this).find("#cfivethird").children().text();
        pick5['num4'] = $(this).find("#cfivefourth").children().text();
        pick5['num5'] = $(this).find("#cfivefifth").children().text();
        results.push(pick5);

        pick5['num1'] = $(this).find("#ronefirst").children().text();
        pick5['num2'] = $(this).find("#ronesecond").children().text();
        pick5['num3'] = $(this).find("#ronethird").children().text();
        pick5['num4'] = $(this).find("#ronefourth").children().text();
        pick5['num5'] = $(this).find("#ronefifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#rtwofirst").children().text();
        pick5['num2'] = $(this).find("#rtwosecond").children().text();
        pick5['num3'] = $(this).find("#rtwothird").children().text();
        pick5['num4'] = $(this).find("#rtwofourth").children().text();
        pick5['num5'] = $(this).find("#rtwofifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#rthreefirst").children().text();
        pick5['num2'] = $(this).find("#rthreesecond").children().text();
        pick5['num3'] = $(this).find("#rthreethird").children().text();
        pick5['num4'] = $(this).find("#rthreefourth").children().text();
        pick5['num5'] = $(this).find("#rthreefifth").children().text();
        results.push(pick5);
        
        pick5={};
        pick5['num1'] = $(this).find("#rfourfirst").children().text();
        pick5['num2'] = $(this).find("#rfoursecond").children().text();
        pick5['num3'] = $(this).find("#rfourthird").children().text();
        pick5['num4'] = $(this).find("#rfourfourth").children().text();
        pick5['num5'] = $(this).find("#rfourfifth").children().text();
        results.push(pick5);

        pick5={};
        pick5['num1'] = $(this).find("#rfivefirst").children().text();
        pick5['num2'] = $(this).find("#rfivesecond").children().text();
        pick5['num3'] = $(this).find("#rfivethird").children().text();
        pick5['num4'] = $(this).find("#rfivefourth").children().text();
        pick5['num5'] = $(this).find("#rfivefifth").children().text();
        results.push(pick5);
        results = JSON.stringify(results);
        d3.json(`/cash5/savenumbers/${results}`).then((response)=>{
            console.log("result :",response);
            if (response=='Unsuccessful')
                {
                alert("Numbers already saved for today.");
                }
            else {
                alert("Numbers Saved");
                }
        });
    });
}

function analyzeNumber() {
    var i;
    var predstring;
    iframe=document.getElementById("frameid");
    let iframeWindow = iframe.contentWindow;
    let doc = iframe.contentDocument;
    pick=doc.getElementById("picks");
    d3.json(`/cash5/analyzeNumbers`).then((response)=>{
        for (i=0;i<response.length;i++) {
            var datelist=response[i][0].split(" ");
            var date=datelist[2].concat(' ',datelist[1],' ,',datelist[3]);
            var num1=response[i][1];
            var num2=response[i][2];
            var num3=response[i][3];
            var num4=response[i][4];
            var num5=response[i][5];
            predstring="";
            predstring= date.concat(' - ',num1,',',num2,',',num3,',',num4,',',num5);
            pick.append(new Option(predstring,String(i+1)));
        }
    });
}

function getSelected() {

    var oneoffive=0;
    var twooffive=0;
    var threeoffive=0;
    var fouroffive=0;
    var fiveoffive=0;
    var pick=document.getElementById("picks");
    var selected = pick.options[pick.selectedIndex].text;
    var wtable=document.getElementById("wnumbers");
    var selectedlist=selected.split(' - ');
    var pnumlist = selectedlist[1].split(',');
    d3.json(`/cash5/winningNumbers`).then((response)=>{
        for (i=0;i<response.length;i++) {
            var count=0;
            var row = wtable.insertRow(i+1);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var num1 = row.insertCell(2);
            var num2 = row.insertCell(3);
            var num3 = row.insertCell(4);
            var num4 = row.insertCell(5);
            var num5 = row.insertCell(6);
            var datelist1 = response[i][0].split(",");
            var day = datelist1[0];
            datelist2 = datelist1[1].split(" ");
            date = datelist2[2].concat(" ",datelist2[1],' ,',datelist2[3]);
            cell1.innerHTML=day;
            cell1.style.color="yellow";
            cell2.innerHTML=date;
            cell2.style.color="#cc00cc";
            num1.innerHTML=response[i][1];
            if (pnumlist[0]==response[i][1]) {
                count+=1;
                num1.style.color="red";
            }
            num2.innerHTML=response[i][2];
            if (pnumlist[1]==response[i][2]) {
                count+=1;
                num2.style.color="red";
            }
            num3.innerHTML=response[i][3];
            if (pnumlist[2]==response[i][3]) {
                count+=1;
                num3.style.color="red"
            }
            num4.innerHTML=response[i][4];
            if (pnumlist[3]==response[i][4]) {
                count+=1;
                num4.style.color="red"
            }
            num5.innerHTML=response[i][5];
            if (pnumlist[4]==response[i][5]) {
                count+=1;
                num5.style.color="red"
            }
            switch (count) {
                case 1:
                  oneoffive+=1;
                  break;
                case 2:
                  twooffive+=1;
                  break;
                case 3:
                   threeoffive+=1;
                  break;
                case 4:
                  fouroffive+=1;
                  break;
                case 5:
                  fiveoffive+=1;
                  break;
            }
        }
        var results="Winning Numbers".concat(" (1/5:",oneoffive,")   (2/5:",twooffive,
                        ")   (3/5:",threeoffive,")   (4/5:",fouroffive,")   (5/5:",fiveoffive,
                        ")     Total Draws:",response.length);
        document.getElementById('results').innerHTML=results;
    });
}
