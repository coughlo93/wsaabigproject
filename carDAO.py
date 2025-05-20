import csv

class CarDAO:
    def __init__(self, filename='cars.csv'):
        self.filename = filename
        self.cars = []

        # Attempt to load existing car records from CSV
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)  # Skip header row
                for idx, row in enumerate(reader):
                    if len(row) < 3:
                        continue  # Skip incomplete rows
                    try:
                        year = int(row[2])
                    except ValueError:
                        year = None
                    car = {
                        "id": idx + 1,
                        "manufacturer": row[0],
                        "model": row[1],
                        "year": year
                    }
                    self.cars.append(car)
            self.last_id = self.cars[-1]["id"] if self.cars else 0
        except FileNotFoundError:
            # Start with an empty list if the CSV doesn't exist yet
            self.cars = []
            self.last_id = 0

    def save_to_file(self):
        # Overwrite the CSV file with current in-memory car list
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Manufacturer", "Model", "Year"])
            for car in self.cars:
                writer.writerow([car["manufacturer"], car["model"], car["year"]])

    def getAll(self):
        # Return the full list of cars
        return self.cars

    def findByID(self, id):
        # Return a copy of the car with matching ID, if found
        for car in self.cars:
            if car["id"] == id:
                return car.copy()
        return None

    def create(self, car):
        # Add a new car to the list and append it to the CSV
        self.last_id += 1
        year = car.get("year")
        if isinstance(year, str):
            try:
                year = int(year)
            except:
                year = None
        new_car = {
            "id": self.last_id,
            "manufacturer": car.get("manufacturer"),
            "model": car.get("model"),
            "year": year
        }
        self.cars.append(new_car)
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([new_car["manufacturer"], new_car["model"], new_car["year"]])
        return new_car

    def update(self, id, car):
        # Update an existing car's details by ID
        for i, existing in enumerate(self.cars):
            if existing["id"] == id:
                self.cars[i]["manufacturer"] = car.get("manufacturer", existing["manufacturer"])
                self.cars[i]["model"] = car.get("model", existing["model"])
                self.cars[i]["year"] = car.get("year", existing["year"])
                self.save_to_file()
                return

    def delete(self, id):
        # Remove a car from the list by ID and save the updated list
        for i, existing in enumerate(self.cars):
            if existing["id"] == id:
                self.cars.pop(i)
                self.save_to_file()
                return

# Create a global DAO instance that can be imported into other modules
carDAO = CarDAO()
