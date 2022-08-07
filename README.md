# AirBnb Clone
## Brief Description

 This project is the first of a much bigger project of the Airbnb clone Web application. It focuses on building a project knowing the following skills:

 ```
-How to create a Python package
-How to create a command interpreter in Python using the cmd module
-What is Unit testing and how to implement it in a large project
-How to serialize and deserialize a Class
-How to write and read a JSON file
-How to manage datetime
-What is an UUID
-What is *args and how to use it
-What is **kwargs and how to use it
-How to handle named arguments in a function
```

 This project is created using the **Python** programming/scripting language. It is an implementation of some tasks of the second trimester of the alx software engineering programmme. The interface is a command interpreter.


## The Command Interpreter
 This  works like a shell but with a specific use case.
 It  does the following:
 ```
- Creates a new object (ex: a new User or a new Place)
-Retrieves an object from a file, a database etc…
-Does operations on objects (count, compute stats, etc…)
-Updates attributes of an object
-Destroys an object
```
A good example is shown below:

  **For an interactive mode**
```shell
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

**For non-interaactive mode**
```shell
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

> The command is started by running  the AirBnb script and passing in arguments.
---