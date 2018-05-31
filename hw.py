
from flask import Flask
import random
from flask import jsonify
import records
app = Flask(__name__)

db = records.Database("postgres://localhost/clemson_stats_db")

@app.route("/")
def hello():

    return jsonify("Hello!")

@app.route("/data")
def get_rows(db):
    rows = db.query("SELECT * FROM clemson_stats_db;")
    return rows
    print(rows.export('json'))
