'''
	Name:		ipcalc
	Version:	0.1
	Description:
		ipcalc module provides a set of commonly used operations of IPv4 address.
		The current set includes:
			network_addr - 
'''
    
	def network_addr(self):
        o = self.addr
        m = self.mask
        return (o[0] & m[0], o[1] & m[1], o[2] & m[2], o[3] & m[3])


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
