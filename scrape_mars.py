#!/usr/bin/env python
# coding: utf-8

# # Webscraping the following websites for news on upcoming mission to mars:
# https://redplanetscience.com/
# https://spaceimages-mars.com
# https://galaxyfacts-mars.com
# https://marshemispheres.com/

# Import modules for use in webscraping:
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Setup for working with Browser:
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ## Latest News - Mars Mission

    # URL for news on Mars Mission
    rps_url = "https://redplanetscience.com/"

    # Use Browser to pull html data and use beautiful soup to parse the data
    browser.visit(rps_url)
    rps_html = browser.html
    rps_soup = bs(rps_html, "html.parser")

    # Search parsed soup file for latest news title and snippet
    news_title = rps_soup.find("div", class_="content_title").text
    news_teaser = rps_soup.find("div", class_ = "article_teaser_body").text

    # ## Capture Mars image

    # URL for JPL site housing image of Mars
    jpl_url = "https://spaceimages-mars.com/"

    # Use Browser to pull html data and use beautiful soup to parse the data
    browser.visit(jpl_url)
    jpl_html = browser.html
    jpl_soup = bs(jpl_html, "html.parser")

    # Search parsed soup file for html containing Mars Featured Image
    jpl_find = jpl_soup.find_all("div", class_="floating_text_area")

    # Find image url within jpl_find
    for item in jpl_find:
        a = item.find("a")  
        href = a["href"]
        
    # Establish variable to hold the image url        
    featured_image_url = jpl_url + href
    
    # ## Mars Facts

    # URL for facts about Mars
    facts_url = "https://galaxyfacts-mars.com"

    # Read html from url into variable
    table = pd.read_html(facts_url)

    # Create data frame from html data
    facts_df = table[0]

    # Convert first row to column headers
    header_row = 0
    facts_df.columns = facts_df.iloc[header_row]
    facts_df = facts_df.drop(header_row)

    # Rename first column
    facts_df=facts_df.rename(columns = {'Mars - Earth Comparison':'Description'})

    # Set index to first column
    facts_df.set_index("Description", inplace = True)

    # TODO - Correct in JN from line 
    # Convert dataframe to html
    facts_table = facts_df.to_html(
        table_id="facts_table", 
        justify="center",
        classes="table table-striped table-bordered border border-dark")

    # Remove new line code from table
    facts_table = facts_table.replace("\n", " ")

    # Create html file from dataframe:
    facts_df.to_html("facts_html", index=False)

    # ## Mars Hemispheres

    # URL for images of Mars hemispheres
    hem_url = "https://marshemispheres.com/"

    # Use Browser to pull html data and use beautiful soup to parse the data
    browser.visit(hem_url)
    hem_html = browser.html
    hem_soup = bs(hem_html, "html.parser")

    # Search soup file for section containing hemisphere titles and html's for images
    hem_find = hem_soup.find_all("div", class_ = "item")

    # Setup for loop to pull the hemisphere titles from H3 header data
    # For loop pulls html links for each hemisphere's page
    # Image link from each hemisphere page is pulled
    # Hemisphere title and image url are stored in a dictionary
    hemisphere_image_urls = []

    for item in hem_find:
        title = item.find("h3").text
        link = item.find("a", class_ = "itemLink")["href"]
        hemi_url = hem_url + link
        browser.visit(hemi_url)
        hemi_url_html = browser.html
        hemi_soup = bs(hemi_url_html, "html.parser")
        img = hem_url + hemi_soup.find("img", class_ = "wide-image")["src"]
        hemisphere_image_urls.append({"img_url": img, "title": title})

        mars_info = {
                    "news_title": news_title,
                    "news_teaser": news_teaser,
                    "mars_image": featured_image_url,
                    "mars_facts": facts_table,
                    "mars_hemispheres": hemisphere_image_urls
                     }
    browser.quit()

    return mars_info

