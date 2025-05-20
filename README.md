# Car Viewer Web App

This project is a web application that allow the user to view, add, update, and delete cars (CRUD operations) using a Flask RESTful API and a CSV-based data source. It is a customised version of the "bookviewer" sample provided by my lecturer Andrew Beatty, in which I have modified it to manage cars instead of books.

---

## Assignment Brief

The goal of the assignment was to:
- Create a Flask-based web app with a RESTful API
- Provide a web interface using HTML and AJAX (JavaScript)
- Use CSV data instead of a traditional database
- Replace the original book data with car listings (Manufacturer, Model, Year)
- Provide full CRUD functionality via both API and UI

---

## How I Completed This Project

### 1. Downloaded the Starter Template
I downloaded the [deploytopythonanywhere](https://github.com/andrewbeattycourseware/deploytopythonanywhere) template provided by Andrew Beatty to use as my base.

---

### 2. Changed the Context to Cars
I changed all references to "books" to "cars":
- In HTML - carviewer.html
- In Flask routes - server.py
- In the data handler - carDAO.py

The fields that I changed were:
- Title → Manufacturer
- Author → Model
- Price → Year

---

### 3. Created Random Car Data
Using ChatGPT, I prompted that it generate a csv file with 200 random car listings, including:
- Manufacturer (e.g. Toyota, BMW)
- Model (e.g. Corolla, Qashqai)
- Year (1995–2024)

The CSV that I generated was used as the main data source.

---

### 4. Developed - carDAO.py
I wrote a CSV-based DAO (Data Access Object) named carDAO.py that:
- Reads all cars from cars.csv on startup
- Adds new cars and saves them back to the CSV
- Updates/deletes records and rewrites the CSV

---

### 5. Built the REST API in - server.py
The Flask app handles the following endpoints:
- `GET /cars` – List all cars
- `GET /cars/<id>` – Get a specific car
- `POST /cars` – Add a new car
- `PUT /cars/<id>` – Update a car
- `DELETE /cars/<id>` – Delete a car

I used the flask-cors library to enable AJAX from the frontend.

---

### 6. Updated the HTML + JavaScript
In carviewer.html:
- I changed the title to "Cars"
- Updated the form and table to use Manufacturer, Model, Year
- Used jQuery to handle form submissions and dynamic updates via AJAX calls to the Flask API

---

### 7. Tested the App Locally in VS Code
I ran the app locally using the below code:
```bash
python -m venv venv
source venv\Scripts\activate
pip install flask flask-cors
python server.py
```

Then I accessed it in the browser at:  
**http://127.0.0.1:5000**

---

### 8. Packaged the Project
I zipped the folder with all necessary files:
- server.py
- carDAO.py
- carviewer.html
- cars.csv
- README.md

### 9. Uploaded to PythonAnywhere

- I signed up to use PythonAnywhere where I was able to upload the project to my [PythonAnywhere](https://coughlo93.eu.pythonanywhere.com/).
- Uploaded all project files via the files tab.
- I changed the working directory tab to /home/coughlo93
- I updated the WSGI configuration file to point to my Flask app. 
- I initially struggled with this until I realised that I needed to install flask to the console
- Once I done installed Flask, I reloaded the page and it was live at [https://coughlo93.eu.pythonanywhere.com]( https://coughlo93.eu.pythonanywhere.com)

---

## References

1. Andrew Beatty’s [Flask Deployment Template](https://github.com/andrewbeattycourseware/deploytopythonanywhere)
2. Flask Documentation – https://flask.palletsprojects.com/
3. Flask-CORS – https://flask-cors.readthedocs.io/
4. jQuery AJAX – https://api.jquery.com/jQuery.ajax/
5. MDN Web Docs – https://developer.mozilla.org/en-US/
6. RESTful API Design Guide – https://restfulapi.net/
7. CSV Module (Python) – https://docs.python.org/3/library/csv.html
8. Stack Overflow – https://stackoverflow.com/
9. PythonAnywhere Guide – https://help.pythonanywhere.com/pages/Flask/
10. JavaScript ES6 Syntax – https://www.w3schools.com/js/js_es6.asp

---
### Author: Owen Coughlan
### Email: g00439345@atu.ie

---