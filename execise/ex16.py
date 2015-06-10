from sys import argv

script, filename=argv

print "truncate file first"
raw_input("?")
print "truncating file..."
target=open(filename, 'w')
target.truncate()

print "Now input 2 new lines"
line1=raw_input("line 1: ")
line2=raw_input("line 2: ")

target.write(line1+"\n"+line2+"\n")

target.close()