# **web-scraping-challenge**

Build a web application that scrapes several websites for data related to the Mission to Mars
and displays the information in a single HTML page.<br>

## **software/tools used**

* pandas:  https://pandas.pydata.org/<br>
  * libraries:<br>
    * BeautifulSoup<br>
    * splinter<br>
* Jupyter Notebook:  https://jupyter.org/<br>
* python 3<br>
  * Flask
  * PyMongo
* HTML 5<br>
* Bootstrap 5<br>
* CSS<br>

## **resources**
* Background provided as part of Georgia Tech Data Analytics Boot Camp:<br>
© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.<br>

* Sites Scraped:
*   NASA Mars News: https://redplanetscience.com<br>
*   JPL Mars Space Images: https://spaceimages-mars.com<br>
*   Mars Facts:  https://galaxyfacts-mars.com<br>
*   Astrogeology:  https://marshemispheres.com<br>

## **project background**

* In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

## **Step 1 - Scraping**

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

### **NASA Mars News**

* Scrape the NASA Mars News site (https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. 

### **JPL Mars Space Images - Featured Image**

* Visit the url for the Featured Space Image site https://spaceimages-mars.com.
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
* Make sure to find the image url to the full size `.jpg` image.
* Make sure to save a complete url string for this image.

### **Mars Facts**

* Visit the Mars Facts webpage https://galaxyfacts-mars.com and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

### **Mars Hemispheres**

* Visit the astrogeology site https://marshemispheres.com/ to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

### **Step 2 - MongoDB and Flask Application**

* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
  * Store the return value in Mongo as a Python dictionary.
* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

## **acknowledgement**

* Background provided as part of Georgia Tech Data Analytics Boot Camp:<br>
  * © 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

* Project Author:  Valerie Pippenger - https://github.com/Pip85

## **process**

**WEB SCRAPING**

*The web scraping is initiated in a Jupyter Notebook using the following modules:
    * Pandas
    * BeautifulSoup
    * Splinter - Browser
    * ChromeDriverManager

* A connection was made to Browser using the Chrome Driver.
* The first site scraped was https://redplanetscience.com
 * This site provides current news on the Mission to Mars.  The most recent news title and snippet 
 URL's were scraped into variables.

* Scrape 2 came from  https://spaceimages-mars.com.  The featured home page image URL was scraped
 into a variable.

* Scrape 3 came from https://galaxyfacts-mars.com.  A table of Mars facts was scraped into a
a Pandas dataframe.  Minor table cleaning was done and the dataframe was converted to HTML.
Table facts include Diameter, Mass, etc. comparisons between Mars and Earth.

* The final scrape came from https://marshemispheres.com.  Here the URL's of images of the 4
 Mars hemispheres and their image titles were scraped into a dictionary.  The web scraping
 required a for loop with several find queries to locate the actual image URL's.

* The next phase of the web scraping involved downloading the Jupyter Notebook into Python.
 A scrape function was created encompassing the scrape code from the Notebook for use in a
 Flask app.  Scraped data was placed into a Python dictionary called mars_info.

**FLASK APP**

* Using Flask, render_template and PyMongo an app was created to hold the scraped data.
 A Flask app and route was set up to call the scrape function from the Python file and
 store that data in a Mongo database. A home route was also created to render the HTML
 template that will show the data on the web.
 
**WEB APP**

* Once the data is scraped and stored in the database, the app renders an HTML template,
 index.html.  The HTML uses a bootstrap css link and bootstrap JavaScript.  A button
 is created that will activate the scrape function so that the site will show updated
 information.  

 * Bootstrap grid layouts were used to show the latest Mars Mission news, the Mars featured
 planet image, the table of facts and the 4 hemisphere images and titles.

 ![site](https://github.com/Pip85/web-scraping-challenge/blob/main/Missions%20to%20Mars/Images/App%20Image%201%20-%20Large%20Screen.png)