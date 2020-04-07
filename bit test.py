qos_list = []
with open("f.txt", "rb") as f:
    byte = f.read(1)
    while byte:
        qos_list.append((ord(byte) & 192)>>6)
        qos_list.append((ord(byte) & 48)>>4)
        qos_list.append((ord(byte) & 12)>>2)
        qos_list.append((ord(byte) & 3))
        byte = f.read(1)
f.close()
f = open('o.txt', 'wb')
for b in range(0, len(qos_list), 4):
    byte = qos_list[b]<<6 | qos_list[b+1]<<4 | qos_list[b+2]<<2 | qos_list[b+3]
    f.write(chr(byte))
f.close()    

    

