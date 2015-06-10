def print_2(*args):
	arg1, arg2=args
	print "arg1 %s, arg2 %s" %(arg1, arg2)
	
def print_2_again(arg1, arg2):
	print "arg1 %s, arg2 %s" %(arg1, arg2)

def print_1(arg1):
	print "arg1 %s" %(arg1)
	
def print_none():
	print "no args"
	
print_2("Lai", "Xu")
print_2_again("Lai", "Xu")
print_1("Lai")
print_none()