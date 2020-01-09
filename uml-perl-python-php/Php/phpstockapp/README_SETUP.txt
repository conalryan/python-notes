1. Copy the phpstockapp folder into the htdocs folder of your local server
	Example: Using xampp setup on windows, place the phpstockfolder here:
	C:\xampp\htdocs\phpstockapp
2. In the phpstockkapp folder you will find a sub folder labeled sql and a file labeled mysql_db_setup.sql
	Use the sql statements to setup the sql databse that the app will connect to.
3. Start your local server and navigate to:
	http://localhost/phpstockapp
4. Enter a stock symbol
	Example: aapl or msft and click Get Quote
	Action: you will be redirected to the appropriate quote at yahoo finance
5. The Quotes page is locked by default.  You must login to access your quotes.
	Click the security drop down menu in the top right corner -> select Login
	Enter: monty as the user.
	Enter: some_pass as the password.
	Action: You will be redirected to monty's quotes page.