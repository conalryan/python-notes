<?php
include_once 'includes/functions.php';
 
sec_session_start();
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
 </head>

  <body>
    <div class="container">

      <div class="col-md-4 col-md-offset-4">
        <form class="form-signin" action="controller/loginController.php" method="post" name="login_form">
          <h2 class="form-signin-heading">Please sign in</h2>

          <label for="inputUserName" class="sr-only">User Name</label>
          <input type="text" id="userName" name="userName" class="form-control" placeholder="User Name" required autofocus>
          
          <label for="inputPassword" class="sr-only">Password</label>
          <input type="password" id="userPassword" name="userPassword" class="form-control" placeholder="Password" required>
          
          <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
        </form>
      </div>

    </div> <!-- /container -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script> 
  </body>
</html>