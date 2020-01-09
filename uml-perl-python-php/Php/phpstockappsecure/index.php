<?php
include_once 'includes/functions.php';
 
sec_session_start();
?>


      <!-- Main component for a primary marketing message or call to action -->
      <div class="jumbotron">
        <h1>PHP Stock Quote App</h1>
        <p>This app was designed by Conal Ryan for the Umass Lowell class - Perl/Python/PHP Survey</p>
        <p>This app uses php and mysql to get and store quotes.</p>
        
        <!-- Get Quote -->
        <div class="col-md-6 col-md-offset-3">
        <form class="form-inline">
	 	  <div class="form-group">
		    <div class="input-group input-group-lg">
		      <input type="text" class="form-control" id="inputSymbol" placeholder="Stock Symbol">
		    </div>
		  </div>
		  <button type="submit" class="btn btn-lg btn-primary">Get Quote</button>
	    </form>
	    </div>

      </div>

      <!-- Columns -->
	    <div class="row">
	      <div class="col-xs-12 col-md-8">.col-xs-12 .col-md-8</div>
	      <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	    </div>
	    <div class="row">
	      <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	      <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	      <div class="col-xs-6 col-md-4">.col-xs-6 .col-md-4</div>
	    </div>
	    <div class="row">
	      <div class="col-xs-6">.col-xs-6</div>
	      <div class="col-xs-6">.col-xs-6</div>
	    </div>

	  <!-- Table -->
	  <table class="table table-striped">
      <thead>
        <tr>
          <th>#</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Username</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </table>

';?>

<?php include 'footer.php';?>