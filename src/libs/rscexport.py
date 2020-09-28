import os


class RscExport:


    def __init__(self, resource = None):
        self.__resource = resource
        self.__directory = './exports/'


    def __write_ipaddresslist(self):
        if self.__data and self.__resource:
            for version, tags in self.__data.items():
                for tag, ips in tags.items():
                    with open(self.__directory + self.__resource['prefix'] + '-' + version + '-' + tag + '.rsc', 'w') as file:
                        file.write('# ' + self.__resource['description'] + "\n")
                        file.write('/' + version.replace('ipv4', 'ip') + ' firewall address-list' + "\n")
                        file.write('remove [find list=' + self.__resource['prefix'] + '-' + version + '-' + tag + ']' + "\n")
                        for ip in ips:
                            file.write('add list=' + self.__resource['prefix'] + '-' + version + '-' + tag + ' address=' + ip + ' comment="' + self.__resource['description'] + '"' + "\n")


    def __makedir(self):
        if self.__directory != None:
            if not os.path.exists(self.__directory):
                os.makedirs(self.__directory)


    def __write(self):
        self.__makedir()
        if self.__resource['export'] == 'addresslist':
            self.__write_ipaddresslist()
            return True
        else:
            return False



    def export(self, data, directory = None):
        if directory != None:
            self.__directory = directory
        self.__data = data
        return self.__write()