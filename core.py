from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'  # SQLite database file
db = SQLAlchemy(app)


class DummyObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age


def create_dummy_objects():
    dummy_data = [
        {"name": "John", "age": 25},
        {"name": "Jane", "age": 30},
        {"name": "Bame", "age": 45},
        {"name": "Aj", "age": 21},
        {"name": "Danny", "age": 35},
        {"name": "Doe", "age": 40},
        {"name": "Max", "age": 24},
        {"name": "Havier", "age": 30},
        {"name": "Arthur", "age": 20},
        {"name": "Morgan", "age": 31},
        {"name": "Maz", "age": 25},
        {"name": "Archie", "age": 30},
        {"name": "Jay", "age": 25},
        {"name": "Shawn", "age": 30},
        {"name": "Lenny", "age": 25},
        {"name": "Braawk", "age": 30},
        {"name": "John", "age": 15},
        {"name": "Javi", "age": 71},
        {"name": "John", "age": 51},
        {"name": "Jane", "age": 37},
        {"name": "John", "age": 41},
        {"name": "Jane", "age": 18},
        {"name": "Clarke", "age": 17},
        {"name": "Bruce", "age": 73},
        {"name": "Bane", "age": 25},
        {"name": "Jane", "age": 30},
    ]

    for data in dummy_data:
        dummy_object = DummyObject(name=data["name"], age=data["age"])
        db.session.add(dummy_object)

    db.session.commit()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api/data')
def get_all_data():
    dummy_objects = DummyObject.query.all()
    data = [{'id': obj.id, 'name': obj.name, 'age': obj.age} for obj in dummy_objects]
    return jsonify(data)


@app.route('/api/data/<int:dummy_id>')
def get_data(dummy_id):
    dummy_object = DummyObject.query.get(dummy_id)
    if dummy_object is None:
        return jsonify({'error': 'Invalid dummy ID'})
    data = {'id': dummy_object.id, 'name': dummy_object.name, 'age': dummy_object.age}
    return jsonify(data)

with app.app_context():
        db.create_all()
        create_dummy_objects()

if __name__ == '__main__':
    app.run(debug=True)
