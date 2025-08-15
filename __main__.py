from flask import *
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

    voronoi_data = {
    "Tondo": {
        "Education": {
            "Manila High School": {
                "Contact Number": "(02) 8252 5836",
                "Address": "Narra St., Tondo, Manila",
                "Kind of School": "Public High School",
                "Coordinates": {
                    "Longitude": "120.9715",
                    "Latitude": "14.6223"
                }
            },
            "Tondo High School": {
                "Contact Number": "(02) 8252 5837",
                "Address": "Juan Luna St., Tondo, Manila",
                "Kind of School": "Public High School",
                "Coordinates": {
                    "Longitude": "120.9748",
                    "Latitude": "14.6189"
                }
            },
            "St. Stephen's High School": {
                "Contact Number": "(02) 8252 5838",
                "Address": "Masangkay St., Tondo, Manila",
                "Kind of School": "Private High School",
                "Coordinates": {
                    "Longitude": "120.9687",
                    "Latitude": "14.6205"
                }
            },
        },
        "Hospitals": {
            "Tondo Medical Center": {
                "Address": "1388 Dagupan St., Tondo, Manila",
                "Contact Number": "(02) 8252 5831",
                "Coordinates": {
                    "Longitude": "120.9692",
                    "Latitude": "14.6178"
                }
            },
            "Mary Johnston Hospital": {
                "Address": "1221 Juan Nolasco St., Tondo, Manila",
                "Contact Number": "(02) 8252 5832",
                "Coordinates": {
                    "Longitude": "120.9734",
                    "Latitude": "14.6193"
                }
            },
            "Gat Andres Bonifacio Memorial Medical Center": {
                "Address": "1388 Samson Rd, Tondo, Manila",
                "Contact Number": "(02) 8252 5833",
                "Coordinates": {
                    "Longitude": "120.9756",
                    "Latitude": "14.6217"
                }
            },
            "Tondo General Hospital": {
                "Address": "San Pablo St., Tondo, Manila",
                "Contact Number": "(02) 8252 5834",
                "Coordinates": {
                    "Longitude": "120.9701",
                    "Latitude": "14.6232"
                }
            }
        },
        "Markets": {
            "Tondo Market": {
                "Address": "Recto Ave., Tondo, Manila",
                "Contact Number": "(02) 8252 5841",
                "Coordinates": {
                    "Longitude": "120.9723",
                    "Latitude": "14.6201"
                }
            },
            "Divisoria Market": {
                "Address": "Tutuban, Tondo, Manila",
                "Contact Number": "(02) 8252 5842",
                "Coordinates": {
                    "Longitude": "120.9765",
                    "Latitude": "14.6167"
                }
            }
        }
    }
}

    return render_template("03 map.html", data=voronoi_data)

@app.route("/suggestions")
def suggestions():
    print(location, industries)

    voronoi_data = {
    "Tondo": {
        "Education": {
            "Manila High School": {
                "Contact Number": "(02) 8252 5836",
                "Address": "Narra St., Tondo, Manila",
                "Kind of School": "Public High School",
                "Coordinates": {
                    "Longitude": "120.9715",
                    "Latitude": "14.6223"
                }
            },
            "Tondo High School": {
                "Contact Number": "(02) 8252 5837",
                "Address": "Juan Luna St., Tondo, Manila",
                "Kind of School": "Public High School",
                "Coordinates": {
                    "Longitude": "120.9748",
                    "Latitude": "14.6189"
                }
            },
            "St. Stephen's High School": {
                "Contact Number": "(02) 8252 5838",
                "Address": "Masangkay St., Tondo, Manila",
                "Kind of School": "Private High School",
                "Coordinates": {
                    "Longitude": "120.9687",
                    "Latitude": "14.6205"
                }
            }
        },
        "Hospitals": {
            "Tondo Medical Center": {
                "Address": "1388 Dagupan St., Tondo, Manila",
                "Contact Number": "(02) 8252 5831",
                "Coordinates": {
                    "Longitude": "120.9692",
                    "Latitude": "14.6178"
                }
            },
            "Mary Johnston Hospital": {
                "Address": "1221 Juan Nolasco St., Tondo, Manila",
                "Contact Number": "(02) 8252 5832",
                "Coordinates": {
                    "Longitude": "120.9734",
                    "Latitude": "14.6193"
                }
            },
            "Gat Andres Bonifacio Memorial Medical Center": {
                "Address": "1388 Samson Rd, Tondo, Manila",
                "Contact Number": "(02) 8252 5833",
                "Coordinates": {
                    "Longitude": "120.9756",
                    "Latitude": "14.6217"
                }
            },
            "Tondo General Hospital": {
                "Address": "San Pablo St., Tondo, Manila",
                "Contact Number": "(02) 8252 5834",
                "Coordinates": {
                    "Longitude": "120.9701",
                    "Latitude": "14.6232"
                }
            }
        },
        "Markets": {
            "Tondo Market": {
                "Address": "Recto Ave., Tondo, Manila",
                "Contact Number": "(02) 8252 5841",
                "Coordinates": {
                    "Longitude": "120.9723",
                    "Latitude": "14.6201"
                }
            },
            "Divisoria Market": {
                "Address": "Tutuban, Tondo, Manila",
                "Contact Number": "(02) 8252 5842",
                "Coordinates": {
                    "Longitude": "120.9765",
                    "Latitude": "14.6167"
                }
            }
        }
    }
}

    return render_template("04 suggestions.html", data=voronoi_data)



if __name__ == "__main__":
    print('HAH')
    app.run(debug=True)