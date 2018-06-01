
from flask import Flask
from flask import jsonify, make_response
import records
app = Flask(__name__)

db = records.Database("postgres://localhost/clemson_stats_db")

@app.route("/")
def get_rows():
    rows = db.query("SELECT * FROM clemson_stats_db;")
    resp = make_response(rows.export('json'), 200)
    resp.headers['content-type'] = "application/json"
    return resp
