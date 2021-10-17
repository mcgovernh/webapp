from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of ireland images
images = [
    "https://assets-eu-01.kc-usercontent.com/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/2c9a48c5-0768-4bb8-ae6c-02f205de02f3/header-dogs-bay-beach-connemara-galway.jpg?w=756&amp;q=66&amp;h=716&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/2c9a48c5-0768-4bb8-ae6c-02f205de02f3/header-dogs-bay-beach-connemara-galway.jpg?w=756&amp;q=66&amp;h=716&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/2c9a48c5-0768-4bb8-ae6c-02f205de02f3/header-dogs-bay-beach-connemara-galway.jpg?w=756&amp;q=66&amp;h=716&amp;fit=crop&amp;fm=webp"

]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
