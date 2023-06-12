from flask_jwt_extended import create_access_token, jwt_required
from flask import request, abort, jsonify
from flask_restful import Resource
from app import db

class Login(Resource):
    def post(self):
        # Proses validasi login
        # username = request.form['username']
        # password = request.form['password']
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        if username != 'admin' or password != 'password':
            abort(401, 'Invalid credentials')
        
        # Login berhasil, buat access token

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

class Protected(Resource):
    @jwt_required()
    def get(self):
        # Jika token valid, tampilkan response
        return jsonify({'hello': 'world'})