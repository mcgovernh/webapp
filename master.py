from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of ireland images
images = [
    './drive/MyDrive/imagesofireland/cliffsofmoher.jpg',
    './drive/MyDrive/imagesofireland/DesertedVillage.jpg',
    './drive/MyDrive/imagesofireland/AirCorp.jpg',
    './drive/MyDrive/imagesofireland/Derrynane.jpg',
     './drive/MyDrive/imagesofireland/Blaskets.jpg',
     './drive/MyDrive/imagesofireland/BrazenHeadDublin.jpg',
     './drive/MyDrive/imagesofireland/cashel.jpg',
     './drive/MyDrive/imagesofireland/dublincastle.jpg',
     './drive/MyDrive/imagesofireland/castle.jpg'
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
