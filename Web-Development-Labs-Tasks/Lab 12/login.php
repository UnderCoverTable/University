<html>
<body>  



<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

  ID: <input name="id">
  <br><br>
  Password: <input name="password">
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

$query1 = "SHOW TABLES LIKE 'users'";
// $query2 = "SHOW TABLES LIKE 'admins'";

$result = mysqli_query($conn, $query1);

if (mysqli_num_rows($result) == 0) {
    $query = "CREATE TABLE users (
        user_id int(11) NOT NULL PRIMARY KEY,
        user_password varchar(50)
    )";
    mysqli_query($conn, $query);
    echo "Table Created";
}
else{
    echo "Table already exists";
}

// $result = mysqli_query($conn, $query2);

// if (mysqli_num_rows($result) == 0) {
//     $query = "CREATE TABLE admins (
//         admin_id int(11) NOT NULL PRIMARY KEY,
//         admin_password varchar(50)
//     )";
//     mysqli_query($conn, $query);
//     echo "Table Created";
// }
// else{
//     echo "Table already exists";
// }

// Sample logins
// $query = "INSERT INTO users (user_id, user_password) VALUES (12345, '12345')";
// mysqli_query($conn, $query);

// $query = "INSERT INTO admins (admin_id, admin_password) VALUES (1234, '1234')";
// mysqli_query($conn, $query);




if (isset($_POST['submit'])) {



    $inputID = $_POST['id'];
    $inputpass = $_POST['password'];


    $query = "SELECT * FROM users WHERE user_id='$inputID'";
    $result = mysqli_query($conn, $query);

        while ($row = mysqli_fetch_assoc($result))
        {
            if($row['user_password'] == $inputpass ){
                echo "Logged in";
                session_start();

                if(rand() % 2 == 0){
                    $_SESSION["role"] = "USER";
                }
                else{
                    $_SESSION["role"] = "ADMIN";
                }
            }
            else{
                echo "Couldnt login";
            }
    
        }



    
}


?>


</body>
</html>