AirBnB clone
------------

Project description - Our project focuses on building a command interpreter to run AirBnB objects. The command interpreter is similar to that of a simple shell in which it is unix-based. This allows users to interact with the web application through a command-line.

How to initialize the interpreter - In order to run our command-line interpreter, we need to create an entry point. We do this by creating the following:

- create our console.py file
- Import the cmd module from Python standard library
- Define the class 'HBNBCommand' that inherits from cmd.Cmd
- At the bottom of our file we add if __name__ == '__main__':
    HBNBCommand().cmdloop(), this will create an instance of our interpreter using the cmdloop() function.
- We turn our console.py into an executable in order to start it
- run $ ./console.py in terminal to initialize


To make our command-line usable we need to create arguments into our 'HBNBCommand class. The commands required are listed as follows:

- To exit the program when we run 'quit' we create 'do_quit(self, arg) with 'self' referencing the instance of a class while arg is passed to the quit method when called.

- do_EOF(self, arg) will exit the program when EOF signal is sent, an example usage of this is pressing CTRL+C.

- help_quit(self) prints the document for the 'quit' command

- emptyline(self) handles an emptyline input by not executing anything.

- We can then run 'quit' or send an EOF signal to exit as well as run 'help' for a list of available commands.
