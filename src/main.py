#!/usr/bin/python3

import argparse
import routeros_api
from libs.parser import Parser
from libs.resource import Resource
from libs.rscexport import RscExport


def arguments():
    arguments = argparse.ArgumentParser()
    arguments.add_argument('-e', '--export', action='store_true', default=False, help='')
    arguments.add_argument('-s', '--set', action='store_true', default=False, help='')
    arguments.add_argument('-d', '--directory', action='store', default=None, help='')
    arguments.add_argument('-r', '--resource', action='store', default=None, help='')
    arguments.add_argument('-a', '--ipaddress', action='store', default=None, help='')
    arguments.add_argument('-c', '--port', action='store', default=None, help='')
    arguments.add_argument('-u', '--user', action='store', default=None, help='')
    arguments.add_argument('-p', '--password', action='store', default=None, help='')
    return arguments.parse_args()


if __name__ == '__main__':
    argument = arguments()

    if argument.resource == None:
        resource = Resource().help()
        if resource != False:
            print("\n" + resource + "\n\n" + 'Select the resource you want to export. For more information use the --help parameter.' + "\n")
        else:
            print('File not found')
    else:
        resource = Resource().get(argument.resource)
        if resource == False:
            print('File not found')
        elif resource == None:
            print('Resource not found')
        else:
            data = Parser(resource).get()
            if data == False:
                pass
            elif data == None:
                pass
            else:
                if argument.export == True:
                    result = RscExport(resource).export(data, argument.directory)
                    if result == True:
                        print('Export OK')
                    else:
                        print('Export ERROR')
                if argument.set == True:
                        print('N/A')


