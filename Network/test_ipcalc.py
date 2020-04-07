import ipcalc

def test_valid_ip_addr():
	print('Trying valid IP address as string',end='...')
	ip = '192.168.1.1'
	assert ipcalc.is_valid_ip_addr(ip) == True
	print('Passed.')

	print('Trying random string ',end='...')
	ip = 'xxxxxx'
	assert ipcalc.is_valid_ip_addr(ip) == False
	print('Passed.')

	print('Trying valid IP address as tuple of ints',end='...')
	ip = (192,168,0,1)
	assert ipcalc.is_valid_ip_addr(ip) == True
	print('Passed.')

	print('Trying tuple with string',end='...')
	ip = ('192','168','0','1')
	assert ipcalc.is_valid_ip_addr(ip) == False
	print('Passed.')

	print('Trying valid IP address as list of ints',end='...')
	ip = [192,168,0,1]
	assert ipcalc.is_valid_ip_addr(ip) == True
	print('Passed.')
	
	print('Trying int',end='...')
	ip = 192
	assert ipcalc.is_valid_ip_addr(ip) == False
	print('Passed.')
	
	print('Trying float',end='...')
	ip = 192.168
	assert ipcalc.is_valid_ip_addr(ip) == False
	print('Passed.')
	
	
		
	assert ipcalc.is_valid_ip_addr('192.168.0.1') == False
	#assert ipcalc.is_valid_ip_addr('192.168.0.x') == False
	#assert ipcalc.is_valid_ip_addr('192.168.x.1') == True
	#assert ipcalc.is_valid_ip_addr('1.x.0.1') == False
	#assert ipcalc.is_valid_ip_addr('x.168.0.1') == False