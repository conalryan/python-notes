<?php
include_once '../includes/functions.php';
 
sec_session_start(); // Our custom secure way of starting a PHP session.
 
if (isset($_POST['userName'], $_POST['userPassword'])) {
    $userName = $_POST['userName'];
    $userPassword = $_POST['userPassword']; // The hashed password.
 
    login("localhost", "$userName", "$userPassword", "phpstockapp") ;
}
