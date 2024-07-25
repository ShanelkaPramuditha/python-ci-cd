from flask import Flask, render_template
from dotenv import load_dotenv
import os

env = os.getenv("MODE", "development")
if env == "production":
    load_dotenv(".env")
else:
    load_dotenv(".env.dev")


app = Flask(__name__)

app.config["ENVIRONMENT"] = os.getenv("ENVIRONMENT")


@app.route("/")
def index():
    environment = app.config["ENVIRONMENT"]
    return render_template("index.html", environment=environment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
