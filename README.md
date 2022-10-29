# 0x00. AirBnB clone - The console

## Description

A console version of AirBnB clone. Implemented using python programming language.

## Command Line Interpreter

This provides a Command Line Interface (CLI) for interacting with the AirBnB

### How to start the interpreter
```bash
$ ./console.py
(hbnb) 
```
### How to use it
ACTION | COMMAND
------ | -------
Create a user | User.create()
Print user instance count | User.count()
Print all users: | User.all()
Print user will specific id: | User.show("id-here")
Update user details: | User.update("id-here", "attribute", "value")
Update user using dictionary: | User.update("id-here", {"attribute": "value"})
Delete a user by id | User.destroy("id-here")
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Examples
```bash
$ ./console.py
(hbnb) 
```
