import math, sys

class ipv4(object):
    '''
        No point documenting this, I'm just making it up as I go along
        and of course I'll remember what I meant when I come back to it. 
    '''
    print (sys.argv)
    def __init__(self, addr, mask_len):
        if self.isValidIPAddr(addr):
            if type(addr) == str:
                self.addr = addr
                self.octets = tuple(map(int,self.getAddr().split('.')))
            elif type(addr) == tuple:
                self.octets = addr
                self.addr = self.dotted(self.octets)
        else:
            print('Invalid IP address')
            self.addr = '0.0.0.0'
            self.octets = (0,0,0,0)

        self.mask_len = mask_len
        self.subnet_mask = tuple(self.__setSubnetMask__())
        self.network_addr = self.__setNetworkAddr__()
        self.broadcast_addr = self.__setBroadcastAddr__()
    
    def getAddr(self):
        return self.addr
    def getMaskLen(self):
        return self.mask_len
    def getOctets(self):
        return self.octets
    def getOctet(self, o):
        return self.getOctets()[o]
    def getSubnetMask(self):
        return self.subnet_mask
    def getNetworkAddr(self):
        return self.network_addr
    def getBroadcastAddr(self):
        return self.broadcast_addr

    def isValidIPAddr(self, addr):
        if type(addr) == str:
            try:
                addr = list(map(int,addr.split('.')))
            except:
                return False
        if (type(addr) ==  list or type(addr) == tuple) and len(addr) == 4 and all(isinstance(o,int) for o in addr) and all(-1 < o < 256 for o in addr):
            if addr[0] != 127:
                return True
        return False  

    def isValidSubnetMask(self, mask):
        if type(mask) == str:
            try:
                mask = map(int,mask.split('.'))
            except:
                return False
#        if (type(mask) ==  list or type(mask) == tuple) and all(isinstance(o,int) for o in mask) and len(mask) == 4 and all(-1 < o < 256 for o in mask) and math.log(256-mask[next (i for i, e in enumerate(mask) if e < 255)],2).is_integer() and (len(mask[next (i for i, e in enumerate(mask) if e < 255) + 1:]) == 0 or ([0] * (3 - next (i for i, e in enumerate(mask) if e < 255)) == mask[next (i for i, e in enumerate(mask) if e < 255) + 1:])):
#            return True
#        return False  
        if type(mask) ==  list or type(mask) == tuple:
            if all(isinstance(o,int) for o in mask) and len(mask) == 4 and all(-1 < o < 256 for o in mask) and math.log(256-mask[next (i for i, e in enumerate(mask) if e < 255)],2).is_integer():
                if  len(mask[next (i for i, e in enumerate(mask) if e < 255) + 1:]) == 0 or ([0] * (3 - next (i for i, e in enumerate(mask) if e < 255)) == mask[next (i for i, e in enumerate(mask) if e < 255) + 1:]):
                    return True
                return False
            return False
        return False
    def isBroadcastAddr(self):
        return self.getBroadcastAddr() == self.getOctets()
    def isNetworkAddr(self):
        return self.getNetworkAddr() == self.getOctets()

    def printBinAddr(self):
        rtr_str = ''
        for o in self.getOctets():
            rtr_str = rtr_str + str(self.bytePad(bin(o)[2:])) + "."
        return rtr_str[0:-1]
    def printBinMask(self):
        rtr_str = ''
        for o in self.getSubnetMask():
            rtr_str = rtr_str + str(self.bytePad(bin(o)[2:])) + "."
        return rtr_str[0:-1]
    def printDottedAddr(self):
        as_str = list(map(str, self.getOctets()))
        return as_str[0] + '.' + as_str[1] + '.' + as_str[2] + '.' + as_str[3]
    def printDottedMask(self):
        as_str = map(str, self.getSubnetMask())
        return as_str[0] + '.' + as_str[1] + '.' + as_str[2] + '.' + as_str[3]


    def bytePad(self, bits):
        return '0' * (8 - len(bits)) + bits
        
    def __setSubnetMask__(self):
        rtr_mask = [0,0,0,0]
        mask_len = self.getMaskLen()
        i = 0
        while mask_len > 8:
            rtr_mask[i] = 255
            mask_len = mask_len - 8
            i +=  1
        rtr_mask[i] = 256 - 2**(8-mask_len)
        return rtr_mask

    def __setNetworkAddr__(self):
        o = self.getOctets()
        m = self.getSubnetMask()
        return (o[0] & m[0], o[1] & m[1], o[2] & m[2], o[3] & m[3])

    def __setBroadcastAddr__(self):
        o = self.getOctets()
        m = self.getSubnetMask()
        return (o[0] | (256 + ~m[0]), o[1] | (256 + ~m[1]), o[2] | (256 + ~m[2]), o[3] | (256 + ~m[3]))

    def show(self):
        print ('{}\n{}\n{}\n{}\n{}\n'.format(ip.getOctets(),ip.getMaskLen(),ip.getSubnetMask(),ip.getNetworkAddr(),ip.getBroadcastAddr())        )

ip = ipv4("192.168.1.1",30)

'''
mask = (255,255,128,0)
next ((i for i, x in enumerate(mask) if x != 255),3)
mask[0:j]

all(o == 255 for o in mask[0:j])


'''

