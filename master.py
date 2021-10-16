from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of ireland images
images = [
    "http://drive.google.com/uc?export=view&id=14_kMj43xi5YJpPbAaGeRgX9jI7b_btkC",
    "http://drive.google.com/uc?export=view&id=14_kMj43xi5YJpPbAaGeRgX9jI7b_btkC",
    "http://drive.google.com/uc?export=view&id=14_kMj43xi5YJpPbAaGeRgX9jI7b_btkC"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
