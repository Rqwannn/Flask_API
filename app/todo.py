from flask import request, abort, jsonify
from flask_restful import Resource, reqparse, fields, marshal_with
from app import db
from app.TodoModel import TodoList

task_post_args = reqparse.RequestParser()

# task and summary must be the same of key objects todos
# use raw object if using reqparse
# use www-form-urlencode using request.form.get()

task_post_args.add_argument("name", type=str, required=True, help="Name is required")
task_post_args.add_argument("task", type=str, required=True, help="Task is required")
task_post_args.add_argument("summary", type=str, required=True, help="Summary is required")

task_put_args = reqparse.RequestParser()

task_put_args.add_argument("name", type=str)
task_put_args.add_argument("task", type=str)
task_put_args.add_argument("summary", type=str)

# fields digunakan untuk menentukan format atau struktur data yang akan dihasilkan oleh API
# marshal_with digunakan untuk mengubah objek Python ke format yang telah ditentukan dengan fields

resource_field = {
    "id": fields.Integer,
    "name": fields.String,
    "task": fields.String,
    "summary": fields.String
}

class HelloWorld(Resource):
    def get(self):
        todo =  TodoList.query.filter_by(name="Raqwan").first_or_404()
        return jsonify(todo)

class HelloName(Resource):
    @marshal_with(resource_field)
    def get(self, id_name):
        todo = TodoList.query.filter_by(id=id_name).first_or_404()
        return todo, 200
    
    @marshal_with(resource_field)
    def put(self, id_name):
        args = task_put_args.parse_args()
        todo = TodoList.query.filter_by(id=id_name).first()

        if not todo:
            abort(404, "Name Doesn`t Exist, Task Cannot Update")

        data = {
            "name": args["name"],
            "task": args["task"],
            "summary": args["summary"]
        }

        todo = TodoList(**data)
        db.session.commit()

        return todo, 200
    
    def delete(self, id_name):
        todo = TodoList.query.get_or_404(id_name)
        db.session.delete(todo)
        db.session.commit()

        status = {
            "Status": "Todo Delete"
        }

        return jsonify(status) # gunakan fungsi ini jika membuat object python, kalau langsung dari TodoList.query ndak usah
    
    @marshal_with(resource_field)
    def post(self, id_name):
        args = task_post_args.parse_args()
        todo =  TodoList.query.filter_by(id=id_name).first()

        if todo:
            abort(409, "Name ID already exists")

        data = {
            "id": id_name,
            "name": args["name"],
            "task": args["task"],
            "summary": args["summary"]
        }

        todo = TodoList(**data)
        db.session.add(todo)
        db.session.commit()

        return todo, 200
