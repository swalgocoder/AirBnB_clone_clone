#!/usr/bin/python3
import datetime
import uuid

class BaseModel():
    def __init__(self, *args, **kwargs):
        """
        sets three attributes: 'id', 'created_at', 'updated_at'
        **kwargs: the number of arguments is unknown
        """
        """
        e.g.: kwargs = {'arg1":'Value one', 'arg2':'Value Two', 'arg3': 'Value Three}
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.utcnow())
        self.updated_at = str(datetime.datetime.utcnow())
        for x in args:
            if type(x) is dict:
                self.__dict__ = x
            else:
                if kwargs is not {}:
                    for key, value in kwargs:
                        self.key = value

    def save(self):
        '''This is the save method.
        save updates the updated_at attribute with current date and time.
        save calls on the FileStorage class to save new instances of BaseModel.
        '''
        self.updated_at = str(datetime.datetime.utcnow())

    def to_json(self):
        '''This is the to_json method.
        The method returns a dictionary with all key/value pairs.

        Returns: dictionary
        '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        '''This is the string method.

        Returns: formatted string to print
        '''
        class_name = type(self).__name__
        id_string = self.id
        return ("[{}] ({}) {}".format(class_name, id_string, self.__dict__))
