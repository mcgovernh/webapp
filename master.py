from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of ireland images
images = [
    "https://assets-eu-01.kc-usercontent.com/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/2c9a48c5-0768-4bb8-ae6c-02f205de02f3/header-dogs-bay-beach-connemara-galway.jpg?w=756&amp;q=66&amp;h=716&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com:443/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/32165516-3fca-4baa-b5da-9dad8d227888/header-wild-nephin-ballycroy-national-park-mayo.jpg?w=756&amp;q=66&amp;h=448&amp;fit=crop&amp;fm=webp".
    "https://assets-eu-01.kc-usercontent.com:443/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/e3a89dbf-96e2-4be8-b098-cd94bfb557e4/header-hiking-croagh-patrick-mayo%20copy.jpg?w=756&amp;q=66&amp;h=616&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com:443/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/9edcbd74-6172-4e67-817d-7146fc1ace16/header-cork-city-cork.jpg?w=1152&amp;q=66&amp;h=624&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com:443/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/3424d425-c34b-4e9a-8838-ae4246f278cb/header-sliabh-league-donegal%20walk.jpg?w=756&amp;q=66&amp;h=560&amp;fit=crop&amp;fm=webp",
    "https://assets-eu-01.kc-usercontent.com:443/aa24ba70-9a12-01ae-259b-7ef588a0b2ef/d2dda78f-e984-4928-8392-aa9630068199/header-kylemore-abbey-galway.jpg?w=756&amp;q=66&amp;h=560&amp;fit=crop&amp;fm=webp"

]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
