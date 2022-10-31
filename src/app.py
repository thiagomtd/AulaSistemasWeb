from flask import Flask,render_template
import http.client
import json

app = Flask(__name__)

api_key = "apikey 02RHA8wnnQVsxP30FmWp4F:1Y8mzAE69JWA0DAtX0xJoL"
@app.route("/")
def index():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': api_key
        }

    conn.request("GET", "/gasPrice/fromCity?city=brazil", headers=headers)
    #    conn.request("GET", "/gasPrice/fromCity?city=brazil", headers=headers)


    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    return render_template("index.html",data=data)