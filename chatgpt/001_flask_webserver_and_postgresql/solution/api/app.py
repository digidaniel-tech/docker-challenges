import models.userModel as userModel
import controllers.userController as userController

from flask import Flask, request
from flask_restful import marshal_with
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
  app = Flask(__name__)

  # This is needed when running behind a reverse proxy
  app.wsgi_app = ProxyFix(
      app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
  )

  @app.route("/users", methods=["GET"])
  @marshal_with(userModel.user_fields)
  def get_users():
    return userController.getAllUsers()

  @app.route("/users", methods=["POST"])
  @marshal_with(userModel.user_fields)
  def addUser():
    content=request.get_json()
    user = userModel.User(
      name=content['name'],
      email=content['email']
    )

    return userController.addUser(user)

  return app

app = create_app()
