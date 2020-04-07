def dotted(addr_lst):
    as_str = map(str, addr_lst)
    return as_str[0] + '.' + as_str[1] + '.' + as_str[2] + '.' + as_str[3]


input_addr = raw_input('Input IP Network Address: ') or '192.168.17.18'
input_mask = raw_input('Enter mask Length [24]: ') or 24

octets = map(int,(input_addr.split('.')))
subnet_mask = [0,0,0,0]
ml = input_mask
i = 0
while ml > 8:
    subnet_mask[i] = 255 
    ml = ml - 8
    i=i+1
subnet_mask[i]= 256 - 2**(8-ml)

network_addr = (octets[0] & subnet_mask[0], octets[1] & subnet_mask[1], octets[2] & subnet_mask[2], octets[3] & subnet_mask[3])
broadcast_addr = (octets[0] | (256 + ~subnet_mask[0]), octets[1] | (256 + ~subnet_mask[1]), octets[2] | (256 + ~subnet_mask[2]), octets[3] | (256 + ~subnet_mask[3]))

print '{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}'.format('IP Address:', octets, 'Subnet Length:', input_mask, 'Subnet Mask', subnet_mask, 'Network Address:', network_addr, 'Broadcast Address:', broadcast_addr)
print '\n'
print '{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}\n{:<25}{:<20}'.format('IP Address:', dotted(octets), 'Subnet Length:', input_mask, 'Subnet Mask', dotted(subnet_mask), 'Network Address:', dotted(network_addr), 'Broadcast Address:', dotted(broadcast_addr))
print '\n'
print '{:20}{:20}{:20}\n{:20}{:20}{:20}'.format('NETWORK_NUMBER','FIRST_OCTET_BINARY','FIRST_OCTET_HEX',dotted(network_addr),bin(octets[0]),hex(octets[0]))
print '{:20}{:20}{:20}{:20}\n{:20}{:20}{:20}{:20}'.format('first_octet','second_octet','third_octet','fourth_octet',bin(octets[0]),bin(octets[1]),bin(octets[2]),bin(octets[3]))
    
