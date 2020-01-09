<?php
include_once 'includes/functions.php';
 
sec_session_start();
?>

<?php include 'templates/header.php';?>

  <!-- Main component for a primary marketing message or call to action -->
  <div class="jumbotron">
    <h2>My Quotes</h1>
  </div>

  <?php if(isset($_SESSION['userName'])) : ?>
      <p>Welcome <?php echo htmlentities($_SESSION['userName']); ?>!</p>

  <?php
  // SELECT data ----------------------------------------------------------------
  $servername = "localhost";
  $username = "jeffrey";
  $password = "mypass";
  $dbname = "phpstockapp";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  } 

  $sql = "SELECT id, user_name, stock_symbol, stock_price FROM stock_quotes";
  $result = $conn->query($sql);

  echo "
  <!-- Table -->
    <table class='table table-striped'>
      <thead>
          <tr>
            <th>#</th>
            <th>User</th>
            <th>Symbol</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>";
    if ($result->num_rows > 0) {
      // output data of each row
      while($row = $result->fetch_assoc()) {
        echo "
        <tr>
          </th>
            <th scope='row'>" . $row["id"] . "</th>
            <td>" . $row["user_name"] . "</td>
            <td>" . $row["stock_symbol"] . "</td>
            <td>" . $row["stock_price"] . "</td>
          </tr>";
      }
    } else {
        echo "0 results";
    }
    echo "
    </tbody>
    </table>";
  $conn->close();
  ?>
  <?php else : ?>
    <p>
      <span class="error">You are not authorized to access this page.</span> Please <a href="login.php">login</a>.
    </p>
  <?php endif; ?>

<?php include 'templates/footer.php';?>