# web-scraping-challenge
Build a web application that scrapes several websites for data related to the Mission to Mars
 and displays the information in a single HTML page.

WEB SCRAPING
The web scraping is initiated in a Jupyter Notebook using the following modules:
    Pandas
    BeautifulSoup
    Splinter - Browser
    ChromeDriverManager

A connection was made to Browser using the Chrome Driver.
The first site scraped was https://redplanetscience.com
 This site provides current news on the Mission to Mars.  The most recent news title and snippet 
 URL's were scraped into variables.

Scrape 2 came from  https://spaceimages-mars.com.  The featured home page image URL was scraped
 into a variable.

Scrape 3 came from https://galaxyfacts-mars.com.  A table of Mars facts was scraped into a
a Pandas dataframe.  Minor table cleaning was done and the dataframe was converted to HTML.
Table facts include Diameter, Mass, etc. comparisons between Mars and Earth.

The final scrape came from https://marshemispheres.com.  Here the URL's of images of the 4
 Mars hemispheres and their image titles were scraped into a dictionary.  The web scraping
 required a for loop with several find queries to locate the actual image URL's.

The next phase of the web scraping involved downloading the Jupyter Notebook into Python.
 A scrape function was created encompassing the scrape code from the Notebook for use in a
 Flask app.  Scraped data was placed into a Python dictionary called mars_info.

FLASK APP
Using Flask, render_template and PyMongo an app was created to hold the scraped data.
 A Flask app and route was set up to call the scrape function from the Python file and
 store that data in a Mongo database. A home route was also created to render the HTML
 template that will show the data on the web.
 
WEB APP
Once the data is scraped and stored in the database, the app renders an HTML template,
 index.html.  The HTML uses a bootstrap css link and bootstrap JavaScript.  A button
 is created that will activate the scrape function so that the site will show updated
 information.  

 Bootstrap grid layouts were used to show the latest Mars Mission news, the Mars featured
 planet image, the table of facts and the 4 hemisphere images and titles.