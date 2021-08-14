$servername = "localhost";
$username = "root";
$password = "";

$conn = new mysqli($servername, $username, $password,"devfest-the oblivionn");

$sql = "INSERT INTO contractors (firstname, lastname, email)
VALUES ('John', 'Doe', 'john@example.com')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}