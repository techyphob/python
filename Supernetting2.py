from math import log

def NetAddr(i: str, m: str) -> str:
    i_lst = i.split('.')
    m_lst = m.split('.')
    r_lst = []
    for j in range (0,4):
        r_lst.append(int(i_lst[j]) & int(m_lst[j]))
    return '.'.join(map(str,r_lst))

def BcastAddr(i: str, m: str) -> str:
    i_lst = i.split('.')
    m_lst = m.split('.')
    r_lst = []
    for j in range (0,4):
        r_lst.append(int(i_lst[j]) | (256 + ~int(m_lst[j])))
    return '.'.join(map(str,r_lst))

def SubnetMask(ml: int) -> str:
    sm = [0, 0, 0, 0]
    if (0 <= ml < 33):
        i = 0
        while ml > 8:
            sm[i] = 255
            i = i + 1
            ml = ml - 8
        sm[i] = 256 - 2**(8 - ml)
    return '.'.join(map(str,sm))

def MaskLength(mask: str) -> int:
    ml = 0
    mask = map(int,mask.split('.'))
    for o in mask:
        ml = ml + 8-log(256-o,2)
    return int(ml)
    
def FindMask(NetAddr1: str, NetAddr2: str):
    NetAddr1 = NetAddr1.split('.')
    NetAddr2 = NetAddr2.split('.')
    ml = 0
    for i in range (0,4):
        xor_value = int(NetAddr1[i])^int(NetAddr2[i])
        if (xor_value) == 0:
            ml = ml + 8
        else:
            for x in range (0,8):
                if (256-2**x &  xor_value) == 0:
                    ml = ml + (8-x)
                    break
            break
    return ml

ip1 = '192.168.1.0'
ip2 = '192.168.0.0'
print (NetAddr(ip1,SubnetMask(28)))
print (BcastAddr(ip1,SubnetMask(28)))
print (FindMask(ip1,ip2))

#
# The script needs to check:
#   is the route valid in terms of the correct mask and network address
#   is the ip address valid i.e. 4 dotted decimal values lying in the range 0-255
#   is the mask valid i.e. between 0 and 30


#with open('routes.txt','r') as inf:
#    s = inf.read()
#inf.close()
#
#routes_list = list(r.split('/') for r in s.split('\n'))
#
#ml = 32
#for r in range(0,len(routes_list)-1):
#    new_ml = FindMask(CS2L(routes_list[r][0]),CS2L(routes_list[r+1][0]))
#    if new_ml > int(routes_list[r][1]):
#        new_ml = int(routes_list[r][1])
#    elif new_ml > int(routes_list[r+1][1]):
#        new_ml = int(routes_list[r+1][1])
#    if new_ml < ml:
#        ml = new_ml
    
# need to work out the base address - should just be a matter of taking any of the previous routes and calculating the net and bcast addrs

#r = routes_list[0]
#print ("Base address:\t" + str(NetAddr(r[0],CL2S(SubnetMask(ml)))))
#print ("Netmask:\t" + str(SubnetMask(ml)))


    
#ip1 = '192.168.10.0'
#ip2 = '192.168.10.23'
#m1 = '255.255.255.0'
#m2 = '255.255.255.252'
#m = FindMask(NetAddr(ip1,m1),NetAddr(ip2,m2))
#new_mask = '.'.join(map(str,SubnetMask(m)))
#print(new_mask)
#print (NetAddr(ip1,new_mask))
#print (NetAddr(ip2,new_mask))
#print (BcastAddr(ip1,new_mask))
#print (BcastAddr(ip2,new_mask))
