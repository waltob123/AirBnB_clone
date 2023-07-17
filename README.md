# AirBnB Clone
#

This project is clone of the AirBnB web application written in the Python Programming Language. The application stores data using a json file and it also has a console where users can interact with the application.

## How to start the console.
#

To start the console application, if you are on a linux operating system and have python3 installed you can use the command ```path_to_the_console/console.py``` from the terminal.

If you are on a windows machine or macOS you can start the application from a command prompt or a terminal. First navigate to where the console.py is then type the command `python3 console.py`.

## How to use the console
#
To use the console you have to type the command and pass it an argument.
Example
```
(hbnb) show User
```
You can type help to get all commands or type help with the command name to get help on a particular command.
Example
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help count
Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
(hbnb) help create
Usage: create <class>
        Create a new class instance and print its id.
        
(hbnb) 
```

To close the application you can type quit or EOF to close the application.
Example
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help count
Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
(hbnb) help create
Usage: create <class>
        Create a new class instance and print its id.
        
(hbnb) quit
(venv) Nanas-MacBook-Pro-2:AirBnB_clone fsociety123$ 
```
```
(venv) Nanas-MacBook-Pro-2:AirBnB_clone fsociety123$ python3 console.py
(hbnb) help update
Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
(hbnb) EOF

(venv) Nanas-MacBook-Pro-2:AirBnB_clone fsociety123$ 
```

You can create a new user using create User
```
(venv) Nanas-MacBook-Pro-2:AirBnB_clone fsociety123$ python3 console.py
(hbnb) create User
93f5cfd4-471c-48e8-ae63-00dcbee34ef8
```

You can show a user by typing show User <user_id>
```
(hbnb) show User 93f5cfd4-471c-48e8-ae63-00dcbee34ef8
[User] (93f5cfd4-471c-48e8-ae63-00dcbee34ef8) {'id': '93f5cfd4-471c-48e8-ae63-00dcbee34ef8', 'created_at': datetime.datetime(2023, 7, 16, 22, 58, 16, 730522), 'updated_at': datetime.datetime(2023, 7, 16, 22, 58, 16, 730905)}
(hbnb) 
```

You can update a user by typing update User <user_id> <attribute_to_update>
```
(hbnb) update User 93f5cfd4-471c-48e8-ae63-00dcbee34ef8 first_name "John"
(hbnb) show User 93f5cfd4-471c-48e8-ae63-00dcbee34ef8
[User] (93f5cfd4-471c-48e8-ae63-00dcbee34ef8) {'id': '93f5cfd4-471c-48e8-ae63-00dcbee34ef8', 'created_at': datetime.datetime(2023, 7, 16, 22, 58, 16, 730522), 'updated_at': datetime.datetime(2023, 7, 16, 22, 58, 16, 730905), 'first_name': 'John'}
(hbnb) 
```

You can delete a user by typing destroy User <user_id>
```
(hbnb) destroy 93f5cfd4-471c-48e8-ae63-00dcbee34ef8
** class doesn't exist **
(hbnb) destroy User 93f5cfd4-471c-48e8-ae63-00dcbee34ef8
(hbnb) 
```

You can use `all <class_name>` or `<class_name>.all()` to show all instances creaated for a particular class.


## Authors
Desmond Asiedu Asamoah <walterobrien_123@yaho.com>

Nana Nyarko Asare <nananyarkoasare74@gmail.com>
