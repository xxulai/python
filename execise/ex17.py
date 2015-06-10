from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s" %(from_file, to_file)

in_data=open(from_file).read()
print "The input file is %d bytes long" %len(in_data)

print "Output exists? %r" %exists(to_file)
print "Press any key to continue..."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Copy done"
out_file.close()
