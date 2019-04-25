# Mission to Mars #
A web application that scrapes various websites for data related to the Mission to Mars, stores scraped data in MongoDB, and displays the latest information in a single HTML page.

## Step 1 - Scraping ## 
[mission_to_mars.ipynb]( )(Jupyter Notebook file that outlines all the scraping) 

**Python libraries used:** BeautifulSoup, Pandas, and Splinter

* Scrape latest news title and paragraph text from the NASA Mars News Site.
* Scrape the image url for the current featured Mars Image from JPL Featured Space Image.
* Scrape the latest Mars weather tweet from the Mars Weather twitter account
* Scrape Mars metrics (e.g. diameter, mass) from the Mars Facts webpage.
* Scrape Mars hemispheres images and names from the USGS Astrogeology site.

## Step 2 - MongoDB and Flask Application ##

* [scrape_mars.py](https://github.com/hollybergen/Data_Science_Projects/blob/master/Mission%20to%20Mars%20-%20Web-Scraping%20%26%20Document%20Databases/scrape_mars.py) 
  * Declares a function called scrape that executes all the above scraping and returns the scraped data.
* [app.py](https://github.com/hollybergen/Data_Science_Projects/blob/master/Mission%20to%20Mars%20-%20Web-Scraping%20%26%20Document%20Databases/app.py) 
  * Creates an app route called /scrape that calls the scrape function and store data in Mongo database; creates a root route / that queries the Mongo database and pass the mars data into an HTML template to display the data.
* [index.html](https://github.com/hollybergen/Data_Science_Projects/blob/master/Mission%20to%20Mars%20-%20Web-Scraping%20%26%20Document%20Databases/templates/index.html) 
  * A template HTML file that display all data in the appropriate HTML elements.

## Webpage Screenshots ##
