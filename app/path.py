from app import api
from .todo import *
from .auth import *

def TODO_API_PATH():
    api.add_resource(HelloWorld, "/hellowords")
    api.add_resource(HelloName, "/hellowords_name/<int:id_name>", methods=["GET", "DELETE", "PUT"])
    api.add_resource(HelloName, "/hellowords_name/<int:id_name>", endpoint="helloname.post", methods=["POST"])

def AUTH_API_PATH():
    api.add_resource(Login, "/login")
    api.add_resource(Protected, "/protected")
