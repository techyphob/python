#import math, sys

class ipv4(object):
    '''
        No point documenting this, I'm just making it up as I go along
        and of course I'll remember what I meant when I come back to it.

        The original concept was to store str and tuple representation of the IP
        address. This may not be the best approach and could cause unnessary code complexity.

        Although this does allow for the IP address to be presented in multiple methods
    '''
    #print (sys.argv)
    def __init__(self, addr, mask_len):
        if self.isValidIPAddr(addr):# and self.isValidSubnetMask(mask_len):
            self.addr = addr
            self.mask_len = mask_len
        else:
            print('Default IP address and mask set!')
            self.addr = '0.0.0.0'
            self.mask_len = 0

    @property
    def addr(self) -> str:
        return self._addr

    @addr.setter
    def addr(self, new_addr) -> None:
        try:
            if type(new_addr) == str:
                self._addr = tuple(map(int,new_addr.split('.')))
            elif type(new_addr) == tuple:
                self._addr = new_addr
            elif type(new_addr) == list:
                self._addr = tuple(new_addr)
        except Exception as e:
            print(e)

    @property
    def mask_len(self):
        return self._mask_len

    @mask_len.setter
    def mask_len(self, new_len):
        self._mask_len = new_len

    @property
    def mask(self):
        return self.subnetMask(self.mask_len)

    @property
    def network_addr(self):
        o = self.addr
        m = self.mask
        return (o[0] & m[0], o[1] & m[1], o[2] & m[2], o[3] & m[3])

    @property
    def broadcast_addr(self):
        o = self.addr
        m = self.mask
        return (o[0] | (256 + ~m[0]), o[1] | (256 + ~m[1]), o[2] | (256 + ~m[2]), o[3] | (256 + ~m[3]))

    def isValidIPAddr(self, addr):
        if type(addr) == str:
            try:
                addr = tuple(map(int,addr.split('.')))
            except Exception as e:
                return false
        if (type(addr) ==  list or type(addr) == tuple) and len(addr) == 4 and all(isinstance(o,int) for o in addr) and all(-1 < o < 256 for o in addr):
            if addr[0] != 127:
                return True
        return False  

    def isValidSubnetMask(self, mask):
        '''
    this probably needs rewriting
        '''
        if type(mask) == str:
            try:
                mask = map(int,mask.split('.'))
            except Exception as e:
                return False
        if type(mask) ==  list or type(mask) == tuple:
            if all(isinstance(o,int) for o in mask) and len(mask) == 4 and all(-1 < o < 256 for o in mask) and math.log(256-mask[next (i for i, e in enumerate(mask) if e < 255)],2).is_integer():
                if  len(mask[next (i for i, e in enumerate(mask) if e < 255) + 1:]) == 0 or ([0] * (3 - next (i for i, e in enumerate(mask) if e < 255)) == mask[next (i for i, e in enumerate(mask) if e < 255) + 1:]):
                    return True
                return False
            return False
        return False

    def subnetMask(self, mask_len):
        rtr_mask = [0,0,0,0]
        i = 0
        while mask_len > 8:
            rtr_mask[i] = 255
            mask_len = mask_len - 8
            i +=  1
        rtr_mask[i] = 256 - 2**(8-mask_len)
        return rtr_mask

    def isBroadcastAddr(self):
        return self.broadcast_addr == self.addr

    def isNetworkAddr(self):
        return self.network_addr == self.addr

    @property
    def addr2bin(self):
        rtr_str = ''
        for o in self.addr:
            rtr_str = rtr_str + str(self.bytePad(bin(o)[2:])) + "."
        return rtr_str[0:-1]

    @property
    def mask2bin(self):
        rtr_str = ''
        for o in self.mask:
            rtr_str = rtr_str + str(self.bytePad(bin(o)[2:])) + "."
        return rtr_str[0:-1]

    @property
    def addr2str(self):
        return '.'.join(map(str, self.addr))

    @property
    def mask2str(self):
        return '.'.join(map(str, self.mask))

    def bytePad(self, bits):
        return '0' * (8 - len(bits)) + bits
    

ip = ipv4("192.168.1.1",30)
#ip = ipv4([192,168,1,1],30)
#ip = ipv4((192,168,0,1),30)


