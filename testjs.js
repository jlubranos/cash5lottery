var tdChange = document.getElementById('tdChange');

var numbers = [.03, .18, -.018];
var randNumber = numbers[Math.floor(Math.random() * numbers.length)];
if (Math.abs(randNumber) > .025){ //bold significant changes
    tdChange.style.fontWeight = 'bold';
}

tdChange.style.color = randNumber >= 0 ? 'green' : 'red';
<p id='tdChange'>This is a paragraph</p>

// OR 

var tdChange = $('#tdChange');
var numbers = [.03, .18, -.018];
var randNumber = numbers[Math.floor(Math.random() * numbers.length)];

if (Math.abs(randNumber) > .025) {
    tdChange.toggleClass('bold');
}

tdChange.toggleClass(randNumber >= 0 ? 'green' : 'red');

// CSS
.bold { font-weight: bold; }
.green { color: green; }
.red { color: red; }

// IN Html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

//Inside Javascript
<p id='tdChange'>This is a paragraph</p>

// Dynamic variables

<script> 
    var k = 'value'; 
    var i = 0; 
    for(i = 1; i < 5; i++) { 
        eval('var ' + k + i + '= ' + i + ';'); 
    } 
    console.log("value1=" + value1); 
    console.log("value2=" + value2); 
    console.log("value3=" + value3); 
    console.log("value4=" + value4); 
</script> 

<!DOCTYPE html>
<html>
<body>

<h2>Iframe - Target for a Link</h2>

<iframe src="demo_iframe.htm" name="iframe_a" height="300px" width="100%" title="Iframe Example"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>

<p>When the target attribute of a link matches the name of an iframe, the link will open in the iframe.</p>

</body>
</html>