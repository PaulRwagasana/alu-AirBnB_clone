# AirBnB Clone Project

## Description of the Project
This project is a simple clone of the AirBnB website. The first stage focuses on implementing a backend interface or console to manage program data (similar to a shell). The console provides commands to create, update, destroy objects, and manage file storage.

### Console Tasks
- Implement a parent class (`BaseModel`) to handle initialization, serialization, and deserialization of future instances.
- Develop a simple serialization/deserialization flow: `Instance <-> Dictionary <-> JSON string <-> file`.
- Create all classes for AirBnB (`User`, `State`, `City`, `Place`, etc.) that inherit from `BaseModel`.
- Build the first abstracted storage engine for the project: **File Storage**.
- Write unittests to validate all classes and the storage engine.

## Description of the Command Interpreter
The command interpreter allows management of project objects by:
- Creating a new object (e.g., a `User` or `Place`).
- Retrieving an object from a file, database, etc.
- Performing operations on objects (e.g., counting, computing stats).
- Updating attributes of an object.
- Destroying an object.

### How to Start the Interpreter
To start the command interpreter, run:
```bash
./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  delete  destroy  exit  help  q  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit

```
### Tests

this is how to run all tests:
```bash
 python3 -m unittest discover tests
```
This is how to run specific tests
```bash
 python3 -m unittest tests/test_models/test_city.py
```

### Authors

<p><b>Kelvin Rwihimba</b></p>
<P><b>Paul Rwagasana</b></P>


