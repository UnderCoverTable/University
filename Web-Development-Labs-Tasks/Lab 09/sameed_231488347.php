<?php
    echo "<br>TASK 1<br>";
    $colors = array("red","green","blue");

    foreach($colors as $colorItem){
        echo "$colorItem <br>";
    }

    echo "<br>TASK2<br>";

    function task2func($pos,$item,$arr){
        $arr[$pos] = $item;
        foreach($arr as $arrItem){
            echo "$arrItem <br>";
        }  
    }

    task2func(3,"orange",$colors);

    echo "<br>TASK3<br>";

    $inc = 0;
    $origLetter;
    $name = array("s","a","m","e","e","d");
    foreach($name as $letter){
        $origLetter = $letter;

        $inc = $letter++;
        $inc = $letter++;
        $inc = $letter++;
        $inc = $letter++;


        echo "$origLetter  -->  $inc <br>";
    }

    echo "<br>TASK4<br>";

    $temps = array(10,20,30,40,50,60,70,80,90,100);
    $avg = 1;
    $sum = 1;
    $tempsLen = count($temps);

    $max5;
    $min5;


    foreach($temps as $tempsItem){
        $sum += $tempsItem;
    }  

    rsort($temps);
    $max5 = array_slice($temps, 0, 5);

    sort($temps);
    $min5 = array_slice($temps, 0, 5);

    $avg = $sum / $tempsLen;
    echo "Avergae is : $avg <br>";

    echo "Max 5 vals are : <br>";
    foreach($max5 as $arrItem){
        echo "$arrItem <br>";
    }  

    echo "Min 5 vals are : <br>";
    foreach($min5 as $arrItem){
        echo "$arrItem <br>";
    }  


    echo "<br>TASK5<br>";

    function task5func($posStart,$posEnd,$arr){
       $sum1 = 0;

       for($i = $posStart; $i <= $posEnd; $i++){
            $sum1 += $arr[$i];
       }

        echo "Sum is $sum1 <br>";

    }

    task5func(1,3,array(1,2,3,4,5));

    echo "<br>TASK6<br>";

    for($i = 200; $i <= 250; $i++){
        if($i % 4 == 0){
            echo "$i <br>";
        }
    }

    

?>