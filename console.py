#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for hbnb command line interpreter"""

    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Place": Place(),
        "Amenity": Amenity(),
        "Review": Review()
    }

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'EOF command to exit the program\n'
        exit()

    def do_create(self, args):
        'Creates a new instance of BaseModel, saves it (to the JSON file)\n'
        if not args:
            print("** class name missing **")
        elif args not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = self.__classes[args]
            new.save()
            print(new.id)

    def do_show(self, args):
        'Prints string representation for instance based on class and id\n'
        rep = storage.all()
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in rep:
                if arg[1] == rep[obj_id].id:
                    print(rep[obj_id])
                    match = True
            if match is not True:
                print("** no instance found **")

    def do_destroy(self, args):
        'Deletes an instance based on the class name and id\n'
        rep = storage.all()
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in rep:
                if arg[1] == rep[obj_id].id:
                    try:
                        match = True
                        del rep[obj_id]
                        new = {}
                        with open("file.json", 'w', encoding="utf-8") as json_file:
                            for key, value in rep.items():
                                new.update({key: value.to_dict()})
                            json_file.write(json.dumps(new))
                        break
                    except KeyError:
                        pass

            if match is not True:
                print("** no instance found **")

    def do_all(self, args):
        'Prints string representations of all instances\n'
        rep = storage.all()
        arg = args.split()
        if len(args) == 0:
            obj_list = []
            for obj in rep.keys():
                obj_list.append(rep[obj].__str__())
            print("{}".format(obj_list))
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in rep.keys():
                if arg[0] == rep[obj].__class__.__name__:
                    obj_list.append(rep[obj].__str__())
            print("{}".format(obj_list))

    def do_update(self, args):
        'Updates an instance\n'
        arg_list = args.split()
        all_objs = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in all_objs.keys():
                if arg_list[1] == all_objs[obj_id].id:
                    match = all_objs[obj_id]
            if match is False:
                print("** no instance found **")
            else:
                if len(arg_list) == 2:
                    print("** attribute name missing **")
                elif len(arg_list) == 3:
                    print("** value missing **")
                else:
                    setattr(match, arg_list[2], arg_list[3])

    def postcmd(self, stop, line):
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
