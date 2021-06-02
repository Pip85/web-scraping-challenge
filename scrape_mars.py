#!/usr/bin/env python
# coding: utf-8

# # Webscraping the following websites for news on upcoming mission to mars:
# https://redplanetscience.com/
# https://spaceimages-mars.com
# https://galaxyfacts-mars.com
# https://marshemispheres.com/

# In[15]:


# Import modules for use in webscraping:
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[16]:


# Setup for working with Browser:

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## Latest News - Mars Mission

# In[17]:


# URL for news on Mars Mission
rps_url = "https://redplanetscience.com/"

# Use Browser to pull html data and use beautiful soup to parse the data
browser.visit(rps_url)
rps_html = browser.html
rps_soup = bs(rps_html, "html.parser")


# In[18]:


# Search parsed soup file for latest news title and snippet
news_title = rps_soup.find("div", class_="content_title").text
news_teaser = rps_soup.find("div", class_ = "article_teaser_body").text
print(news_title)
print(news_teaser)


# ## Capture Mars image

# In[19]:


# URL for JPL site housing image of Mars
jpl_url = "https://spaceimages-mars.com/"

# Use Browser to pull html data and use beautiful soup to parse the data
browser.visit(jpl_url)
jpl_html = browser.html
jpl_soup = bs(jpl_html, "html.parser")


# In[20]:


# Search parsed soup file for html containing Mars image
jpl_find_img = jpl_soup.find_all("img", "headerimage")

# Loop through header data to find the url link of of the image
for img in jpl_find_img:
    jpl_img = img["src"]

# Establish variable to hold the image url    
featured_image_url = jpl_url + jpl_img
print(featured_image_url) 


# ## Mars Facts

# In[21]:


# URL for facts about Mars
facts_url = "https://galaxyfacts-mars.com"

# Read html from url into variable
facts_table = pd.read_html(facts_url)


# In[22]:


# Create data frame from html data
facts_df = facts_table[0]

# Create html file from dataframe:
facts_df.to_html("facts_html", index=False)


# ## Mars Hemispheres

# In[23]:


# URL for images of Mars hemispheres
hem_url = "https://marshemispheres.com/"

# Use Browser to pull html data and use beautiful soup to parse the data
browser.visit(hem_url)
hem_html = browser.html
hem_soup = bs(hem_html, "html.parser")


# In[24]:


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
 
print(hemisphere_image_urls)


# In[25]:


browser.quit()

