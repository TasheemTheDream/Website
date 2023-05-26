from flask_app import app
import flask_app.controllers.index_controller
import flask_app.controllers.auth_controller
import flask_app.controllers.upload_controller
import flask_app.controllers.gallery_controller
import flask_app.controllers.login

if __name__ == "__main__":
    app.run(debug=True)
