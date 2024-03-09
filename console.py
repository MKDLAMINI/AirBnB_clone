#!/usr/bin/python3
"""
This module defines our bnb console
"""
import cmd
import re
import shlex
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Creates the HolbertonBnB command interpreter.
    """

    prompt = "(hbnb) "
    bnb_classes = {
        'BaseModel': BaseModel, 'User': User,
        'Place': Place, 'City': City,
        'State': State, 'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print("")
        return True

    def emptyline(self):
        """
        No execution after empty line is displayed.
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program.")

    def help_EOF(self):
        """
        Help message for the EOF signal.
        """
        print("EOF signal to exit the program.")

    def do_create(self, args):
        """
        Create a new instance of a class.
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.bnb_classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.bnb_classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Print the string representation of an instance.
        """
        class_name, instance_id = self._parse_args(args, 2)
        if not instance_id:
            print("** instance id missing **")
            return
        elif not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.bnb_classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id.
        """
        class_name, instance_id = self._parse_args(args, 2)
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.bnb_classes:
            print("** class doesn't exist **")
            return
        elif not instance_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
        else:
            del instances[key]
            storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        instance_objects = storage.all()

        bnb_command = shlex.split(arg)

        if len(bnb_command) == 0:
            for command_idx, data in instance_objects.items():
                print(str(data))
        elif bnb_command[0] not in self.bnb_classes:
            print("** class doesn't exist **")
        else:
            class_name = bnb_command[0]
            class_instances = [
               str(data)
               for command_idx, data in instance_objects.items()
               if command_idx.split('.')[0] == class_name
            ]
            if class_instances:
                for instance in class_instances:
                    print(instance)
            else:
                print("** no instance found **")

    def default(self, arg):
        """
        Called when an unknown command is entered.
        """
        arguments = arg.split('.')
        class_name = arguments[0]
        command = arguments[1].split('(')
        method_name = command[0]
        method_dict = {
            'all': 'do_all',
        }
        if method_name in method_dict:
            method = getattr(self, method_dict[method_name])
            return method("{} {}".format(class_name, ''))

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_update(self, args):
        """
        Update an instance based on the class name and id.
        """
        class_name, instance_id, *attributes = self._parse_args(args, 3)
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.bnb_classes:
            print("** class doesn't exist **")
            return
        elif not instance_id:
            print("** instance id missing **")
            return
        elif not attributes:
            print("** attribute name missing **")
            return
        elif len(attributes) == 1:
            print("** value missing **")
            return

        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        instance = instances.get(key)
        if not instance:
            print("** no instance found **")
            return

        for attr_name, attr_value in zip(attributes[::2], attributes[1::2]):
            setattr(instance, attr_name, attr_value)
        instance.save()

    def _parse_args(self, args, expected_length):
        """Parse command arguments."""
        parsed_args = args.split()
        if len(parsed_args) < expected_length:
            return (None,) * expected_length
        return tuple(parsed_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
