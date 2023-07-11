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

$query = "SHOW TABLES LIKE 'EMP_INFO'";
$result = mysqli_query($conn, $query);

if (mysqli_num_rows($result) == 0) {
    $query = "CREATE TABLE EMP_INFO (
        EMP_IDNO int(11) NOT NULL PRIMARY KEY,
        EMP_FNAME varchar(50),
        EMP_LNAME varchar(50),
        EMP_DEPT varchar(50)
    )";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (127323, 'Joseph', 'Joestar', '57')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (526689, 'Jonathan', 'Joestar', '63')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (843759, 'Jotaro', 'Joestar' ,'57')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (328717, 'Dio', 'Brando' ,'63')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (444527, 'Diego', 'Brando' ,'47')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (659831, 'Jhonny', 'Brando' ,'47')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (847647, 'Alexov', 'Kujo' ,'57')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (478861, 'Enrico', 'Manuel' ,'47')";
    mysqli_query($conn, $query);

    $query = "INSERT INTO EMP_INFO (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES (555935, 'Alexi', 'Kulesewar' ,'57')";
    mysqli_query($conn, $query);

    echo "Table Created";

}
else{

    echo "Table already exists";
}


$query = "SELECT * FROM EMP_INFO WHERE EMP_DEPT = '57' OR EMP_DEPT = '63' ORDER BY EMP_DEPT DESC";
$result = mysqli_query($conn, $query);

echo "<br>";
echo "<br>";
echo "Employees from Department 57 and 63 Sorted Descending by EMP_DEPT";

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>EMP IDNO</th>
                <th>EMP FNAME</th>
                <th>EMP LNAME</th>
                <th>EMP DEPT</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['EMP_IDNO']}</td>
                    <td>{$row['EMP_FNAME']}</td>
                    <td>{$row['EMP_LNAME']}</td>
                    <td>{$row['EMP_DEPT']}</td>

                  </tr>";
}
echo "</table><br><br>";



echo "<br>";
echo "<br>";
echo "Employees from Department 57 and 63 Sorted Ascending by EMP_FNAME";


$query = "SELECT * FROM EMP_INFO WHERE EMP_DEPT = '57' OR EMP_DEPT = '63' ORDER BY EMP_FNAME ASC";
$result = mysqli_query($conn, $query);

echo "<table cellspacing='10' cellpadding='10'>";
echo "<tr>
                <th>EMP IDNO</th>
                <th>EMP FNAME</th>
                <th>EMP LNAME</th>
                <th>EMP DEPT</th>
              </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>
                    <td>{$row['EMP_IDNO']}</td>
                    <td>{$row['EMP_FNAME']}</td>
                    <td>{$row['EMP_LNAME']}</td>
                    <td>{$row['EMP_DEPT']}</td>

                  </tr>";
}
echo "</table><br><br>";


?>