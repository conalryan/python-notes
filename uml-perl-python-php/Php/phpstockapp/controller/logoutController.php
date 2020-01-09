<?php
include_once '../includes/functions.php';
sec_session_start();
session_unset(); 
// destroy the session 
session_destroy();
header('Location: ../logout.php');

/*
$mysqli = $_SESSION['conn'];

//echo $mysqli;

// close db connection
//echo $_SESSION['connection'];


//logout($_SESSION['conn']);

// close db connection
    if($_SESSION['conn'] != null) {
    	$mysqli = $_SESSION['conn'];
    	$mysqli->close();
    }
        // remove all session variables
        session_unset(); 
        // destroy the session 
        session_destroy(); 
    //    header('Location: ../logout.php');
      //  header('Location: ../error.php?error=3');
    
*/
?>