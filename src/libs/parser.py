import csv
import urllib3

from libs.ipaddress import IPaddress


class Parser:


    def __init__(self, resource = None):
        self.__resource = resource
        self.__data = None


    def __as_turris_csv(self, data):
        list = {}
        for cols in csv.reader(data.split('\n'), delimiter=','):
            if 2 < len(cols):
                version = IPaddress(cols[0]).version()
                if version != False:
                    if version not in list:
                        list[version] = {}
                        list[version]['all'] = []
                    list[version]['all'].append(cols[0])
                    tags = cols[2].split(',')
                    for tag in tags:
                        if tag not in list[version]:
                            list[version][tag] = []
                        list[version][tag].append(cols[0])

        return list if len(list) > 0 else False


    def __as_sentinel_csv(self, data):
        list = {}
        for cols in csv.reader(data.split('\n'), delimiter=','):
            if 1 < len(cols):
                version = IPaddress(cols[0]).version()
                if version != False:
                    if version not in list:
                        list[version] = {}
                        list[version]['all'] = []
                    list[version]['all'].append(cols[0])
                    tags = cols[1].split(',')
                    for tag in tags:
                        if tag not in list[version]:
                            list[version][tag] = []
                        list[version][tag].append(cols[0])

        return list if len(list) > 0 else False


    def __as_simple_textfile(self, data):
        list = {}
        for row in map(str.strip, data.split('\n')):
            version = IPaddress(row).version()
            if version != False:
                if version not in list:
                    list[version] = {}
                    list[version]['all'] = []
                list[version]['all'].append(row)

        return list if len(list) > 0 else False


    def __as_tor_exits(self, data):
        list = {}
        for row in data.split('\n'):
            cols = row.split(' ')
            if 1 < len(cols):
                version = IPaddress(cols[1]).version()
                if version != False:
                    if version not in list:
                        list[version] = {}
                        list[version]['all'] = []
                    list[version]['all'].append(cols[1])

        return list if len(list) > 0 else False


    def __download(self, url):
        http = urllib3.PoolManager()
        resp = http.request('GET', url)
        if resp.status == 200:
            return resp.data.decode('utf-8')
        else:
            return False


    def __parse(self):
        if self.__resource != None and self.__data != False:
            if self.__resource['parser'] == 'turris_csv':
                return self.__as_turris_csv(self.__data)
            elif self.__resource['parser'] == 'sentinel_csv':
                return self.__as_sentinel_csv(self.__data)
            elif self.__resource['parser'] == 'simple_textfile':
                return self.__as_simple_textfile(self.__data)
            elif self.__resource['parser'] == 'tor_exits':
                return self.__as_tor_exits(self.__data)
            else:
                return None
        else:
            return False


    def get(self, resource = None):
        if resource != None:
            self.__resource = resource
        self.__data = self.__download(self.__resource['url'])
        return self.__parse()