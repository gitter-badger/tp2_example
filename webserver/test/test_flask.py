import http.client
import urllib
import pytest

def test_start_match():
    conn = http.client.HTTPConnection('localhost',5000)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    params = urllib.parse.urlencode( {
        "team1":1,
        "team2":2,
        "place":"LP"
    })
    conn.request("GET", "/start_match", params, headers)
    response = conn.getresponse()
    conn.close()
    assert response.status == 200

def test_stop_match():
    conn = http.client.HTTPConnection('localhost',5000)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request("GET", "/stop_match", headers=headers)
    response = conn.getresponse()
    conn.close()
    assert response.status == 200