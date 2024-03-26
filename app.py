from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import json
import requests

current_datetime = datetime.now()
date_str = current_datetime.strftime("%m-%d") 
filename = "taps/taps(%s).txt" %  date_str 
filename = os.path.join(filename)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_ids', methods=['POST'])
def update_ids():
    data = request.get_json()
    new_id = data.get('id').strip()

    # Here, you can open your .txt file and append the new ID
    

    with open(filename, 'a') as file:
        file.write(new_id + '\n')

    return 'ID updated successfully!'

@app.route('/get_line_count')
def get_line_count():
    line_count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
    except FileNotFoundError:
        pass

    return jsonify({'line_count': line_count})

@app.route('/get_guests')
def get_guests():
    # Example JSON data
    base_url = 'https://jmi2gxpho8.execute-api.us-east-1.amazonaws.com/abgtQuiz?event='
    today_date = datetime.today().date()
    date  = today_date.strftime('%Y-%m-%d')
    parameters = json.dumps({ "t": "get_specific_day", "date": date })
    
    new_url = base_url+parameters
    response = requests.get(new_url)
    today_guests = response.json()[date]

    return today_guests



if __name__ == '__main__':
    app.run(debug=True)