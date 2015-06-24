def computepay(h,r):	
	print "In computepay",'h=', h,'r=', r		
	if h <= 40:
		p = r * h
		return p
	else:
		p = r * 40 + (r * 1.5 * (h - 40))
		return p
try:
	inp = raw_input("Enter Hours:")
	hrs = float(inp)
	inp = raw_input("Enter Rate:")	
	rate = float(inp)		
except:
	print "Error, please enter a numeric value"
	quit()

print "In the main code", hrs, rate 
pay = computepay(hrs,rate)
print "Pay=", pay
