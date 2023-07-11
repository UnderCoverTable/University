function isPalindrome(){
    var inputPal = document.getElementById("palin").value;
    var j = 0;
    j = Number(j);


    var flag = 0;
    var len = inputPal.length;
    console.log(inputPal.length);

    
    for(let i = len-1; i > (inputPal.length / 2) - 1; i--){
        console.log(inputPal[i]);
        console.log(inputPal[j]);



        if(inputPal[i] != inputPal[j]){
            flag = 1;
        }
        j++;
        
    }
    

    if(flag == 1){
        document.getElementById("palindrome-result").innerHTML = "NO";
    }
    else{
        document.getElementById("palindrome-result").innerHTML = "YES";
    }

}


function bubbleSort(){

    var array1 = [1,5,6,9,8,7];
    document.getElementById("array").innerHTML = "Unsorted = "  + array1 ;


    for(let i = 0; i < array1.length; i++){
        
        for(let j = 0; j < ( array1.length - i) - 1; j++){

            if(array1[j] > array1[j+1]){

                var temp = array1[j]
                array1[j] = array1[j + 1]
                array1[j+1] = temp

            }

        
        }

      
    }
    document.getElementById("array-sorted").innerHTML = "Sorted = "  + array1 ;

    


}

function tables(){

    var Inputnum = prompt("Enter a number");
    var i = 1;

    document.getElementById("table0").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table1").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table2").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table3").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table4").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table5").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table6").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table7").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table8").innerHTML = Inputnum * i;
    i++;
    document.getElementById("table9").innerHTML = Inputnum * i;
    i++;

   

}

function arrayDif(){

    

    var intArray1 = [1,2,3,4,5,6];
    var arrayLen = intArray1.length;
    var ansArray = [];


    console.log(arrayLen);
    var j  =0;
    var i  =0;


    for(i; i != arrayLen; i++){
        for(var j = 0; j != arrayLen; j++){
            console.log(intArray1[j],intArray1[i]);

            if(intArray1[j] - intArray1[i] == 2 || intArray1[j] - intArray1[i] == -2){
                ansArray.push(["["+intArray1[i] , intArray1[j] +"]"]);
            }


        }


    }
    document.getElementById("arrr").innerHTML = intArray1 ;

    document.getElementById("arDif").innerHTML = ansArray ;
    







}


function area(){
    var totalArea = 0;

    var areaRect1 = 7*3;
    var areaRect2 = 7*3;
    var areaTri = 1/2 * 3 * 5;

    totalArea = areaRect1 + areaRect2 + areaTri;
    document.getElementById("result").innerHTML = totalArea ;





}