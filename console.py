#!/usr/bin/python3
"""
contains the entry point of the command interpreter

"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage
from models import storage
import json


class HBNBCommand(cmd.Cmd):

    """
    HBNB console
    """

	_classes =  {
	"BaseModel": BaseModel,
	"User": User,
	"Place": Place,
	"State": State,
	"City": City,
	"Amenity": Amenity,
	"Review": Review
}

    prompt = "(hbnb) "

    def do_quit(self, arg):
	"""
	Quit command to exit the program:
	- quit

	"""
	return True
    
    def do_EOF(self, arg):
	"""
	End Of File: exit the program
	-EOF

	"""
	return True

    def help_quit(self):
	"""This action is provided by default by cmd"""

    print("Quit command to exit the program\n")
	return True
    def help_EOF(self):
	"""EOF help"""
 
    print("End Of File: exit the program\n")
	return True
    
    def emptyline(self):
	"""
	empty line + Enter should not execute anything
	"""
	return False

    def do_create(self, arg):
	"""
	creates instance of Basemodel
	save it to json and prints the id
	"""
	if not arg:
	
	print("** class name missing **")

	elif args not in self.classes:
	print("** class doesn't exist **")

	else:
	new = self.classes[args]
	new.save()
	print(new.id)

    def do_show(self, args):
	""" Prints the string representation of an instance based on class and id\n"""
	rep = storage.all()
	arg = args.split()
	if not arg :
	    print("** class name missing **")
	elif arg[0] not in self.classes:
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
	""" Delete an instance based on the class name and id\n """

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
