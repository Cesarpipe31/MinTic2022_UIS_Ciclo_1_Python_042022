<?php
    $data = file_get_contents("contactos.json");
    $contactos = json_decode($data, true);
    foreach ($contactos as $contacto)
    {
        echo '<pre>';
        print_r($contacto);
        echo '</pre>';
    }
?>