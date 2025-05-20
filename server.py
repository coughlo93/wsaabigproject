from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from carDAO import carDAO

# Initialize Flask app and configure static folder and CORS
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Serve the main HTML page
@app.route('/')
@cross_origin()
def index():
    return app.send_static_file('carviewer.html')

# Return all car entries
@app.route('/cars')
@cross_origin()
def getAll():
    return jsonify(carDAO.getAll())

# Return a specific car by ID
@app.route('/cars/<int:id>')
@cross_origin()
def findById(id):
    car = carDAO.findByID(id)
    if not car:
        abort(404)
    return jsonify(car)

# Add a new car to the CSV
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

    # Reject if any field is missing
    if car["manufacturer"] is None or car["model"] is None or car["year"] is None:
        abort(400)

    return jsonify(carDAO.create(car))

# Update an existing car by ID
@app.route('/cars/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundCar = carDAO.findByID(id)
    if not foundCar:
        abort(404)

    if not request.json:
        abort(400)

    reqJson = request.json

    # Validate year is numeric if provided
    if 'year' in reqJson and type(reqJson['year']) is not int:
        abort(400)

    # Apply updates only for provided fields
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

# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
