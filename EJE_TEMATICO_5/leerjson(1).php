<?php
$data = file_get_contents("contactos.json");
$products = json_decode($data, true);
 
foreach ($products as $product) {
    echo '<pre>';
    print_r($product);
    echo '</pre>';
}
?>