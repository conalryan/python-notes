<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';
 
sec_session_start();
 
if (login_check($mysqli) == true) {
    $logged = 'in';
} else {
    $logged = 'out';
}
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">
    <title>Signin</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link href="css/signin.css" rel="stylesheet">
    <script type="text/JavaScript" src="js/sha512.js"></script> 
    <script type="text/JavaScript" src="js/forms.js"></script> 
 </head>

  <body>

    <?php
      if (isset($_GET['error'])) {
        echo '<p class="error">Error Logging In!</p>';
      }
    ?> 

    <div class="container">

      <div class="col-md-4 col-md-offset-4">
        <form class="form-signin" action="includes/process_login.php" method="post" name="login_form">
          <h2 class="form-signin-heading">Please sign in</h2>

          <label for="inputEmail" class="sr-only">Email address</label>
          <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required autofocus>
          
          <label for="inputPassword" class="sr-only">Password</label>
          <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
          
          <button class="btn btn-lg btn-primary btn-block" type="submit" onclick="formhash(this.form, this.form.password);">Sign in</button>
        </form>
      </div>

    </div> <!-- /container -->
    
    <?php
      if (login_check($mysqli) == true) {
        echo '<div class="col-md-4 col-md-offset-4 text-center"> 
                <p>Currently logged ' . $logged . ' as ' . htmlentities($_SESSION['username']) . '.</p></div>';
        echo '<div class="col-md-4 col-md-offset-4 text-center">
                <p>Do you want to change user? <a href="includes/logout.php">Log out</a>.</p></div>';
      } else {
        echo '<div class="col-md-4 col-md-offset-4 text-center">
                <p>Currently logged ' . $logged . '.</p></div>';
        echo "<div class='col-md-4 col-md-offset-4 text-center'>
                <p>If you don't have a login, please <a href='register.php'>register</a></p></div>";
      }
    ?> 
    
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script> 
  </body>
</html>