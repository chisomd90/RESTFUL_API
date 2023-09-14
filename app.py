from flask import Flask, request, jsonify
from model import db, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

# Create a new person by name
@app.route('/api/<string:name>', methods=['POST'])
def create_person_by_name(name):
    data = request.json
    new_person = Person(name=name, age=data['age'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

# Retrieve details of a person by name
@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        return jsonify({'name': person.name, 'age': person.age})
    return jsonify({'message': 'Person not found'}), 404

# Update details of a person by name
@app.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        data = request.json
        person.age = data['age']
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})
    return jsonify({'message': 'Person not found'}), 404

# Delete a person by name
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})
    return jsonify({'message': 'Person not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
