#!/usr/bin/python3
""" module that contains the command interpreter """
import cmd
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """ defines command interpreter class """
    prompt = '(hbnb) '

    __list_class = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review()
        }

    def do_create(self, args):
        'Creates new instance and saves it to JSON file\n'
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__list_class:
            print("** class doesn't exist **")
        else:
            new = self.__list_class[args]
            new.save()
            print(new.id)

    def do_show(self, args):
        'Prints a string representation of an instance, based on name and id\n'
        all_objs = storage.all()
        arg_list = args.split()
        if not arg_list:
            print("** class name is missing **")
        elif arg_list[0] not in HBNBCommand.__list_class:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in all_objs.keys():
                if arg_list[1] == all_objs[obj_id].id:
                    print(all_objs[obj_id])
                    match = True
            if match is not True:
                print("** no instance found **")

    def do_all(self, args):
        'Prints string representation multiple instances\n'
        arg_list = args.split()
        all_objs = storage.all()
        if len(args) == 0:
            rep_list = []
            for obj_id in all_objs.keys():
                rep_list.append(all_objs[obj_id].__str__())
            print(rep_list)
        elif arg_list[0] not in HBNBCommand.__list_class:
            print("** class doesn't exist **")
        else:
            rep_list = []
            for obj_id in all_objs.keys():
                if arg_list[0] == all_objs[obj_id].__class__.__name__:
                    rep_list.append(all_objs[obj_id].__str__())
            print(rep_list)

    def do_update(self, args):
        'Updates an instance\n'
        arg_list = args.split()
        all_objs = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__list_class:
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
                    print("** attribute name is missing **")
                elif len(arg_list) == 3:
                    print("** value is missing **")
                else:
                    setattr(match, arg_list[2], arg_list[3])

    def do_destroy(self, args):
        'Deletes an instance based on class name and id\n'
        all_objs = storage.all()
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__list_class:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in all_objs:
                if arg_list[1] == all_objs[obj_id].id:
                    try:
                        match = True
                        del all_objs[obj_id]
                        new = {}
                        with open("file.json", 'w', encoding='utf-8') as jf:
                            for key, value in all_objs.items():
                                new.update({key: value.to_dict()})
                            jf.write(json.dumps(new))
                        break
                    except KeyError:
                        pass

            if match is not True:
                print("** no instance found **")

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        exit()

    def postcmd(self, stop, line):
        """ continues command interpreter after help """
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
