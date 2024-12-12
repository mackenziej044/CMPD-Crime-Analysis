# import flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure the database
app.config

# define endpoints
@app.route('/data')
def get_data():
    data = {'file_name': 'cmpd_data.db'} 
    return jsonify(data)

# run server
if __name__ == '__main__':
    app.run(debug=True)