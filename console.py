#!/usr/bin/python3
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Creates the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    bnb_classes = {
        'BaseModel': BaseModel, 'User': User,
        'Place': Place, 'City': City,
        'State': State, 'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """No execution after empty line is displayed."""
        pass

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program.")

    def help_EOF(self):
        """Help message for the EOF signal."""
        print("EOF signal to exit the program.")

    def do_create(self, args):
        """Create a new instance of a class."""
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
        """Print the string representation of an instance."""
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
        """Delete an instance based on the class name and id."""
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

    def do_all(self, args):
        """Print all string representations of instances."""
        if args and args not in HBNBCommand.bnb_classes:
            print("** class doesn't exist **")
            return

        instances = storage.all().values()
        if args:
            class_instances = [
                str(instance) for instance in instances
                if isinstance(instance, HBNBCommand.bnb_classes[args])
            ]
        else:
            class_instances = [str(instance) for instance in instances]

        print(class_instances)

    def do_update(self, args):
        """Update an instance based on the class name and id."""
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
