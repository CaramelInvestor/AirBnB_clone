# AirBnB_clone
AirBnB clone - The console project

Welcome to the AirBnB clone project!

The console project has to do with:
creating your data model
managing (creating, updating, destroying, etc) objects via a console / command interpreter
storing and persisting objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

# `Commands:`
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* update - Updates an instance based on the class name and id
* quit/EOF - quit the console
* help - see descriptions of commands

To start console type in shell

    AirBnB_clone$ ./console.py
    (hbnb) 

## `Create`
To create an object use format "create <ClassName>" ex:

	(hbnb) create BaseModel

## `Show`
To show an instance based on the class name and id. Ex: 

	(hbnb) show BaseModel 1234-1234-1234.

# `Supported classes:`
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

# `Authors`

**Okonkwo Chiamaka** **[Email](okonkwosmmac@gmail.com@)**


