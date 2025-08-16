from flask import *

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

import json
import pandas as pd
from math import radians, cos

def suggest_locations(lamudi_file_path):
    """Process property data from Lamudi Excel file"""
    try:
        lamudi_df = pd.read_excel(lamudi_file_path)
        print(f"Loaded {len(lamudi_df)} properties")
    except Exception as e:
        return {"error": f"Failed to load Lamudi data: {str(e)}"}
    
    results = []
    for idx, row in lamudi_df.iterrows():
        try:
            results.append({
                "name": str(row['name']),  # Directly use the name column
                "area_in_sqm": f"{int(row['sqm'])} sqm",
                "price": f"₱{int(row['price']):,}/month",
                "coordinates": {
                    "lat": float(row['latitude']),
                    "lng": float(row['longitude'])
                }
            })
        except Exception as e:
            print(f"Skipping row {idx}: {str(e)}")
            continue
    
    # Calculate highlights
    highlights = {
        "cheapest": "N/A",
        "biggest": "N/A",
        "most_cost_effective": "N/A"
    }
    
    if results:
        try:
            # Add temporary numerical fields
            for loc in results:
                loc['_price'] = float(loc['price'][1:].replace(',', '').replace('/month', ''))
                loc['_area'] = float(loc['area_in_sqm'].replace(' sqm', ''))
                loc['_value'] = loc['_price'] / loc['_area']
            
            highlights = {
                "cheapest": min(results, key=lambda x: x['_price'])['name'],
                "biggest": max(results, key=lambda x: x['_area'])['name'],
                "most_cost_effective": min(results, key=lambda x: x['_value'])['name']
            }
            
            # Remove temporary fields
            for loc in results:
                loc.pop('_price', None)
                loc.pop('_area', None)
                loc.pop('_value', None)
        except Exception as e:
            print(f"Highlight calculation error: {str(e)}")
    
    return {
        "properties": results,
        "highlights": highlights
    }


###
###
###
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
    voronoi_data = get_location_data({"location":location, "industries":industries})
    input = {"location":location, "industries":industries}
    return render_template("03 map.html", data=voronoi_data, input=input)

@app.route("/suggestions/<location>/<industries>")
def suggestions(location, industries):
    input = {"location":location, "industries":industries}
    voronoi_data = get_location_data({"location":location, "industries":industries})
    suggestions = suggest_locations('lamudi.xlsx')
    print(suggestions)
    return render_template("04 suggestions.html", input=input, suggestions=suggestions, data=voronoi_data)



if __name__ == "__main__":
    print('HAH')
    app.run(debug=True)