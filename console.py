#!/usr/bin/python3
"""the console command interpreter module"""

import ast
import cmd

from models import all_class, storage


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter class

    Args:
        cmd (module): base class module
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """quit command"""
        return True

    def help_quit(self):
        """help quit"""
        print("\n".join(["Quit command to exit the program", ""]))

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id

        usage: (hbnb) create <class name>
        """
        if arg:
            if arg in all_class:
                my_obj = all_class[arg]()  # creates instance of class
                my_obj.save()
                print(my_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id

        usage: (hbnb) show <class name> <id>
        """
        my_args = arg.split(" ")
        if arg:
            if len(my_args) < 2 and my_args[0] in all_class:
                print("** instance id missing **")
            else:
                if my_args[0] in all_class:
                    key = f"{my_args[0]}.{my_args[1]}"
                    if key in storage.all():
                        print(str(storage.all()[key]))
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)

        usage: (hbnb) destroy <class name> <id>
        """
        my_args = arg.split(" ")
        if arg:
            if len(my_args) < 2 and my_args[0] in all_class:
                print("** instance id missing **")
            else:
                if my_args[0] in all_class:
                    key = f"{my_args[0]}.{my_args[1]}"
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name

        usage: (hbnb) all <class name>
        usage: (hbnb) all
        """
        if arg and arg not in all_class:
            print("** class doesn't exist **")
        elif arg:
            print([str(v) for k, v in storage.all().items()
                   if k.split(".")[0] == arg])
        else:
            print([str(v) for k, v in storage.all().items()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        (save the change into the JSON file)

        usage: update <class name> <id> <attribute name> <attribute value>
        """
        if not arg:
            print("** class name missing **")
        else:
            my_arg = arg.split(" ")

            if my_arg[0] not in all_class:
                print("** class doesn't exist **")
            else:
                if len(my_arg) == 1:
                    print("** instance id missing **")
                if len(my_arg) > 1:
                    my_id = my_arg[1]
                    key = f"{my_arg[0]}.{my_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    elif len(my_arg) == 2:
                        print("** attribute name missing **")
                    elif len(my_arg) == 3:
                        print("** value missing **")

                    elif len(my_arg) >= 4:
                        if my_arg[2] in ("created_at", "updated_at", "id"):
                            pass
                        else:
                            my_model = storage.all()[key]
                            setattr(my_model, my_arg[2], eval(my_arg[3]))
                            storage.all()[key].save()

    def default(self, line):
        """returns a list of the string representation of a named class

        Usage: <class_name>.all()
        """
        args = line.split(".", 1)
        class_name = args[0]
        if args[1] == "all()":
            self.do_all(class_name)
        elif args[1] == "count()":
            if class_name in all_class:
                print(
                    len(
                        [
                            str(v)
                            for k, v in storage.all().items()
                            if k.split(".")[0] == class_name
                        ]
                    )
                )
        elif args[1].startswith("show"):
            class_id = args[1].split("(")[1].split(")")[0]
            arg = f"{class_name} {class_id}"
            self.do_show(arg)
        elif args[1].startswith("destroy"):
            class_id = args[1].split("(")[1].split(")")[0]
            arg = f"{class_name} {class_id}"
            self.do_destroy(arg)
        elif args[1].startswith("update"):
            line_str = str(args[1:]).split("(")[1].split(")")[0]
            if ", {" not in line_str:
                arguments = line_str.split(", ")
                arg = f"{class_name} {arguments[0]}"\
                    f" {arguments[1]} {arguments[2]}"
                self.do_update(arg)
            else:
                _id = str(line_str[0:36])
                _dict_str = str(line_str[38:])
                my_dict = ast.literal_eval(_dict_str)
                for key, val in my_dict.items():
                    arg = f"{class_name} {_id} {repr(key)} {repr((val))}"
                    self.do_update(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
