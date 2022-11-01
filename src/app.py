from flask import Flask,render_template, request
import http.client
import json

app = Flask(__name__)

api_key = "apikey 02RHA8wnnQVsxP30FmWp4F:1Y8mzAE69JWA0DAtX0xJoL"



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


    return data["result"]["gasoline"]



@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")



@app.route("/calc",methods=["POST"])
def calc():
    kml = request.form.get("kml")
    dist = request.form.get("dist")
    print(kml,dist)

    gasolina = float(api())* 5
    calculo = float(dist) / float(kml)

    resultado = calculo * gasolina

    print(resultado)

    return render_template("calc.html",resultado=resultado)