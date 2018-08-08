# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from models import Team
from sqlalchemy.sql import select
import datetime
import os
  
app = Flask(__name__)
db = Database()
pro = Process()

# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    west = db.get_all_zone_teams(1)
    east = db.get_all_zone_teams(2)

    return render_template('index.html',east=east,west=west)

@app.route('/match', methods = ["POST"])
def start_match():
    data = request.form
    d_m = {}
    d_m["team1"] = data["eastern"]
    d_m["team2"] = data["western"]
    d_m["place"] = data["place"]
    if (data["place"] == ""):
        d_m["place"] = "NEUTRAL"    
    id_match = db.init_match(d_m)
    db.get_session().close()
    pro.start_process(d_m,id_match)
    return render_template('match.html', 
                           id_team_east=d_m["team1"], id_team_west=d_m["team2"], id_match=id_match)

@app.route('/match/stop/<id_match>', methods = ["GET"])
def stop_match(id_match):
    data = pro.stop_process(id_match)
    return jsonify({"status": data})
    
@app.route('/result/match/<id_match>', methods = ["GET"])
def get_result_match(id_match):
    result_match = db.get_result_match(id_match)
    return jsonify(result_match)  

@app.route('/match/<id_match>', methods = ["GET"])
def get_match(id_match):
    match = db.get_match(id_match);
    return jsonify(match)  

@app.route('/team/<id_team>', methods = ["GET"])
def get_team(id_team):
    team = db.get_team(id_team);
    return jsonify(team)  

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='0.0.0.0', port=8888)

