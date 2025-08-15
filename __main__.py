from flask import *

import requests
import json
from typing import Dict, List
import ast

def get_location_data(user_input):
    # Load the JSON data
    with open('Data-Data.json', 'r') as file:
        data = json.load(file)
    
    # Extract input parameters
    location = user_input['location']
    industries = ast.literal_eval(user_input['industries']) if isinstance(user_input['industries'], str) else user_input['industries']
    
    # Initialize result structure
    result = {location: {}}
    
    # Return empty dict if location doesn't exist
    if location not in data:
        return result
    
    # Filter industries
    for industry in industries:
        if industry in data[location]:
            result[location][industry] = data[location][industry]
    
    return result

print('HAH')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("01 index.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/user_input", methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        location = request.form.get('location')
        industries = request.form.get('industry', '')
        # Process industries into list (remove empty strings)
        industry_list = [industry for industry in industries.split(',') if industry]
        
        # Now you can use the data
        return redirect(url_for('map', location=location, industries=industry_list))
    return render_template("02 dropdown.html")

@app.route("/map/<location>/<industries>")
def map(location, industries):
    print(location, industries)

    voronoi_data = get_location_data({"location":location, "industries":industries})
    print(voronoi_data)
    return render_template("03 map.html", data=voronoi_data)

@app.route("/suggestions")
def suggestions():
    
    return render_template("04 suggestions.html", data=voronoi_data)



if __name__ == "__main__":
    print('HAH')
    app.run(debug=True)