from flask import Flask,jsonify,request
from database import fetch_jobs
app = Flask(__name__)

@app.get('/benz')
def fetch_benz():
    return jsonify(fetch_jobs('Benz'))

@app.get('/Airbnb')
def fetch_airbnb():
    return jsonify(fetch_jobs('Airbnb'))
@app.get('/')
def hello():
    return jsonify(fetch_jobs(''))

@app.get('/intern')
def fetch_intern():
    return jsonify(fetch_jobs('Intern'))
@app.get('/FullTime')
def fetch_fullTime():
    return jsonify(fetch_jobs('FullTime'))


@app.route('/about')
def about():
    return 'This is the About page!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
