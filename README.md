# AirBnb Clone - The Console

## Table of contents

* [Description of project](#description-of-project)
* [Description of the command interpreter](#description-of-the-command-interpreter)
* [Resources](#resources)
* [Learning Objectives](#learning-objectives)
* [Requirements](#requirements)
* [Authors](#authors)

## Description of project

The Airbnb Clone - the console project is an essential introductory step towards constructing a comprehensive web application - the Airbnb clone. By developing a command interpreter, users can effectively manage Airbnb objects through a console interface. This initial phase lays the groundwork for subsequent project components, including HTML/CSS templating, database storage, API integration, and front-end development.

Each task in the project is crucial for developing the Airbnb Clone application. It starts with setting up a parent class, BaseModel, for managing instance initialization and data storage. Then, a streamlined process for data serialization and deserialization is established. Next, all necessary classes for Airbnb functionality are created, and a file storage engine is implemented for data management. Finally, comprehensive unittests are conducted to ensure the reliability of the system.

## Description of the command interpreter

The command interpreter in the Airbnb Clone project acts as a crucial link between users and the system, enabling smooth interaction through text-based commands. Users input actions such as creating, modifying, or searching for Airbnb objects, which the interpreter analyzes, executes, and provides feedback on. Currently, the command interpreter allows for creating new objects (e.g., a new user or a new location), retrieving objects from a file, database, etc., performing operations on objects (such as counting, computing statistics, etc.), updating object attributes, and destroying an object.

## Resources

* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [**packages** concept page]
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Requirements
### Python Script

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/python3```
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Test Cases

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### More info

Your shell should work like this in interactive mode:

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

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo ```"python3 -m unittest discover tests" | bash```

## Authors

* [Abdou Rodrigue HASSANY MOHAMED](https://github.com/Rdrg974)
* [Kaïs PAUMOND](https://github.com/kjuarez38)
