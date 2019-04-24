#!/usr/bin/env python
# coding: utf-8
# FLASK_APP=app.py flask run

# Dependencies
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
from IPython.display import Image
from IPython.core.display import HTML, Image, display


def scraper():

    # Create beautiful soup object from html, create a function
    def scrape(url):
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    # Create dictionary to store variables
    mars = {}
    
    # Mars News #
    #------------------------------------------------#   
    
    # Save URL, use scrape function created and save as variable name
    url_news = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    soup = scrape(url_news)

    # Collect latest news title & paragraph text
    latest_news = soup.find("ul", class_="item_list").find("div",class_ = "content_title").a.text
    latest_paragraph = soup.find("ul", class_="item_list").find("div",class_ = "article_teaser_body").text
    
    # Append to dictionary
    mars["latest_news"] = latest_news
    mars["latest_paragraph"] = latest_paragraph


    # Mars Image #
    #------------------------------------------------#
    
    # Save urls as variables
    url_base = "https://www.jpl.nasa.gov"
    url_featured = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Use function created to scrape site and find targets of scraped object
    image_soup = scrape(url_featured)
    image_url = image_soup.find("div", class_="carousel_container").find("article", class_="carousel_item").find('a')['data-fancybox-href']

    # Image url output is only the path after "url", so must append to base url
    # example: /spaceimages/images/mediumsize/PIA09113_ip.jpg
    featured_image_url = f'{url_base}{image_url}'
    
    # Append to dictionary
    mars["featured_image_url"] = featured_image_url

    

    # Mars Weather #
    #------------------------------------------------#

    # Save urls as variable
    url_twitter = "https://twitter.com/marswxreport?lang=en"

    # Use function created to scrape site and find targets of scraped object
    twitter_soup = scrape(url_twitter)

    # Use soup object to locate the most recent tweet with the weather
    mars_weather = (twitter_soup.find("div", class_="js-tweet-text-container").find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text)
    
    # Append to dictionary
    mars["mars_weather"] = mars_weather
    


    # Mars Facts #
    #------------------------------------------------#

    # Save url as variable
    fact_url = "https://space-facts.com/mars/"

    # Use function created to scrape site and find targets of scraped object
    fact_soup = scrape(fact_url)

    # Create table as beautiful soup object 
    table = fact_soup.find("table").find("tbody").find_all("tr")

    # Another option: pandas df using pd.read_html which automatically finds tables and converts to df
    mars_df = pd.read_html(fact_url)
    mars_facts_df = pd.DataFrame(mars_df[0])

    # Name columns and set index
    mars_facts_df.columns = ['Parameter','Data']
    mars_df_table = mars_facts_df.set_index("Parameter")
    mars_df_table

    # Convert the pd df to HTML table and clean up. 
    mars_html_table = mars_df_table.to_html(classes='marsdata')
    mars_table = mars_html_table.replace('\n', ' ')

    # Append to dictionary
    mars["mars_table"] = mars_table
        


    # Mars Hemispheres #
    #------------------------------------------------#

    # Save url as variable
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Use function created to scrape site and find targets of scraped object
    hemi_soup = scrape(hemi_url)

    # Establish base url to prefix to links
    base_url = "https://astrogeology.usgs.gov"

    # Create object from 
    item = hemi_soup.find_all("div", class_="item")

    # Create list to append urls
    hemi_dicts = []

    # Loop through object, find link, append to list, add base url, and grab title
    for i in item:
        link = i.find(class_="description").a["href"]
        full_url = (base_url + link)
        scraped = scrape(full_url)
        img_url = scraped.find("div", class_="downloads").find("li").a["href"]
        title = (i.find(class_="description").h3.text).replace(" Enhanced", "")
        hemi_dicts.append({"title": title, "img_url":img_url})

        
    # Append to dictionary
    mars["hemi_dicts"] = hemi_dicts
    
    # Return results
    return mars

    # Quit browser
    browser.quit()


