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

$query = "SHOW TABLES LIKE 'myInfo'";
$result = mysqli_query($conn, $query);

if (mysqli_num_rows($result) == 0) {
    $query = "CREATE TABLE myInfo (
        id int(11) NOT NULL PRIMARY KEY,
        firstName varchar(50),
        lastName varchar(50),
        birth varchar(50)
    )";
    mysqli_query($conn, $query);

    $query = "INSERT INTO myInfo (id, firstName, lastName, birth) VALUES (1, 'Joseph', 'Joestar', '1999-05-12')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO myInfo (id, firstName, lastName, birth) VALUES (2, 'Jonathan', 'Joestar', '1996-12-14')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO myInfo (id, firstName, lastName, birth) VALUES (3, 'Jotaro', 'Joestar' ,'2008-02-08')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO myInfo (id, firstName, lastName, birth) VALUES (4, 'Dio', 'Brando' ,'1889-02-29')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO myInfo (id, firstName, lastName, birth) VALUES (5, 'Diego', 'Brando' ,'1889-02-29')";
    mysqli_query($conn, $query);

    echo "Table Created";

}
else{

    echo "Table already exists";
}

$query = "SELECT * FROM myInfo";
$result = mysqli_query($conn, $query);

echo "<br>";
echo "<br>";
echo "Full Table";

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last name</th>
                <th>Birthday</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['id']}</td>
                    <td>{$row['firstName']}</td>
                    <td>{$row['lastName']}</td>
                    <td>{$row['birth']}</td>
                  </tr>";
}
echo "</table><br><br>";

echo "<br>";
echo "<br>";
echo "First Name & Last Name from Table";

$query = "SELECT firstName,lastName FROM myInfo";
$result = mysqli_query($conn, $query);

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>First Name</th>
                <th>Last name</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['firstName']}</td>
                    <td>{$row['lastName']}</td>
                  </tr>";
}
echo "</table><br><br>";

echo "<br>";
echo "<br>";
echo "All info on Only people with last name, Brando Table";

$query = "SELECT * FROM myInfo WHERE lastName = 'Brando'";
$result = mysqli_query($conn, $query);

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
    <th>ID</th>
    <th>First Name</th>
    <th>Last name</th>
    <th>Birthday</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
    <td>{$row['id']}</td>
    <td>{$row['firstName']}</td>
    <td>{$row['lastName']}</td>
    <td>{$row['birth']}</td>
                  </tr>";
}

echo "</table><br><br>";


echo "<br>";
echo "<br>";
echo "Only First & Last name of people with last name, Joestar Table";

$query = "SELECT firstName,lastName FROM myInfo WHERE lastName = 'Joestar'";
$result = mysqli_query($conn, $query);

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>First Name</th>
                <th>Last name</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['firstName']}</td>
                    <td>{$row['lastName']}</td>
                  </tr>";
}
echo "</table><br><br>";


?>