import cmd
import re
from shlex import split

from models import storage
from models.base_model import BaseModel
from models.state import User
from models.city import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_args(arg):
    """
    simplify arguments that user inputs.

    Args:
        arg (str): The user input.

    Returns:
        list: lists simplified arguments.
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            sequence = split(arg[:brackets.span()[0]])
            count = [i.strip(",") for i in sequence]
            count.append(brackets.group())
            return count
    else:
        sequence = split(arg[:curly_braces.span()[0]])
        count = [i.strip(",") for i in sequence]
        count.append(curly_braces.group())
        return count


class HBNBCommand(cmd.Cmd):
    """Creates the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }

    def blank_line(self):
        """No execution after empty line is displayed."""
        pass

    def quit_program(self, arg):
        """Enter Quit command to exit the program."""
        return True

    def EOF_signal(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def manage_invalid_input(self, arg):
        """manages incorrect user input."""
        print("*** Unknown syntax: {}".format(arg))
        return False

    def manage_missing_class(self, arg):
        """Manages missing class commands."""
        print("** class doesn't exist **")
        return False

    def manage_missing_instance(self, arg, class_name, instance_id):
        """Manages missing instance ID commands."""
        print(f"** no instance found ** ({class_name}.{instance_id})")
        return False

    def create_instance(self, arg):
        """Create a new class instance and print the id."""
        args = parse_args(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            self.handle_missing_class(arg)
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all().get(f"{args[0]}.{args[1]}")
            if obj is None:
                self.handle_missing_instance(arg, args[0], args[1])
            else:
                print(obj)

    def destroy_instance(self, arg):
        """Remove a class."""
        args = parse_args(arg)

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            self.handle_missing_class(arg)
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all().get(f"{args[0]}.{args[1]}")
            if obj is None:
                self.handle_missing_instance(arg, args[0], args[1])
