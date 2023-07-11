// prints array and its sum
function task1(){
    var array1 = [1,2,3,4];
    var sum = 0;
    for(let i = 0;i < array1.length;i++){
        sum += array1[i] ;
    }

    document.getElementById("a").innerHTML = array1;
    document.getElementById("b").innerHTML = sum;
    

}

// 4 seperate functions for each operation

function add(){
    var n1 = Number(document.getElementById("Num1").value);
    var n2 = Number(document.getElementById("Num2").value);

    document.getElementById("operation-result").innerHTML = n1+n2;
}

function subtract(n1,n2){
    var n1 = Number(document.getElementById("Num1").value);
    var n2 = Number(document.getElementById("Num2").value);

    document.getElementById("operation-result").innerHTML = n1-n2;}

function multiply(n1,n2){
    var n1 = Number(document.getElementById("Num1").value);
    var n2 = Number(document.getElementById("Num2").value);

    document.getElementById("operation-result").innerHTML = n1*n2;}

function divide(n1,n2){
    var n1 = Number(document.getElementById("Num1").value);
    var n2 = Number(document.getElementById("Num2").value);

    document.getElementById("operation-result").innerHTML = n1/n2;}

// Takes the array input from html. sorts it and prints
function sortArray(){

    var ar = document.getElementById("arrayInput").value;

    var intArray;

    intArray = ar.split(",");
    intArray.sort();
    document.getElementById("arSort").innerHTML = intArray;



}

// validates inputs. changes the fields to appropriate color from the input

function validateForm(){

    var inpName = document.getElementById("name").value;
    var inpEmail = document.getElementById("email").value;    
    var inpPass = document.getElementById("pass").value;

    if(inpEmail == ""){
        document.getElementById("email").style.backgroundColor = "salmon";
        document.getElementById("email").style.borderBlockColor = "red";
        window.alert("Email was Empty");

    }
    if(inpName == ""){
        document.getElementById("name").style.backgroundColor = "salmon";
        document.getElementById("email").style.borderBlockColor = "red";
        window.alert("Name was Empty");

    }
    if(inpPass == "" || inpPass.length < 8){
        document.getElementById("pass").style.backgroundColor = "salmon";
        document.getElementById("pass").style.borderBlockColor = "red";
        if(inpPass.length < 8){
            window.alert("Password was less then 8 characters");

        }
        else{
            window.alert("Password was Empty");
        }


    }

}

// Calculates tip from the input bill and number of people

function tipCalc(){

    var bill = Number(document.getElementById("billed").value);
    var people = Number(document.getElementById("people").value);


    document.getElementById("tipVal1").innerHTML = "Outstanding = " + (bill*0.3)/people + "$ per person";
    document.getElementById("tipVal2").innerHTML = "Good = " + (bill*0.2)/people+ "$ per person";
    document.getElementById("tipVal3").innerHTML = "Okay = " + (bill*0.15)/people+ "$ per person";
    document.getElementById("tipVal4").innerHTML = "bad = " + (bill*0.10)/people+ "$ per person";
    document.getElementById("tipVal4").innerHTML = "Terible = " + (bill*0.05)/people+ "$ per person";






}

