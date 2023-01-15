from flask import Flask, render_template, url_for, request, url_for, jsonify
import requests
import datetime
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    req = requests.get(
        'https://api.thingspeak.com/channels/1995263/feeds.json?api_key=KPAHRPU02P3AIXNW&results=2 ')
    state1 = req.json()["feeds"][-1]["field1"]
    if request.method == 'POST':
        if state1 == "1":
            return render_template("website.html", state=state1)
        elif state1 == "0":
            return render_template("website.html", state=state1)
    return render_template("website.html", state=state1)


@app.get("/update")
def update():
    req = requests.get(
        'https://api.thingspeak.com/channels/1995263/feeds.json?api_key=KPAHRPU02P3AIXNW&results=2 ')
    state1 = req.json()["feeds"][-1]["field1"]
    time1 = req.json()["feeds"][-1]["created_at"].split("T")
    time2 = time1[1].split(".")[0].split("Z")[0]
    time3 = time1[0]
    username = "admin"
    list = [time2, time3, username, state1]
    return list


if __name__ == "__main__":
    app.run(debug=True)
