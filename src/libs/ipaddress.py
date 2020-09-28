import re
import netaddr


class IPaddress:


    def __init__(self, ip = None):
        self.__address = None
        self.__cidr = None

        if ip != None:
            match = re.search('^([0-9\.]{7,15}|[0-9A-Fa-f\:]{5,39})(\/[0-9]{1,3})?$', ip.strip())
            if match:
                if match.group(1): self.__address = match.group(1)
                if match.group(2): self.__cidr = match.group(2)


    def version(self):
        if self.__address != None:
            if netaddr.valid_ipv4(self.__address) == True:
                return 'ipv4'
            elif netaddr.valid_ipv6(self.__address) == True:
                return 'ipv6'

        return False
