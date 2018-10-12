from flask import Flask, jsonify, request
from models.role import RoleModel
from models.user import UserModel
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:system@localhost/postgres'

app.secret_key = 'Gurpreet'

jwt = JWT(app, authenticate, identity)


@app.route('/get_roles')
@jwt_required()
def get_roles():
    roles = RoleModel.read_roles()
    return jsonify({'roles': [role.json() for role in roles]}), 200


@app.route('/get_users')
@jwt_required()
def get_users():
    logged_in_user = current_identity
    if logged_in_user.role_id == 1:
        users = UserModel.get_users()
        return jsonify({'users': [user.json() for user in users]}), 200


@app.route('/add_user', methods=['POST'])
@jwt_required()
def add_user():
    logged_in_user = current_identity
    data = request.get_json()
    user = UserModel(data['username'], data['password'], data['name'], data['role_id'])
    user.add_user()

    return "User add successfully", 200


@app.route('/delete_user', methods=['POST'])
@jwt_required()
def delete_user():
    data = request.get_json()
    UserModel.query.filter_by(id=data['user_id']).delete()
    db.session.commit()

    return "User deleted successfully", 200


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
