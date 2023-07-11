<html>
<body>  



<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

  ID: <input name="id">
  <br><br>
  Name: <input name="name">
  <br><br>
  Type: <input name="type">
  <br><br>
  price: <input name="price" >
  <br><br>
  <input type="submit" name="submit" value="Submit">  

 
</form>

<?php

$host = "localhost";
$username = "root";
$password = "";
$dbname = "myDB";


$conn = mysqli_connect($host, $username, $password,$dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


// Create database
$sql = "CREATE DATABASE IF NOT EXISTS myDB";
if ($conn->query($sql) === TRUE) {
  echo "Database created successfully if it did not already exist";
  echo "<br>";
} else {
  echo "Error creating database: " . $conn->error;
}

$query = "SHOW TABLES LIKE 'products6'";
$result = mysqli_query($conn, $query);

if (mysqli_num_rows($result) == 0) {
    $query = "CREATE TABLE products6 (
        prod_id int(11) NOT NULL PRIMARY KEY,
        prod_name varchar(50),
        prod_type varchar(50),
        prod_price FLOAT
    )";
    mysqli_query($conn, $query);
    echo "Table Created";
}
else{
    echo "Table already exists";
}

if (isset($_POST['submit'])) {
    $query = "INSERT INTO products6 (prod_id, prod_name, prod_type, prod_price)  VALUES ('{$_POST['id']}', '{$_POST['name']}', '{$_POST['type']}', '{$_POST['price']}')";
    mysqli_query($conn, $query);
}




$query = "SELECT * FROM products6";
$result = mysqli_query($conn, $query);

echo "<br>";
echo "<br>";
echo "Products";

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>ID</th>
                <th>Name</th>
                <th>Type</th>
                <th>Price</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['prod_id']}</td>
                    <td>{$row['prod_name']}</td>
                    <td>{$row['prod_type']}</td>
                    <td>{$row['prod_price']}</td>
                  </tr>";
}
echo "</table><br><br>";


?>


<button onclick="window.location.href='budget.php'"> Min Price</button>




</body>
</html>