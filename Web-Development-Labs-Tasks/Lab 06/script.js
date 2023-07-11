function isPrime(){
    var input = Number(document.getElementById("inputPrime").value);
    var primeFlag = 0;

    if(input == 0 || input == 1){
        primeFlag = 1;
    }

    for(let i = 2; i <= (input/2); i++){
        if(input % i == 0){
            primeFlag = 1;
            break;
        }
    }

    if(primeFlag == 1){
        document.getElementById("prime-result").innerHTML = "Not a prime";
    }
    else{
        document.getElementById("prime-result").innerHTML = "Is a prime";

    }
}

function isLeap(){

    var year = Number(document.getElementById("inputYear").value);

    if ((year % 4 == 0)  && (year % 100 != 0) || (year % 400 == 0)) {
        document.getElementById("leap-result").innerHTML = "Is a leap year";
    }
    else{
        document.getElementById("leap-result").innerHTML = "Not a leap year";
   
    }

}

function changeBackground(boxNum){
    if(boxNum == "1"){
        document.getElementById("big-box").style.backgroundImage = "URL('./images/p1.jpeg')";
    }

    if(boxNum == "2"){
        document.getElementById("big-box").style.backgroundImage = "URL('./images/p2.jpeg')";
    }

    if(boxNum == "3"){
        document.getElementById("big-box").style.backgroundImage = "URL('./images/p3.jpeg')";
    }

    if(boxNum == "-0"){
        document.getElementById("big-box").style.backgroundImage = "URL('./images/white.png')";
    }

}