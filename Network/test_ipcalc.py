import ipcalc

def test_IPtest():
	#test if str is accepted 
	ip = '192.168.1.1'
	assert ipcalc.isValidIPAddr(ip) == True
	#Test if Tuple is accepted
	ip = (192,168,0,1)
	assert ipcalc.isValidIPAddr(ip) == True
	#Test if Dict is accepted
	ip = [192,168,0,1]
	assert ipcalc.isValidIPAddr(ip) == True
	
	
	#assert ipcalc.isValidIPAddr('192.168.0.1') == True
	#assert ipcalc.isValidIPAddr('192.168.0.x') == False
	#assert ipcalc.isValidIPAddr('192.168.x.1') == True
	#assert ipcalc.isValidIPAddr('1.x.0.1') == False
	#assert ipcalc.isValidIPAddr('x.168.0.1') == False