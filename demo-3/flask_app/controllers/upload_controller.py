from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
import os
import uuid
from flask_app.models.file import File

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]

@app.route("/upload")
def upload_file():
    if "user_id" not in session:
        return redirect("/user/create")
    return render_template("/pages/upload.html")

@app.route("/uploads/<filename>")
def serve_files(filename):
    return send_from_directory(app.config["UPLOAD_DIR"], filename)

@app.route("/upload", methods=["POST"])
def handle_file_upload():
    if "my_file" not in request.files:
        error_response = {
            "error": "File does not exist",
        }
        return error_response

    my_file = request.files["my_file"]
    extension = get_file_extension(my_file.filename)
    unique_filename = (uuid.uuid4().hex) + extension

    my_file.save(os.path.join(app.config["UPLOAD_DIR"], unique_filename))
    File.save({
        "file_name": unique_filename,
        "size": os.path.getsize(os.path.join(app.config["UPLOAD_DIR"], unique_filename)),
        "extension": extension,
        "anime_name" : request.form["anime_name"],
        "air_date" : request.form["air_date"],
        "studio" : request.form["studio"],
        "producer" : request.form["producer"],
        "episode_count" : request.form["episode_count"],
        "description" : request.form["description"],
    })

    print(my_file)
    data = {"success": "File has been successfully uploaded.",
        "file_path": f"/uploads/{unique_filename}"
        }
    print(data)
    return redirect("/upload")

