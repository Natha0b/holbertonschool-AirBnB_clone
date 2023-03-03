# **AirBnB clone - The console**👩‍💻

<img align="center" src="https://miro.medium.com/max/1400/0*NChTo-XqLOxLabIW" /></a>

## 	DESCRIPTION PROYECT✍
 The project aims to deploy a server on a simple copy of the** AirBnB** website. Keeping in mind that some of the features will be implemented, in order to cover all the fundamental concepts of the higher level programming path.

#### 📍 DESCRIPTION OF THE COMMAND INTERPRETER
It is a command interpreter to manipulate data without a visual interface, as in a shell (perfect for development and debugging).
A website (the front-end) that displays the final product to everyone: static and dynamic.

A database or files that store data** (data = objects)**
An API that provides a communication interface between the front-end and your data (retrieve it, create it, delete it, update it)

## 📍 Console 
##### This is a command interpreter to manipulate data without a visual interface.

###### 📍 No interactive mode:
`$ ./console.py`

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

##### 📍 Interactive mode:
`$ ./console.py`

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

##### On this mode the console displays a prompt wating for input:

`$ ./console.py
(hbnb) `

##### To exit enter the command quit, or input an EOF signal (ctrl-D).

`$ ./console.py
(hbnb) quit
$`

`$ ./console.py
(hbnb) EOF
$`

## Commands 📋
##### This console supports the folow commands:

	create: `create <class>`
	show: `show <class> <id> or <class>.show(<id>)`
	destroy: `destroy <class> <id> or <class>.destroy(<id>)`
	all:` all or all <class> or <class>.all()`
	count: `count <class> or <class>.count()`
	update: `update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update(<id>, <attribute dictionary>)`

### Authors 👭🏻
* Nathaly Ortiz <a href="https://github.com/Natha0b" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
* Yurany Ulchur <a href="https://github.com/YuranyUlchur" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>