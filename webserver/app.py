# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import render_template
from flask import request
from models import Team
import datetime
import os
  
app = Flask(__name__)
db = Database()
pro = Process()

# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/start_match', methods = ["GET"])
def start_match():
    data = request.form
    d_m = {}
    d_m["team1"] = data["team1"]
    d_m["team2"] = data["team2"]
    d_m["place"] = data["place"]
    id_match = db.init_match(d_m)
    print(pro.start_process(d_m,id_match))
    return "OK"

@app.route('/stop_match', methods = ["GET"])
def stop_match():
    pro.stop_process()
    return "OK"
    


if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=8888)
