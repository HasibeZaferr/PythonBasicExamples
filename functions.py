# -*- coding: utf-8 -*-

def changeme( mylist ):
   print ("Values inside the function before change: ", mylist) #10,20,30 yazdırır
   mylist[2]=50
   print ("Values inside the function after change: ", mylist) #10,20,50 yazdırır
   return


mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist) # 10,20,50 yazdırır


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
str='Hello World!'
printme(str)


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme( str = "My string")


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )


# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )