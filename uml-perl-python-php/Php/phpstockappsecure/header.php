<?php
 
sec_session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Php Stock App</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
	<link ref="stylesheet" type="text/css" href="css/style.css"/>
</head>
<body>

	<!-- Static navbar -->
    <nav class="navbar navbar-default navbar-static-top navbar-inverse">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Php Stock App</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            
            <?php if (login_check($mysqli) == true) : ?>
              <li>Welcome <?php echo htmlentities($_SESSION['username']); ?>!</li>
        
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Security<span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="login.php">Login</a></li>
                <li><a href="logout.php">Logout</a></li>
              </ul>
              </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

	<div class="container">

';?>