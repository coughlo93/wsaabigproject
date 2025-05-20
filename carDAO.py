import csv

class CarDAO:
    def __init__(self, filename='cars.csv'):
        self.filename = filename
        # Load data from the CSV file
        self.cars = []
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                # Expect header row first
                headers = next(reader, None)
                # Columns: Manufacturer, Model, Year in that order
                for idx, row in enumerate(reader):
                    if not row:
                        continue
                    if len(row) < 3:
                        continue  # skip malformed lines
                    manufacturer = row[0]
                    model = row[1]
                    year_str = row[2]
                    try:
                        year = int(year_str)
                    except ValueError:
                        year = None
                    car = {
                        "id": idx + 1,  # assign IDs starting from 1
                        "manufacturer": manufacturer,
                        "model": model,
                        "year": year
                    }
                    self.cars.append(car)
            # Set last_id to the last assigned ID from file
            if self.cars:
                self.last_id = self.cars[-1]["id"]
            else:
                self.last_id = 0
        except FileNotFoundError:
            
            self.cars = []
            self.last_id = 0

    def save_to_file(self):
        # Save the current list of cars back to the CSV file (overwrite whole file)
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(["Manufacturer", "Model", "Year"])
            for car in self.cars:
                # Write each car's data (excluding the internal id in the CSV)
                writer.writerow([car["manufacturer"], car["model"], car["year"]])

    def getAll(self):
        # Return list of all car records
        return self.cars

    def findByID(self, id):
        # Find a car by its id, return a copy of the record or None if not found
        for car in self.cars:
            if car["id"] == id:
                return car.copy()
        return None

    def create(self, car):
        # car is a dict with keys "manufacturer", "model", "year"
        self.last_id += 1
        # Ensure year is int if provided as string
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
        # Append the new car entry to the CSV file
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([new_car["manufacturer"], new_car["model"], new_car["year"]])
        return new_car

    def update(self, id, car):
        # car is a dict with keys "id", "manufacturer", "model", "year"
        for i, existing in enumerate(self.cars):
            if existing["id"] == id:
                # Update the internal record with new values
                self.cars[i]["manufacturer"] = car.get("manufacturer", existing["manufacturer"])
                self.cars[i]["model"] = car.get("model", existing["model"])
                self.cars[i]["year"] = car.get("year", existing["year"])
                # After updating in memory, rewrite the entire CSV file to save changes
                self.save_to_file()
                return

    def delete(self, id):
        # Remove car by id if it exists
        for i, existing in enumerate(self.cars):
            if existing["id"] == id:
                self.cars.pop(i)
                # After removal, rewrite the CSV file to save changes
                self.save_to_file()
                return

# Create a single instance for use in the application
carDAO = CarDAO()
