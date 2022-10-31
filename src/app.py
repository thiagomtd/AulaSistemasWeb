from flask import Flask,render_template, request
import http.client
import json

app = Flask(__name__)

api_key = "apikey 02RHA8wnnQVsxP30FmWp4F:1Y8mzAE69JWA0DAtX0xJoL"
@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("calculo")
def calc():
    kml = request.form.get("kml") #10 km
    dist = request.form.get("dist") #20 km 
    gasolina = api() * 5
    calculo = dist / kml
    resultado = calculo * gasolina
    

    
    return render_template("index.html", resultado=resultado)

def api():
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

    return data["gasoline"]
