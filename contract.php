<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "devfest-the oblivionn";
$conn = new mysqli($servername, $username, $password, $database);





$sql1 = "SELECT Application_ID FROM applications ORDER BY Application_ID DESC LIMIT 1";
$result1 = $conn->query($sql1);
while ($row1 = $result1->fetch_assoc())
{
  $app_prev = $row1["Application_ID"] ;
}

$app = (int)($app_prev[2]+$app_prev[3]+$app_prev[4]);

if($app < 9)
  $app = "A-00".(string)($app+1);
else
  $app = "A-0".(string)($app+1);


$sql3 = "SELECT COUNT(*) as count FROM Applications";
$result3 = $conn->query($sql3);
while ($row3 = $result3->fetch_assoc())
{
  $count = $row3["count"] ;
}
if($count <= 10)
{
  $sql = "SELECT Contractor_ID from applications where Contractor_ID = '".$_GET["con_id"]."'";
  $result = $conn->query($sql);
  while ($row = $result->fetch_assoc())
  {
    if($row["Contractor_ID"] == $_GET["con_id"])
    {
      header("Location: http://localhost/devfest-the oblivionn/contractor.html");
      exit();
    }
  }
  $sql2 = "INSERT INTO applications (Application_ID, Price, Contractor_ID) VALUES ('".$app."','".$_GET["price"]."','".$_GET["con_id"]."')";
  
  if ($conn->query($sql2) === TRUE) {

    echo "New record created successfully";
  } else {
    echo "Error: " . $sql2 . "<br>" . $conn->error;
  }
  
  header("Location: http://localhost/devfest-the oblivionn/contractor3.html");
  exit();

}

else
{
  
  header("Location: http://localhost/devfest-the oblivionn/contractor2.php");
  exit();



}

?>