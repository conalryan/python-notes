<?php

//

function sec_session_start() {
    $session_name = 'sec_session_id';   // Set a custom session name
    // Sets the session name to the one set above.
    session_name($session_name);
    if(!isset($_SESSION)) { 
        session_start(); // Start the PHP session 
    }            
    session_regenerate_id(true);    // regenerated the session, delete the old one. 
}

function login($host, $user, $password, $database) {
 
        //$GLOBALS['$mysqli'] = new mysqli($host, $user, $password, $database);   
        $mysqli = new mysqli($host, $user, $password, $database);   

        // Check connection
        if ($mysqli->connect_error) {
            die("Connection failed: " . $mysqli->connect_error);
            header('Location: ../error.php?error=2');
        }
        //echo "Connected successfully";
        $_SESSION['userName'] = $user;
        $_SESSION['userPassword'] = $password;
        $_SESSION['connection'] = $mysqli;

        // Get the user-agent string of the user.
        $user_browser = $_SERVER['HTTP_USER_AGENT'];
        $_SESSION['login_string'] = hash('sha512', $password . $user_browser);
        header('Location: ../myquotes.php');
}

function logout($mysqli) {

    if($_SESSION['conn'] != null) {
        $_SESSION['conn']->close();
        session_unset();
        session_destroy();
        header('Location: ../logout.php');
    } else {
        header('Location: ../error.php?error=3');
    }
    /*
    // close db connection
    if($GLOBALS['$mysqli'] != null) {
        $GLOBALS['$mysqli']->close();
        // remove all session variables
        session_unset(); 
        // destroy the session 
        session_destroy(); 
        header('Location: ../logout.php');
    } else {
        header('Location: ../error.php?error=3');
    }
    */
}

function login_check($mysqli) {
    // Check if all session variables are set 
    if (isset($_SESSION['username'], $_SESSION['login_string'])) {
 
        $login_string = $_SESSION['login_string'];
        $username = $_SESSION['username'];
 
        // Get the user-agent string of the user.
        $user_browser = $_SERVER['HTTP_USER_AGENT'];
    } else {
        // Not logged in 
        return false;
    }
}