# **AirBnB clone - The console**👩‍💻

<img align="center" alt="github" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230303%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230303T195903Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46a41187266ba2a7b1462eac0d1f60fae67e27971b0d46458b12f71083ac1970" /></a>

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

	create: create <class>
	show: show <class> <id> or <class>.show(<id>)
	destroy: destroy <class> <id> or <class>.destroy(<id>)
	all: all or all <class> or <class>.all()
	count: count <class> or <class>.count()
	update: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update(<id>, <attribute dictionary>)

### Authors 👭🏻
* Nathaly Ortiz <a href="https://github.com/Natha0b" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
* Yurany Ulchur <a href="https://github.com/YuranyUlchur" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>