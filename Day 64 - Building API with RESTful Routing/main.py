from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from sqlalchemy.sql.expression import func


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'map_url': self.map_url,
            'img_url': self.img_url,
            'location': self.location,
            'has_sockets': self.has_sockets,
            'has_toilet': self.has_toilet,
            'has_wifi': self.has_wifi,
            'can_take_calls': self.can_take_calls,
            'seats': self.seats,
            'coffee_price': self.coffee_price,
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    random_cafe = Cafe.query.order_by(func.random()).first()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars()

    # Convert the result to a list of dictionaries
    cafes_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes_list)


@app.route('/search')
def get_cafes_at_location():
    location_param = request.args.get('loc')

    if location_param:
        cafes_at_location = Cafe.query.filter_by(location=location_param).all()

        # Convert the result to a list of dictionaries
        cafes_list = [cafe.to_dict() for cafe in cafes_at_location]

        if cafes_list:
            return jsonify(cafes_list)
        else:
            return jsonify({'error': {'Not Found': f'Sorry we don\'t have cafes at {location_param}'}})

    else:
        return jsonify({'error': 'Location parameter is missing'}), 400

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def create_cafe():
    if request.method == 'POST':
        data = request.json

        # Validate data (add more validation as needed)
        if 'name' not in data or 'map_url' not in data or 'img_url' not in data or 'location' not in data:
            return jsonify({'error': 'Incomplete data provided'}), 400

        # Create a new cafe
        new_cafe = Cafe(
            name=data['name'],
            map_url=data['map_url'],
            img_url=data['img_url'],
            location=data['location'],
            seats=data.get('seats', ''),
            has_toilet=data.get('has_toilet', False),
            has_wifi=data.get('has_wifi', False),
            has_sockets=data.get('has_sockets', False),
            can_take_calls=data.get('can_take_calls', False),
            coffee_price=data.get('coffee_price', '')
        )

        # Add the new cafe to the database
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify({'message': 'Cafe created successfully', 'cafe_id': new_cafe.id}), 201

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)

    if not cafe:
        return jsonify({'error': 'Cafe not found'}), 404

    data = request.json

    # Update the coffee_price if provided in the request
    if 'coffee_price' in data:
        cafe.coffee_price = data['coffee_price']

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': f'Coffee price for cafe {cafe_id} updated successfully'}), 200
    else:
        return jsonify({'error': 'No coffee_price provided in the request'}), 400


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    # Check if the API key is provided in the params
    api_key = request.args.get('api-key')

    # Check if the provided API key is valid
    if api_key != 'TopSecretAPIKey':
        return jsonify({'error': 'Invalid API key'}), 401

    cafe = Cafe.query.get(cafe_id)

    if not cafe:
        return jsonify({'error': 'Cafe not found'}), 404

    # Delete the cafe
    db.session.delete(cafe)
    db.session.commit()

    return jsonify({'message': f'Cafe {cafe_id} deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
