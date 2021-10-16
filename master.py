from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://drive.google.com/file/d/14_kMj43xi5YJpPbAaGeRgX9jI7b_btkC/view?usp=sharing",
    "https://drive.google.com/file/d/1XIiMMtESAUhXVmBvqMjs4jt8HEe7H7MX/view?usp=sharing",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
