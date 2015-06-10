def return_multi(sid):
	add=sid+sid
	mult=sid*sid
	divd=sid/sid
	return add, mult, divd

sid = int(raw_input("sid:? "))
print "multi return add: %d, times: %d, divide: %d" % return_multi(sid)