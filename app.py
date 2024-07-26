from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()
app.config["ENVIRONMENT"] = os.getenv("ENVIRONMENT")
app.config["PORT"] = os.getenv("SERVER_PORT")
print(app.config["ENVIRONMENT"])


@app.route("/")
def index():
    environment = app.config["ENVIRONMENT"]
    return render_template("index.html", environment=environment)


if __name__ == "__main__":
    port = app.config["PORT"]
    app.run(host="0.0.0.0", port=port)
