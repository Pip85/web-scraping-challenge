# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of flask app
app = Flask(__name__)

# setup mongo connection
mars_db = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Create mongo db and collection
# mars_db = client.mars_app
# data = mars_db.data

# Setup home route and render index.html file from mongo db
@app.route("/")
def home():
    mars_data = mars_db.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

# Setup route to call scraped data
@app.route("/scrape")
def scraped_info():
    mars_data = mars_db.db.mars_data
    mars_info = scrape_mars.scrape()
    mars_data.update({}, mars_info, upsert=True)
    return redirect("/")


if __name__== "__main__":
    app.run(debug=True)

