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
    return render_template("03 map.html")

if __name__ == "__main__":
    print('HAH')
    app.run(debug=True)