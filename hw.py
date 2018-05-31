
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
    sql = "SELECT * FROM clemson_stats_db;"
    jsonify(sql)
    return db.query(sql)
