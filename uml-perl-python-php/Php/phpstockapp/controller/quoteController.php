<?php
include_once '../includes/functions.php';
 
sec_session_start(); // Our custom secure way of starting a PHP session.
 
if (isset($_GET['inputSymbol'])) {
    $inputSymbol = $_GET['inputSymbol'];

	header("Location: http://finance.yahoo.com/q?s=" . $inputSymbol);
} else {
	header('Location: ../error.php?error=4');
}