# import flask
from flask import Flask, jsonify

app = Flask(__name__)

# define endpoints
@app.route('/data')
def get_data():
    data = ('cmpd_data.db')
    return jsonify(data)

# run server
if __name__ == '__main__':
    app.run(debug=True)