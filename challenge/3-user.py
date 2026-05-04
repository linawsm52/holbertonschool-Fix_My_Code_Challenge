#!/usr/bin/python3
"""
User class
"""

class User():
    """ User class """

    def __init__(self):
        """ Init """
        self.__password = None

    @property
    def password(self):
        """ Getter password """
        return self.__password

    @password.setter
    def password(self, value):
        """ Setter password """
        if type(value) is not str:
            raise TypeError("password must be a string")
        self.__password = value

    def is_valid_password(self, password):
        """ Test if password is valid """
        if password is None or type(password) is not str:
            return False
        return self.__password == password
