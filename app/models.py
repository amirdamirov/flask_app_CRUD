from db_setup.db_conf import db

class Todo(db.Model):
    __tablename__ = "todolist"

    id = db.Column(db.Integer(),autoincrement=True, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    