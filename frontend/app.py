from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

#MAIN PAGE AND FORMS

@app.route('/')
def index():

    try:
        response = requests.get('http://flask-app-otel-backend-svc:5001/read')
        response.close()
        cities = response.json()
        
        if response.status_code == 200:
            return render_template('index.html', cities=cities)
        else:
            return render_template('index.html')

    except requests.exceptions.RequestException as e:
        return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit', methods=['POST'])
def edit():
    id = request.form.get('id')
    data = {"id": id}
    data_json = json.dumps(data)
    payload = {'json_payload': data_json}

    response = requests.get('http://flask-app-otel-backend-svc:5001/read_one', json=payload)
    if response.status_code == 200:
        return render_template('edit.html', city=response.json())
    else:
        return render_template('failure.html')

#SUCCESS AND FAILURE PAGES

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

#ROUTES TO SEND REQUESTS TO BACKEND

@app.route('/create', methods=['POST'])
def create():

    #getting some values from the form
    city = request.form.get("city")
    country = request.form.get('country')
    visit_date = request.form.get('visit_date')
    transport = request.form.get('transport')

    data = {"city": city, "country": country, "visit_date": visit_date, "transport": transport}
    data_json = json.dumps(data)
    payload = {'json_payload': data_json}

    response = requests.post('http://flask-app-otel-backend-svc:5001/create', json=payload)
    response.close()

    if response.status_code == 200:
        return redirect(url_for('success')) 
    else:
        return redirect(url_for('failure')) 

@app.route('/update', methods=['POST'])
def update():

    id = request.form.get("id")
    city = request.form.get("city")
    country = request.form.get('country')
    visit_date = request.form.get('visit_date')
    transport = request.form.get('transport')

    data = {"id": id, "city": city, "country": country, "visit_date": visit_date, "transport": transport}
    data_json = json.dumps(data)
    payload = {'json_payload': data_json}

    response = requests.put('http://flask-app-otel-backend-svc:5001/update', json=payload)
    response.close()

    if response.status_code == 200:
        return redirect(url_for('success')) 
    else:
        return redirect(url_for('failure')) 

@app.route('/delete', methods=['POST'])
def delete():

    id = request.form.get("id")

    data = {"id": id}
    data_json = json.dumps(data)
    payload = {'json_payload': data_json}

    response = requests.delete('http://flask-app-otel-backend-svc:5001/delete', json=payload)
    response.close()

    if response.status_code == 200:
        return redirect(url_for('success')) 
    else:
        return redirect(url_for('failure')) 

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=5000, threaded=True)