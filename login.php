<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "devfest-the oblivionn";
$conn = new mysqli($servername, $username, $password, $database);

echo $_GET["password"];



$sql1 = "SELECT passcode from contractors WHERE name = '".$_GET["name"]."'";
$result1 = $conn->query($sql1);
$name = $_GET["name"];

$flag = 0;
while ($row1 = $result1->fetch_assoc())
{
  echo $row1["passcode"];
  if($row1["passcode"] == $_GET["password"])
  {
    $flag = 1;
  }
  else
  {
    $flag = -1;
  }
}

if($flag == 1)
{
  

  header("Location: http://localhost/devfest-the oblivionn/contractor.html?name=$name ");
  exit();
}
else{
  
  echo " INCORRECT PASSWORD OR CONTRACTOR_ID";
}

?>
