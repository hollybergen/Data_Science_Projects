# import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)


# create route that renders index.html template and finds documents from mongo
@app.route("/")

def home():

    # Find data
    try:
        mars = list(mongo.db.collection.find())[-1]
    except:
        mars = {}

    # return template and data
    return render_template("index.html", mars=mars)


# Route that will trigger scrape functions
@app.route("/scrape")

def scraper():

    # Run scraped functions
    mars = scrape_mars.scraper()

    # Store results into dictionary
    mars_dict = {
        "latest_news": mars["latest_news"],
        "latest_paragraph": mars["latest_paragraph"],
        "featured_image_url": mars["featured_image_url"],
        "mars_weather": mars["mars_weather"],
        "mars_table": mars["mars_table"],
        "hemi_dicts": mars["hemi_dicts"]
    }

    # Insert mars_dict into database
    mongo.db.collection.insert_one(mars_dict)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)