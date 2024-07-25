from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()
app.config["ENVIRONMENT"] = os.getenv("ENVIRONMENT")
app.config["PORT"] = os.getenv("PORT")


@app.route("/")
def index():
    environment = app.config["ENVIRONMENT"]
    return render_template("index.html", environment=environment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])
