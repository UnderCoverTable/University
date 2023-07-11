<?php

$host = "localhost";
$username = "root";
$password = "";
$dbname = "myDB";

$conn = mysqli_connect($host, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$query = "SELECT prod_type, MIN(prod_price) FROM products6 GROUP BY prod_type";
$result = mysqli_query($conn, $query);

echo "Output";
echo "<br>";
echo "<br>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "{$row['prod_type']} - '$'{$row['MIN(prod_price)']}";
    echo "<br>";

}



?>