from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)


api = Api(app)

CORS(app)

identity = {}

class ExampleResource(Resource):
    def get(self):
        # response = {"msg":"success GET response"}
        return identity
    
    def post(self):
        name = request.form["name"]
        age = request.form["age"]
        identity["name"] = name
        identity["age"] = age
        response = {"msg":"Data berhasil diinput","data":identity}
        return response

api.add_resource(ExampleResource, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)