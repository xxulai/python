#-*- utf-8 -*-
class base(object):
    def __init__(self):
        print "I am base"
    
    def func(self):
        print "In father func"
    
    def func1(self):
        print "In father func1"

class Son(base):
    def __init__(self):
        print "I am Son calling my father"
        super(Son, self).__init__()
    
    def func(self):
        print "In Son func"
        super(Son, self).func()
        
    def func1(self):
        print "In Son func1"
        super(Son, self).func1()

#ambiguous call, raise MRO error
# Traceback (most recent call last):
  # File "multiinheritance.py", line 12, in ?
    # class ambiguousSon(base, Son):
# TypeError: Error when calling the metaclass bases
    # Cannot create a consistent method resolution
# order (MRO) for bases base, Son
#class ambiguousSon(base, Son):
#    def __init__(self):
#        print "I am ambiguousSon calling my father"
#        super(ambiguousSon, self).__init__()
#amSon = ambiguousSon()

class grandSon(Son):
    def __init__(self):
        print "I am grandSon calling my father"
        super(grandSon, self).__init__()
    
    def func(self):
        print "In grandSon func"
        super(grandSon, self).func()

#output
# I am grandSon calling my father
# I am Son calling my father
# I am base
gSon=grandSon()

# In grandSon func
# In Son func
# In father func
gSon.func()

class Son2(base):
    def __init__(self):
        print "I am Son2 calling my father"
        super(Son2, self).__init__()
    
    def func(self):
        print "In Son2 func"
        super(Son2, self).func()

class grandSon2(Son2, Son):
    def __init__(self):
        print "I am grandSon2 calling my father"
        super(grandSon2, self).__init__()
    
    def func(self):
        print "In grandSon2 func"
        super(grandSon2, self).func()
        
    def func1(self):
        print "In grandSon2 func1"
        super(grandSon2, self).func1()

# I am grandSon2 calling my father
# I am Son2 calling my father
# I am Son calling my father
# I am base
gSon2=grandSon2()

# In grandSon2 func
# In Son2 func
# In Son func
# In father func
gSon2.func()

# In grandSon2 func1
# In Son func1
# In father func
gSon2.func1()

class Sonobject(object):
    def __init__(self):
        print "I am Sonobject"
        
    def func(self):
        print "In Sonobject func"
        
class grandSon3(Sonobject, Son):
    def __init__(self):
        print "I am grandSon3 calling my father"
        super(grandSon3, self).__init__()
    
    def func(self):
        print "In grandSon3 func"
        super(grandSon3, self).func()
        
    def func1(self):
        print "In grandSon3 func1"
        super(grandSon3, self).func1()

# I am grandSon3 calling my father
# I am Sonobject        
gSon = grandSon3()
# In grandSon3 func         Sonobject is child of object, so only 1 level up?
# In Sonobject func
gSon.func()
# In grandSon3 func1   there is no func1 in Sonobject
# In Son func1
# In father func1
gSon.func1()

class grandSon4(Sonobject, Son):
    def __init__(self):
        print "I am grandSon4 calling my father"
        super(grandSon4, self).__init__()

# I am grandSon4 calling my father
# I am Sonobject
gSon4 = grandSon4()
#In Sonobject func
gSon4.func()        
       
class grandSon5(Son, Sonobject):
    def __init__(self):
        print "I am grandSon5 calling my father"
        super(grandSon5, self).__init__()

# I am grandSon5 calling my father
# I am Son calling my father
# I am base
gSon5 = grandSon5()
# In Son func
# In father func
gSon5.func()     

#composition
class Composition(object):
    def __init__(self):
        print "I am Composition"
        self.son=Son()
    
    def func(self):
        self.son.func()

#strong weak association
# Composition: Table and Table leg, once table is destroyed, table leg doesn't exist any more 
# Aggregation: Wheel and car, a wheel can still be useful once the car is destoryed
# I am Son calling my father
# I am base
comp=Composition()
# In Son func
# In father func
comp.func()
