import os
import signal
import subprocess
from database import Database

class Process(object):
    list_process = []
    
    def start_process(self, d_m, id_match):        
        process_match = { 'id_match': id_match, 'pid': '' }
        cmd = "python3 process.py %s %s %s" % (d_m["team1"], d_m["team2"], id_match)        
        process = subprocess.Popen(cmd.split(), preexec_fn=os.setsid)
        process_match['pid'] = process.pid
        self.list_process.append(process_match)
        return str(200)

    def stop_process(self, id_match):
        process_match = None
        process_match = next((item for item in self.list_process if (str(item["id_match"]) == str(id_match))), None)

        if process_match != None:        
            db = Database()
            db.get_session().close()
            os.killpg(os.getpgid(process_match['pid']), signal.SIGTERM)
            self.list_process.remove(process_match)
            return str(200)
        return str(500)