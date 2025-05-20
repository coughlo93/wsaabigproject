from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin

# Initialize Flask app with static folder settings
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)  # enable CORS on all routes
app.config['CORS_HEADERS'] = 'Content-Type'

# Import the data access object for cars
from carDAO import carDAO

@app.route('/')
@cross_origin()
def index():
    # Serve the main page (Cars interface)
    return app.send_static_file('carviewer.html')

# Retrieve all cars
@app.route('/cars')
@cross_origin()
def getAll():
    results = carDAO.getAll()
    return jsonify(results)

# Find car by ID
@app.route('/cars/<int:id>')
@cross_origin()
def findById(id):
    car = carDAO.findByID(id)
    if not car:
        # If not found, return 404
        abort(404)
    return jsonify(car)

# Create a new car entry
@app.route('/cars', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)
    car = {
        "manufacturer": request.json.get("manufacturer"),
        "model": request.json.get("model"),
        "year": request.json.get("year")
    }
    # All fields must be present for creation
    if car["manufacturer"] is None or car["model"] is None or car["year"] is None:
        abort(400)
    new_car = carDAO.create(car)
    return jsonify(new_car)

# Update an existing car entry by ID
@app.route('/cars/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundCar = carDAO.findByID(id)
    if not foundCar:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    # Validate data types
    if 'year' in reqJson and type(reqJson['year']) is not int:
        abort(400)
    # Apply updates to the car record
    if 'manufacturer' in reqJson:
        foundCar['manufacturer'] = reqJson['manufacturer']
    if 'model' in reqJson:
        foundCar['model'] = reqJson['model']
    if 'year' in reqJson:
        foundCar['year'] = reqJson['year']
    carDAO.update(id, foundCar)
    return jsonify(foundCar)

# Delete a car by ID
@app.route('/cars/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    carDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)
