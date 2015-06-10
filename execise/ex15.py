from sys import argv

script, filename=argv

txt=open(filename)
print "File %s content: " %filename
print txt.read()

print "Type Name again"
filename=raw_input("> ")
print "File %s content: " %filename
txt=open(filename)
print txt.read()