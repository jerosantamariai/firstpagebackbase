from flask import Flask, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models import db
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app = Flask(__name__)
app.config['DEBUG '] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

Migrate(app, db)
CORS(app)
bcrypt = Bcrypt(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route("/")
def root():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
@app.route('/test/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# @jwt_required
def users(id = None):
    if request.method == 'GET':
        return jsonify({"msg": "usuario get"}), 200
    if request.method == 'POST':
        return jsonify({"msg": "users post"}), 200
    if request.method == 'PUT':
        return jsonify({"msg": "users put"}), 200
    if request.method == 'DELETE':
        return jsonify({"msg": "users delete"}), 200

if __name__ == '__main__':
    manager.run()



# ***** BASE ROUTE *****

# @app.route('/test', methods=['GET', 'POST'])
# @app.route('/test/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# @jwt_required # llamando a jwt_required le indico q las rutas abajo son privadas y requiere autorización pra acceder
# def users(id = None):
#     if request.method == 'GET':
#         return jsonify({"msg": "usuario get"}), 200
#     if request.method == 'POST':
#         return jsonify({"msg": "users post"}), 200
#     if request.method == 'PUT':
#         return jsonify({"msg": "users put"}), 200
#     if request.method == 'DELETE':
#         return jsonify({"msg": "users delete"}), 200