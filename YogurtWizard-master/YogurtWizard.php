<?php 
echo "<b>Toppings: </b><br>";
if (isset($_GET['top'])){
 foreach($_GET['top'] as $topping){
 	echo $topping."<br>";
 }
}
?>