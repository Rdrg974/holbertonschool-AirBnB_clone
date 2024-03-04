#!/usr/bin/python3
"""Console module."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show string representation of instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances."""
        if arg and arg not in [cls.__name__ for cls in storage.all().values()]:
            print("** class doesn't exist **")
            return
        if arg:
            objs = [str(obj) for key, obj in storage.all().items() if key.split('.')[0] == arg]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles end of file."""
        return True

    def emptyline(self):
        """Handles empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
