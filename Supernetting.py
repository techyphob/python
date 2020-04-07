#   routes and mask now read from file in x.x.x.x/xx format
#   need to check mask lengths the logic of the code will create a smaller mask if the possible
#
#
def CS2L(i):
    if type(i) == str:
        return i.split('.')
    else:
        return 'error'

def CL2S(i):
    if type(i) == list:
        return '.'.join(map(str,i))
    else:
        return 'error'
    
def NetAddr(i,m):
#input str dotted formats for both 
    i_lst = i.split('.')
    m_lst = m.split('.')
    r_lst = []
    for j in range (0,4):
        r_lst.append(int(i_lst[j]) & int(m_lst[j]))
    return r_lst

def BcastAddr(i,m):
#input str dotted format
    i_lst = i.split('.')
    m_lst = m.split('.')
    r_lst = []
    for j in range (0,4):
        r_lst.append(int(i_lst[j]) | (256 + ~int(m_lst[j])))
    return r_lst

def SubnetMask(ml: int):
#converts mask length to dotted format
    sm = [0, 0, 0, 0]
    if (0 <= ml < 33):
        i = 0
        while ml > 8:
            sm[i] = 255
            i = i + 1
            ml = ml - 8
        sm[i] = 256 - 2**(8 - ml)
    return sm

def FindMask(NetAddr1,NetAddr2):
# takes 2 network addresses as arrays
# need to expand this to allow for dotted format
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

#Function IsInSubnet(ByVal ip As String, ByVal sml As Integer, ByVal subnet_ip As String, ByVal subnet_sml As Integer)
#    'logic
#    'If the ip address has the same base address as the subnet using the
 #   'If the test mask length is larger than the subnet then it cannot be contained in the subnet    
    #ret_value = False
    #If sml >= subnet_sml Then
    #    If SubnetAddr(ip, subnet_sml) = SubnetAddr(subnet_ip, subnet_sml) Then ret_value = True
    #End If
    #IsInSubnet = ret_value
#End Function


#
# The script needs to check:
#   is the route valid in terms of the correct mask and network address
#   is the ip address valid i.e. 4 dotted decimal values lying in the range 0-255
#   is the mask valid i.e. between 0 and 30


with open('routes.txt','r') as inf:
    s = inf.read()
inf.close()

routes_list = list(r.split('/') for r in s.split('\n'))

ml = 32
for r in range(0,len(routes_list)-1):
    new_ml = FindMask(CS2L(routes_list[r][0]),CS2L(routes_list[r+1][0]))
    if new_ml > int(routes_list[r][1]):
        new_ml = int(routes_list[r][1])
    elif new_ml > int(routes_list[r+1][1]):
        new_ml = int(routes_list[r+1][1])
    if new_ml < ml:
        ml = new_ml
    
# need to work out the base address - should just be a matter of taking any of the previous routes and calculating the net and bcast addrs

r = routes_list[0]
print ("Base address:\t" + str(NetAddr(r[0],CL2S(SubnetMask(ml)))))
print ("Netmask:\t" + str(SubnetMask(ml)))


    
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
