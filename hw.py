
from flask import Flask
from flask import jsonify
import records
app = Flask(__name__)

db = records.Database("postgres://localhost/clemson_stats_db")

@app.route("/")
def get_rows():
    rows = db.query("SELECT * FROM clemson_stats_db;")
    return jsonify(rows.export('json'))
