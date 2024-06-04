# Airbnb Console Project

## Description
The **Airbnb Console Project** is a command-line interface (CLI) application that simulates the backend of an Airbnb-like service. It allows users to create, read, update, and delete various objects such as users, places, amenities, and more. 

In addition to the CLI application, this project includes a responsive front-end built with HTML and CSS, showcasing the integration of backend and frontend technologies.

## Features
- **Command Interpreter:** A custom command interpreter to manage and manipulate data.
- **CRUD Operations:** Create, Read, Update, and Delete operations for various objects.
- **Persistence:** Data is persisted through serialization and deserialization using JSON files.
- **Responsive Front-end:** A responsive web interface built with HTML and CSS to display and interact with the data.
- **Console Commands:**
  - `create`: Creates a new object.
  - `show`: Shows the string representation of an object.
  - `destroy`: Deletes an object.
  - `all`: Shows all objects or all objects of a specific class.
  - `update`: Updates an object's attributes.
  - `count`: Counts the number of instances of a class.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/BaduDueduMaxwell/AirBnB_clone.git
    ```
2. **Navigate into the project directory:**
    ```bash
    cd AirBnB_clone
    ```

## Usage
Start the console by running the `console.py` script:
```bash
./console.py
```

### Example Commands
- **Create a new User:**
    ```bash
    (hbnb) create User
    ```
- **Show a User:**
    ```bash
    (hbnb) show User <user_id>
    ```
- **Update a User:**
    ```bash
    (hbnb) update User <user_id> email "newemail@example.com"
    ```
- **Delete a User:**
    ```bash
    (hbnb) destroy User <user_id>
    ```
- **Show all Users:**
    ```bash
    (hbnb) all User
    ```

## File Structure
- `console.py`: The main console script.
- `models/`: Directory containing all the model classes.
  - `base_model.py`: Base model with common attributes and methods.
  - `user.py`: User model.
  - Other model files for Place, State, City, Amenity, Review.
- `models/engine/`: Directory containing the storage engine.
  - `file_storage.py`: Handles the serialization and deserialization of objects to JSON files.
- `web_static/`: Directory containing the HTML and CSS files for the front-end.
  - `styles/`: Directory containing CSS files.
  - `index.html`: Main HTML file.
- `tests/`: Directory containing unittests for the models and the console.

## Contributors
- [Maxwell Duedu](https://github.com/BaduDueduMaxwell)
