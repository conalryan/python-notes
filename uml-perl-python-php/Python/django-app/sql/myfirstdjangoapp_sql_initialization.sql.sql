CREATE DATABASE myfirstdjangoapp;

CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';
GRANT ALL ON myfirstdjangoapp.* TO 'monty'@'localhost';

CREATE TABLE IF NOT EXISTS `blog_posts` (
`id` int(11) NOT NULL,
  `author` varchar(30) NOT NULL,
  `title` varchar(100) NOT NULL,
  `bodyText` longtext NOT NULL,
  `timeStamp` datetime NOT NULL,
  `stock` varchar(6) NOT NULL,
  `stockPrice` decimal(6,2) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;


INSERT INTO `blog_posts` (`id`, `author`, `title`, `bodyText`, `timeStamp`, `stock`, `stockPrice`) VALUES
(1, 'Conal Ryan', 'Post one', 'Setting up the Django Database connection and blog_posts table.', '0000-00-00 00:00:00', 'aapl', '100.00'),
(2, 'Rick Newman', 'If Apple wants to transform cars, it should build this instead of copying Tesla', 'The tech world is going gaga over the prospect that mighty Apple will enter the car business and teach those fumblebums at General Motors (GM), Toyota (TM), BMW and Tesla (TSLA) how to build a 21st-century vehicle.\r\n\r\nThere are plenty of reasons to be skeptical that Apple will ever manufacture cars for public sale. The car business is a low-margin heavy industry, for instance, whereas Apple (AAPL) is a high-margin consumer-product company. It does make sense for Apple to get more involved in cars as a supplier of information, software and control systems, but not as a manufacturer running its own assembly lines.\r\n\r\nStill, it’s possible Apple might see an opening others don’t, and decide it can transform autos the way it transformed music with the iPod and iTunes, and communication with the iPhone. Bloomberg recently reported that Apple may be producing cars as early as 2020. Apple has been hiring automotive talent from Tesla (TSLA), Ford (F) and other car companies. The types of people Apple is hiring—including engineers with experience in electrification—suggest the tech giant is interested in building battery-powered cars that would somehow be better than those produced by Tesla, General Motors, BMW, Toyota and most other automakers.', '2015-02-20 16:46:00', 'AAPL', '129.50'),
(3, 'Chris Velazco', 'BlackBerry Classic review: A love letter to fans and few others', 'BlackBerry Classic review: A love letter to fans and few others\r\nLet''s put Apple, Samsung and all their ilk aside for few moments: It really wasn''t that long ago that a homegrown Canadian company called BlackBerry (well, RIM at the time) basically ruled the mobile world. The outfit''s slow decline has been chronicled, opined upon for years, and yet, some of BlackBerry''s most ardent fans still clamor for the days when QWERTY keyboards and teensy trackpads were uber-efficient status symbols instead of the relics they are now.\r\n\r\nEnter the BlackBerry Classic. The name says it all, really: It''s a paean to BlackBerry''s halcyon days, and it''s got a look plucked straight out of 2011, to boot. We took one for an extended spin to see how BlackBerry''s throwback formula holds up today, and (very long story short) it''s mostly the past mashed up with a touch of the modern. The bigger question, as usual, is whether or not it''s worth your time. I suspect you already know the answer, but read on for my full impressions.', '2015-02-10 15:00:00', 'BBRY', '9.87');
