from flask import Flask
import os


app = Flask(__name__)
app.secret_key="secret"

app.config["UPLOAD_DIR"] = os.path.join(app.instance_path, "uploads")

# Create the upload directory if it doesn't exist
if not os.path.exists(app.config["UPLOAD_DIR"]):
    os.makedirs(app.config["UPLOAD_DIR"])