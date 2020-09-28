import os
import json

from tabulate import tabulate


class Resource:


    def __init__(self, file = 'resources.json'):
        self.__file = os.path.dirname(os.path.abspath(__file__)) + '/../' + file
        self.__list = self.__load()


    def __load(self):
        if os.path.isfile(self.__file):
            with open(self.__file) as file:
                data = json.load(file)
                if data:
                    return data
        return None


    def help(self):
        if self.__list != None:
            table = []
            for index, item in enumerate(self.__list):
                table.append([str(index), item['id'], item['description'], item['export']])
            return tabulate(table, headers=['ID', 'Resource', 'Description', 'Type'])
        return False


    def get(self, id = None):
        if self.__list != None:
            for index, item in enumerate(self.__list):
                if item['id'] == id or str(index) == id:
                    return item
            return None
        else:
            return False
