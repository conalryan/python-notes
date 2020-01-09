<?php

$error = filter_input(INPUT_GET, 'err', $filter = FILTER_SANITIZE_STRING);
 
if (! $error) {
    $error = 'Oops! An unknown error happened.';
}

include 'header.php';?>

    <div class="col-md-6 col-md-offset-3">
        <h1>There was a problem</h1>
        <p class="error"><?php echo $error; ?></p>
    </div>

<?php include 'footer.php';?>