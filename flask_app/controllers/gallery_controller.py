from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
from flask_app.models.file import File
import os
import uuid

@app.route("/browse/<int:page>")
def browse(page):
    user_files = File.get_all(page)
    x = 0
    plus = x +1
    return render_template("/pages/browse.html", files = user_files , x = x, plus = plus)

@app.route("/main/<int:id>")
def main_page(id):
    user_files = File.get_one(id)
    x = 0
    
    return render_template("/pages/anime.html", files = user_files , x = x, )