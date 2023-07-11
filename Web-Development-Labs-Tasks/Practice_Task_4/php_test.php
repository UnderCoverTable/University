<?php

    $x = 5;
    $y = 6;

    echo "$x + $y = ";
    echo $x + $y;
    echo "<br>";
    
    echo "$x - $y = ";
    echo $x - $y;
    echo "<br>";

    echo "$x * $y = ";
    echo $x * $y;
    echo "<br>";


    echo "$x / $y = ";
    echo $x / $y;
    echo "<br>";

    echo "$x + 1 = ";
    echo $x += 1;
    echo "<br>";

    echo "$y - 1 = ";
    echo $y -= 1;
    echo "<br>";

    $x = 1;
    while($x <= 10) {
        echo "x = : $x
         <br>";
        $x++;
    }

    $x = 2;
    $i = 1;
    do {
        echo "$x * $i = " . $x * $i . "<br>";
        $i++;
    } while ($i <= 10);

    $x = 0;
    $i = 1;
    for ($i; $i <= 11; $x+=3) {
        echo "The number is: $x <br>";
        $i++;
    }

    $x = 5;
    if($x == 5){
        echo "x = 5";
    }
    else{
        echo "x != 5";
    }

    echo "<br>";
    $abc = array("A", "B", "C");
    echo "alphabet = " . $abc[0];
    echo "<br>";
    echo "alphabet = " . $abc[1];
    echo "<br>";
    echo "alphabet = " . $abc[2];

    




?>