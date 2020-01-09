<?php
include_once 'includes/functions.php';
 
sec_session_start();
?>

<?php include 'templates/header.php';?>

  <!-- Main component for a primary marketing message or call to action -->
  <div class="jumbotron">
    <h1>PHP Stock Quote App</h1>
    <p>This app was designed by Conal Ryan for the Umass Lowell class - Perl/Python/PHP Survey</p>
    <p>This app uses php and mysql to get and store quotes.</p>
    
    <!-- Get Quote -->
    <div class="col-md-6 col-md-offset-3">
      <form class="form-inline" action="controller/quoteController.php" method="get">
        <div class="form-group">
          <div class="input-group input-group-lg">
            <input type="text" class="form-control" name="inputSymbol" id="inputSymbol" placeholder="Stock Symbol">
          </div>
        </div>
        <button type="submit" class="btn btn-lg btn-primary">Get Quote</button>
      </form>
    </div>
  </div>

  <!-- Columns -->
  <div class="row">

    <div class="col-sm-6 col-md-4">
      <div class="panel panel-primary">
        <div class="panel-heading">
          <h3 class="panel-title">S&amp;P 500</h3>
        </div>
        <div class="panel-body">
          The S&amp;P 500, or the Standard &amp; Poor's 500, is an American stock market index based on the market capitalizations of 500 large companies having common stock listed on the NYSE or NASDAQ. The S&P 500 index components and their weightings are determined by S&P Dow Jones Indices. It differs from other U.S. stock market indices, such as the Dow Jones Industrial Average or the Nasdaq Composite index, because of its diverse constituency and weighting methodology. It is one of the most commonly followed equity indices, and many consider it one of the best representations of the U.S. stock market, and a bellwether for the U.S. economy. The National Bureau of Economic Research has classified common stocks as a leading indicator of business cycles.
        </div>
      </div>
    </div>

    <div class="col-sm-6 col-md-4">
      <div class="panel panel-primary">
        <div class="panel-heading">
          <h3 class="panel-title">Nasdaq 100</h3>
        </div>
        <div class="panel-body">
          The NASDAQ-100 is a stock market index made up of 107 equity securities issued by 100 of the largest non-financial companies listed on the NASDAQ. It is a modified capitalization-weighted index. The stocks' weights in the index are based on their market capitalizations, with certain rules capping the influence of the largest components. It is based on exchange, and it is not an index of U.S.-based companies. It does not have any financial companies, since these were put in a separate index. Both of those criteria differentiate it from the Dow Jones Industrial Average, and the exclusion of financial companies distinguishes it from the S&amp;P 500.
        </div>
      </div>
    </div>
    
    <div class="col-sm-6 col-md-4">
      <div class="panel panel-primary">
        <div class="panel-heading">
          <h3 class="panel-title">Dow Jones</h3>
        </div>
        <div class="panel-body">
          The Dow Jones Industrial Average also called the Industrial Average, the Dow Jones, the Dow Jones Industrial, the Dow 30, or simply the Dow, is a stock market index, and one of several indices created by Wall Street Journal editor and Dow Jones & Company co-founder Charles Dow. The industrial average was first calculated on May 26, 1896.[1] Currently owned by S&P Dow Jones Indices, which is majority owned by McGraw-Hill Financial, it is the most notable of the Dow Averages, of which the first (non-industrial) was first published on February 16, 1885. The averages are named after Dow and one of his business associates, statistician Edward Jones. It is an index that shows how 30 large publicly owned companies based in the United States have traded during a standard trading session in the stock market. It is the second oldest U.S. market index after the Dow Jones Transportation Average, which was also created by Dow.
        </div>
      </div>
    </div>
  </div>

<?php include 'templates/footer.php';?>