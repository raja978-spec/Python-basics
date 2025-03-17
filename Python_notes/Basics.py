#                DATA TYPES
#          PRIMITIVE DATATYPES
'''
 Primitive data types are the basic data type. 

 * Integer 
 * Float
 * String
 * Bool
'''
#        NON PRIMITIVE DATA TYPES
'''
 This all are called as built in datatypes.

 * Array
 * List       - * General purpose widely used datastructure,
                * Grow and shrink size as you needed,
                * sequence(ordered) data type,
                * Slice can be done.
                * Muttable data type

 * Tuple      - * Immutable it has index but can't change values once it is assigned and can't
                  add new values, but you can delete whole
                  tuple with del keyword
                * But you can concodinate two tuples, 
                * ordered data type
                * Slice can be done.
                * Tuple can be used as dict's key

 * Set        - * Takes unique value, hasn't index
                * unordered data type 
                * used in union,intersection
                * Can't perform slice operations
                * Muttable data type, you can add new elements
                * But can't change element one it is assigned

 * Dictionary - * key and value pair, 
                * unordered data type,
                * can't contain duplicate keys, but can contain
                  duplicate values.
                * Muttable 
'''


#          KEYWORD PACKAGE
'''
from keyword import kwlist
print(kwlist)

returns the dictionary of all keywords in python
'''

#         USERDEFINED DATA TYPES
'''
 * Stack
 * Queue
 * LinkedList
 * Tree
'''

#             BENEFITS OF PYTHON
'''
 * General purpose langauage
 * Easily readable
 * Platform intependant
 * Supports third party modules 
 * Code reuseability
''' 
#               TYPE CHECKING
'''
 Type checking done in two ways
 
 1. Static- Data types are checked before execution
 2. Dynamic - Data types are checked during execution
 
 * Python know it's variable type in runtime, this is called
   dynamically typed language.
 
 * However java,c,c++ basically knows their variables
   during complie time.
'''
#                    PEP 8
'''
 PEP 8 (Python enhancement protocol) is a document that helps to build reabable 
 python code
'''
#               MEMORY MANAGEMENT
'''
 * All python variables are stored in Private Heap
   Space.
 * Programmres doesn't access the space.
 * Python has built in garbage collection to use
   unused storage space.
'''
#                 NAME SPACE
'''
 In python name space used to create unique object names
 for function and class. Name space is nothing but indendation.
 There are 3 types of name_space
  1. Local namespace  - A name that is created inside the current file's function.
  2. Global namespace - It is also a function's name that is created in various 
                        python file, This global namespace is created while import a
                        python module.
  3. Built-in namespace   
'''
#                 SCOPE RESOLUTATION            
'''
 # global variable can't be changed inside the function, this is called scope resolutation
 # Here python knows outside function xy is global variable 
 # With the help of indentations meanwhile inside xy treated as local variables
 # This is called namespacing and this is also called as scope resolutation
 
 xy = 12 
 def func():
   xy = 13 # It doesn't overwrite
   print(xy)
 print(xy)
 func()
'''
#                    SCOPE
'''
 * A scope is a collection of objects inside a function  or class.
 * scope also has namespace
 Type of scopes
  1. Local Scope    - A variable created inside function, this scope the variable is going to end
                      when the function is end, You can't use this variables outside the function
  2. Global Scope   - A variable or object that is create inside a class, It is accessiable for all local and global functions.
  3. Built-in Scope -  Inbuilt python keywords are considerd as built-inscope 
                       (for,if,elif,try)
  4. Enclosing      - A function that is created inside the function, you can't access outside of that function

  NAMING VARIABLE

  Don't use outer_function's object name in inner function's object
'''

 #                  GLOBAL KEYWORD

'''
 y = "python " # global scope variable

 def Outterfun():
    z = 123 # local variable
    global x # global helps to access inner function's function on outside 
    x= 'Hello ' 
    def innerfunc(): # Enclosing scope
      print('Welcome ')
    innerfunc()

 Outterfun() # Without calling this function
             # program doesn't know the values of x
             # if we want to access a globally assigned 
             # variables inside function the
             # function should be called.
 print(x+ y+'Programmers')
 
 The below example will give you error
 
 
def func(a):
    global x
    x="hello"
    print(a,x)
print(x)
'''

 #                NON-LOCAL KEYWORD
 # Local variabel helps to override outter function's object
'''
 def func1():
  
  xx = 'helo'
  def func2():

    nonlocal xx # Overridies first function's object
    xx = "Hai"
    print(xx)

  func2()
  print(xx)

 func1()
'''  

#                   DECORATORS
'''
 PRENEEDS :
 * Before going to do Decorations you need to know about 
    1. Nested functions
    2. Function returns another function

 * Decorator Helps to add functionality for existing function without changing the structure 
   of the function.
 * And also helps add functionality in class
                       
 def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

 # decorator function to split words
 def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper

 @splitter_decorator	# this is executed next
 @lowercase_decorator	# this is executed first
 def hello():
    return 'Hello World'
 print(hello())
'''
#                  ABOUT FUNCTIONS
'''
 * Functions can be stored into a variable
 * Functions can be passed as arguments to another function
 * Functions can return another function
'''
#                  PIP AND MODLE
'''
 PIP is the package manager for python, Helps to 
 install packages on your project
  
  * Collection of functions are called module.
  * There are 2 type of module
    
    1. Built in modules - pre installed
    2. External modules - Need to be install using pip.
'''   
#              SET AND LIST COMPREHENSION
'''
 Helps to do reduced code typing  

 Set = {x:x**2 for x in range(5)}
 print(Set)
 
 Take more than one tuple value in List
 List = [(x,y) for x in range(10) for y in range(5)]
 print(List)


 a = [1, 2, 3]
 b = [7, 8, 9]

 [(x + y) for (x,y) in zip(a,b)]  # parallel iterators
 # output => [8, 10, 12]
'''
#                 FROOZEN SET 
'''
 * In normal set we can add and remove elements, but
   frozenset has no module to support add and remove
   operations.

 * we can do only set operations

 Set = {12,3,4,55,6}
 Frozen = frozzenset(Set)
 Frozen.add(22) # Raises error
'''

#                     SET UPDATIONS FUNCTIONS
'''
We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
'''

#                  LAMBDA FUNCTION
'''
 * Lambda is a anonymous function, it takes many
   number of argument and returns one expression

  m = lambda a,b : a+b
  print(m("Helo","Hai"))
  
'''
#                 ISINSTANCE
'''
 # helps to check data types
 num = 25
 print(isinstance(25,int))
'''

#                 COPY IN PYTHON
'''
 # = symbol is not used for copy of a variable.
 # It creates a bridge between two variables.
 # Python has copy module to copy objects
 # It has two type of function
  1. ShallowCopy - Added elements will be refelceted on
                   parent's list. But we can't replace
                   the orginial items into's parents list.
  2. DeepCopy - We can append and replace items, but
                all the changes will not be reflected on parent's
                list.


 from copy import copy,deepcopy

 # Shallow copy


 List = [1,[2,3],4]
 List1=copy(List)
 print("List1: ",List1)
 List1[1].append(5) # This will reflect on List
 List1[0]=7 # this will not reflect
 print("List1: ",List1)
 print("List: ",List)

 # Deep copy

 List=[1,[2,3],4]
 List1=deepcopy(List)

 # All this changes will not reflect in List
 
 List1[0]=7
 List1[1].append(5)
 print("List1:",List1)
 print("List:",List)
'''

#             DIFFERENCE BETWEEN REMOVE AND POP
'''
 * Remove moves the specified items.
 * Pop deletes specified index items.
 * del() also delete's the specified index item.
'''

#                 XRANGE AND RANGE
'''
 * xrange does the same thing the range function
 * The only difference between this two is xrange return's object
   and range returns list of specified integer
 * xrange was used in python2 versions.
'''
#                MODULES AND PACKAGES
'''
 * Collection of module is called package.
 * Collection of functions are called modules.
'''
#               CONSTRUCTOR AND __str__
'''
 * Constructor  helps to take argument when the object is created.
 * __str__ helps to take's string arguments, it returns only string.

 class add:
    def __init__(self,Name):
        self.name = Name
    def __str__(self):
        return self.name
 obj = add
 print(obj("Raja"))
'''
#        GLOBAL,PROTECTED,PRIVATE ATTRIBUTE
'''
 GLOBAL OR PUBLIC:
 
 It is accessed by all the place of the program.
 PROTECTED:

 * In python you can create protected variable
  by specifying single underscore
 * They can accessed by inside and inherited class.

 class Shape:
  def __init__(self,length,breadth):
    self._length = length
    self._Breadth = breadth
  def DisplayShape(self):
    print("Length is: ",self._length,"\n","Breadth is: ",self._Breadth)
 class Rectangle(Shape):
  def __init__(self, length, breadth):
      Shape.__init__(self,length, breadth)
  def AddShape(self):
    print("Rectangle value is: ",self._length*self._Breadth)
  
 OBJ = Rectangle(1000,32.457)
 OBJ.DisplayShape()
 OBJ.AddShape()

 PRIVATE:

 * This can be only accessded inside the class
 * This is created by specify two underscore before variable name.

 class Pet:
  def __init__(self,name,color):
    self.__Name = name
    self.__Color = color
  def DisplayDetails(self):
    print("Pet Name:", self.__Name,"\n" "Pet color:",self.__Color)

 Obj=Pet("Rahul",'Brown')
 Obj.DisplayDetails()
'''

#                  SELF-KEYWORD
'''
 * Self is a instance of a class.
 * Self refers object of the class.
 * ObjectName is automatically passes as function's first argument when
   the object is created.
 
      EX: Object=Employee()
       Employee.displaysalary() = Employee.displaysalary(self=Object) 
'''

#              UNIT TESTING
'''
 * Every software  has different Componenets
 * So we have to test exah and every compenents
 * This components are called unit testing.
'''

#                  POLMORPHISM
'''
 * Polymorphism is also called method overding and also 
   same function different behivour.
 * Before overding you have to inherit with parent's class.
 * And create a function inside child's class.
 * Function or method name should be same as parent's method's name.

 class ves1():
  def menu():
    menucolor = "Yellow"
    return menucolor
 class ves2(ves1):
  def menu():
      menucolors="Pink"
      return menucolors
 obj = ves2()
 print(ves2.menu())
'''

#             PICKLE AND UNPICKLE

'''
 PICKLEING
 * This is a module helps to convert human readable
   file to binary file.
 * Dump is the function helps to convert this.
   Dump helps to fetch wanted data into specfied file here it takes data cars as 
   1st parameter, file as second

 UNPICKLEING
  * It means upack the converted binary file
  * Load is the function helps to see this file
  

 import pickle
 cars = ['audi','benz','BMW']
 file = "mycars.pk1"
 #fileObject = open(file,'wb') # wb is write binary
 #pickle.dump(cars,fileObject)
 #fileObject.close()
 fileobject = open(file,'rb') # read binary
 print(pickle.load(fileobject))

'''

#             DEFAULT FUNCTION ARGUMENT
'''
 * If we did not pass any argument to function then
   The default argument will be passed.

 def Default(Name="Stranger"):
  print(Name)
 Default() # prints stranger
 Default("Raja")
'''

#                 RECURSION
'''
 * A function call itself is called recursion
 * It will become an infinite loop, so use carefully.
 * To avoid this recursion use two cases
  
  1. Base case - Recursion terminated here
  2. Recursive case - Calling function itself

 * Factorial is the best example for recursion

   5! --> 5*4!
      --> 5*4*3!
      --> 5*4*3*2!
      --> 5*4*3*2*1!

  * We just calling the same function to do this

 def Fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*Fact(n-1)
 res=Fact(10)
 print(res)
'''

#                PYTHONPATH
'''
 Python path is a environment variable this helps to
 python where looking for packages and module.
'''

#             FILE OPERATIONS
'''
 Open and read a file

 File=open('Python\Python-basics\TimeStamps.txt','r')
 #text=File.read()
 #text=File.readline()
 # We can specify number characters to be read
 text=File.read(2)
 print(text)
 File.close()

 Different modes:

 1. r - read
 2. w - write
 3. a - append
 4. + - Opening files for update
 5. rb - reads binary format
 6. rt - reads text format

 # Write files

 File =open("TimeStamps.txt",'w')
 Text=File.write('Project1 - django')
 print(Text)
 File.close()

 # Open file with with keyword

 with open('Python/Python-basics/TimeStamps.txt') as f:
  text=f.read() # It automatically close the file once it is read
  print(text)
'''
#            *arg and **kwargs
'''
 def Arg(a,b,*arg):
   mul = a * b
   for num in arg:
     mul *= num
   return mul
   
 print(Arg(1, 2, 3, 4, 5)) 

 def tellArguments(**kwargs):
  for key, value in kwargs.items(): 
   print(key + ": " + value)
 tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")
'''

#              HELP AND DIR
'''
 * help() helps to view the documentation of function,
   modules, classes, keyword etc.
 * dir() helps to view selected classes attributes.
'''

#               IF __NAME__=='__MAIN__'

'''
 * __name__ takes current module's name.
 * This statement is also called as main function
 * In java,c,c++ it has main functions like that python has main 
   function like this 
 * All the functions and classes inside this main function are only 
   executed while the current script is running.
 * You can't run that script's function when you import this script
   to another script
 * It is basically avoid unwanted execution
'''

#               .py and .pyc
'''
 * .py contians source code of python
 * .pyc file contains compilation of code
 * .pyc file is only created when you import a 
    file
 * We got byte code after compilation
 * Before executing a python program python interpreter checks for the compiled
   files. If the file is present, the virtual machine executes it. If not found, it checks 
   for .py file. If found, compiles it to .pyc file and then python virtual machine
   executes it.
 * Having .pyc file saves you the compilation time.
'''

#             CLASS AND OBJECTS
'''
 * A class is a blue print of a program.
 * Class allocates memory when the object is declared.
 * We can indentify class and attributes as

   1. Noun      - Name    -   Arjun               - class
   2. Adjective - Details - Age, Salary, Addredd  - Object, attribute
   3. Verb      - Work    - GetSalary()           - Methods, functions
  
   There are two type of variables and three type of methods

   VARIABLES:

   1. Class variables (or) -   class student:
       attributes                 Name = "Arun"
                                  Roll_no = 1222301
   2. Instance variables -  A variable that is created inside the 
      functions are called instance variables.

      class student:
        def display(self):
          # Body of method
 
   METHOD:

   1. Instance method - A method has self as a first argument are
      called instance method.

   2. Class method  - A  method has it's class name as it's first argument
      are called class method

      You can call this method without specifying
      object
  
  class stu:
  @classmethod
  def dis(cls,name,mark):
      print(f"{name} got {(mark/600)*100}%")
 stu.dis("raja",450) # Here cls argument takes
                    # class name as argument
 
 3. Static method - 
  
  * A Method without self and cls argument is called 
    static
  * You can call this method without specifying 
    object
    
 class Stu:
  @staticmethod
  def Hello():
    print("Iam from static method")
    
 Stu.Hello()
'''

#            PASS INSTEAD OF SELF
'''
 * We can pass any name instead of self
 * And we can declare functions inside class without 
   pass self keyword.
 class Method:
  def __init__(sharp,name,age):
    sharp.name=name
    sharp.age=age
  def dis(sharp):
    print(sharp.name,sharp.age)
 obj=Method("raja",21)
 obj.dis()
'''

#             FLOW OF INTREPRETER 
'''
 * Python has it's own complier inside intrepreter
  that will convert source code to byte code
 * And then that byte code moves to python virtual
  machine finally we got output 
'''

#                   SPLIT
'''
 * Split split's one string to a specified character
 * It returns a list of splited items.

 ar=input("enter:")
 print(ar.split('.'))
'''

#                   INHERITANCE
'''
 1. Single inheritance -  A base class inherits only one derived class.
                          
 2. Mutiple inheritance - A child class inherists  more then one class.

 class employee:
   name1=---
 class sales_executive:
   name2=---
 class All(employee,sales_executive):
   name3=---

 obj = All()
 obj.name1.name2

 3. Multilevel inheritance - When a child class becomes parents for another class.

 COMMON IMPORTANT POINTS:

  * By inheriting you can access all parent's class attribute,functions etc
  * In Multiple inheritance you can inherit multiple number of classes.
  * All this inheritance is may be used for polymorphism.
'''

#                 SUPER KEYWORD
'''
 SUPER METHOD - * when you have same name of attribute,method,constructor then this 
                  method will helps you to access parents class methods, attributes, 
                  function.
                * You can pass arguments to parent's constructor and methods using this.
 
 class em:

  name="raju"

  def __init__(self,data):
    print("Iam form em",data)

  def dis(self):
    print("Iam dis form em")
  
  def Dis(self,data):
    print("Iam Dis from em",data)

 class en(em):

  name="ragu"

  def __init__(self):
      super().__init__("C-ARGUMENT")
      print('Iam form en')

  def dis(self):
    super().dis()
    super().Dis("M-ARGUMENT")
    print("Iam dis from en",super().name)

 obj=en()
 obj.dis()
'''

#                 BUILT IN DECORATORS
'''
 PROPERY DECORATOR:

  * It allows class methods as attribute.
  * So we can call a function or methods without
    using ()
  * When we declare a method as property it can't
    be called as method. you can only use that
    function or method as attribute.

  SETTER DECORATOR

   * You can set attribute values with the help
   of this decorator, without this decorator we can't
   set values to the function changed attribute.
   
   * Before going to use this decorator you just
   change the method to attribute.

   * You have to create same name function to
   make setter.

   SYNTAX:  

    @property
    def fun():
      ---------
    @fun.setter
    def fun():
      ---------

    DELETER DECORATOR

    * Normal attributes are delete with the help
    of del() function. But in function changes 
    attribute we have to set this attribute to 
    deleter.

    * Helps to delete the existing attribute.

    * Before going to use this decorator you
    have to change a function to attribute.

    SYNTAX:
    @property
    def func():
      ------------
    @func.deleter
    def func():
      -----------

 class employee:
  def __init__(self,name,age,salary):
    self.Name=name
    self.Age=age
    self.Salary=salary

  @property
  def pro(self):
    if self.Name and self.Age and self.Salary==None:
      return("Deleted")
    else:
     return(f"{self.Name}\n{self.Age}\n{self.Salary}")
  @pro.setter
  def pro(self,string): # string gets values from
                        # attribute and sets to variable.

    name=string.split('.')
    self.Name=name[0]
    self.Age=name[1]
    self.Salary=name[2]
  
  @pro.deleter
  def pro(self): # this sets all the attributes are none
    self.Name=None
    self.Age=None
    self.Salary=None

 # propert
 obj=employee("raja",21,10000)
 print(obj.pro)

 # Setter
 obj.pro="kavin.20.20000"
 print(f"{obj.Name}\n{obj.Age}\n{obj.Salary}")

 # deleter
 del(obj.pro)
 print(obj.pro)
'''

#                OPERATOR OVERLOADING
'''
 * Operator overloading helps to change the behaviour of a
   operator, and also it helps to do different operations with 
   two objects(add,sub,mul).
 * Before going to do this we define the built in methods on that class.
 * We need to use this with two objects.

   EX 1:

   class Complex:
   def __init__(self,num1):
      self.num=num1
   def __add__(obj1,obj2): # Add will return multiple when + is used in object
      return obj1.num*obj2.num
   def __mul__(obj1,obj2): # Multiple will return Sub when - used in object
      return obj1.num-obj2.num

 obj1=Complex(3)
 obj2=Complex(4)
 print(obj1+obj2) 
 print(obj1*obj2)

 EX 2: 

 class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __add__(obj1,obj2): # It will automatically called when the +
                          # Symbol used in object
    return obj1.name+obj2.name
 obj=Student('raja',21)
 obj1=Student('ragu',22)
 print(obj-obj1)
'''

#           PASS BY VALUE PASS BY REFERENCE
'''
 Pass by value - copy of the actual object is passed.
 Pass by reference - Reference of the actual object
 is passed.
'''

#            TYR AND EXCEPT BLOCK
'''
  * try block trys something .
  * If try raise exception that will be handeled by the
    exception block
  * You can specify and raise an exception or use except
    exception as keywords.
  * Finally helps to specify what going to happend
    finally. This helps to close files. 

 #x='23'
 try:
 print(x)
 # You can define an exception in this ways
 except Exception as e:
  print(e) # It prints the raised exception
 except NameError as a:
  print()
 except:
  print("An exception occurd")
 finally:
  print("Process finished")
 if not type(x) is int:
  raise TypeError("Only integers are allowed")
'''

#             ENUMERATE
'''
 Helps to print arrays items with element
 l=[12,3,4,4,5,5]
 for i,itesm in enumerate(l):
  print(i,itesm)
'''

#            ITERATOR AND GENERATOR
'''

 ITERATOR:

 Before going to know about generator we have to 
 know iterabes, iterrator, iteration.

 1. Iterables -* variable's each elements are called 
                 Iterables or Iterators.
               * String can be performed as interables
               * But int can't be used as interable


                EX: a="apple"
                    b=[1,2,3,4]
                    for i in a:
                      print(a)
                    for i in b:
                      print(i)

  It print's each elements as one by one with the 
  help of iterables. 

  When we run this program for loop executes some
  method called __iter__() to check wherethere the
  given variable is iterable or not.

  So __iter__() is a method helps to create iterator

  __next__() is a method  helps to move next iterables

 2. Iteration - for loop moves to next list's values
                this process are called Iteration

 List=[1,2,3,4]
 It=iter(List)
 try:
 print(next(It))
 print(next(It))
 print(next(It))
 print(next(It))
 print(next(It))
 print(next(It))
 except StopIteration:
   print("Can't do")


 GENERATOR:

  * Let's assume we open a media player and play a 
    music suddenly we pause it and again we play it.
  * It starts where it is end. 
  * Generator also like this.
 
 * A function with yield keyword is called generator.
 * It returns a iterable collection of items
 * It helps to create iterators with different 
   manner.
 * We can return a value one or more times by using 
   generator in function.
 * Iterators are basically used in big data
 * When a program's execution process is log(n)

 def Generator():
  a,b=1,2
  c=a+b
  return c
 
 # Here return helps to return one value at a time
 # But using yield we can iterate another values.

 def Generator():
  a,b=1,2
  c=a+b
  yield c
  yield b
  yield a

 var=Generator()
 # To access the iterators we have to use next
 # next value is only called when the next method
 # is called.
 print(next(var))
 print(next(var)) # This is paused in b when we
                 # call next iterator it return 
                 # where it is left.
 print(next(var))
'''

#            METHOD OVERLOADING

'''
 Same method has different argument value is 
 called method overloading.

 class over:
   def rid(self,arg1):
     return "Good morning ",arg1
 obj=over()
 obj.rid('fahat')
 obj.rid("haabi")
'''

#           JOIN METHOD
'''
 Joins string with collection of iterables.
 
 List = ["Apple","Banana","Cherry"]
 Joined_string="and".join(List)
 print(Joined_string)
'''

#            DELETE FILES WITH OS
'''
 import os
 try:
 os.remove("TimeStamps.txt")
 except FileNotFoundError :
  print("Please input correct path")
 finally:
  if os.remove is True:
    print('File removed')
'''

#          FILE COMMANDS FOR UNIX LINUX
'''

# Displays working dir path

import os
print(os.system('pwd')) # pwd (print working directory) 

# appends text to a file because it has the correct permissions.
result = os.system("echo 'Hello, World! 🌍' > hello_world.txt")
print(f"Exit status: {result}")

OUTPUT: Exit status: 0 (0 indicts that the command executed without error
                        if a command has problem it will return
                        Exit status: 63253
                        )

# changing file permission

Let's change the file permissions to make the file read-only. 
The command only display a non-zero exit status code, 
indicating that it successfully changed the permissions.

os.system("chmod 444 hello_world.txt")
OUTPUT: 0

Now when we attempt to modify the file, it won't work because 
the necessary permissions are denied. This is also verified 
by the non-zero exit status code.

os.system("echo 'Good night, moon! 🌑' >> hello_world.txt")

OUTPUT:
sh: 1: cannot create hello_world.txt: Permission denied
512

We can change the file permissions to grant the 
necessary rights to perform the action, allowing us to run the commands successfully

os.system("chmod 666 hello_world.txt")
os.system("echo 'Good night, moon! 🌑' >> hello_world.txt")


# Remove file
os.system("rm -f 'application.log'")
# Create new file
os.system("touch 'application.log'")
# Append entry to log file
os.system("echo 'Log entry 1' >> application.log")
# Append another entry to log file
os.system("echo 'Log entry 2' >> application.log")
# Display file contents
os.system("cat application.log")
# Change permissions to remove read access
os.system("chmod 000 application.log")
# Try to display file contents
os.system("cat application.log")


                            Capturing Output of System Commands

os.system is a useful choice for commands that don't require using 
any of the resulting output. However, sometimes it is helpful to 
capture the output of a command for later use. If you want to use the 
output later, subprocess.run is a better choice.

We can use subprocess.run to capture the output of ls.

import subprocess

result = subprocess.run(["ls"], capture_output=True, text=True)

print("Output of 'ls':")
print(result.stdout)

'''

#         ACCESSING PARENTS MEMBER
'''
  There are two type of methods to access
    1. By using parent's name
    2. By using super keyword
'''

#        PYTHON ACCESS SPECIFIERS
'''
 _VariableName is considered as protected.
 __VariableName is considered as private.
 Without underScore it is considered as global.

 class One:
  _Name="Raja"
  __Degree="BSC"
  Dep="Computer Science"
 class Two():
  print(One._Name)
  print(One.Dep)
  try:
   print(One.__Degree) 
  except Exception as e:
    print("Can't access private members")
'''

# DIFFERENCE BETWEEN NEW AND OVERRIDE MODIFIERS
'''
  * new modifier tell to complier to execute new
    implementation. Not base class
  * Override helps to override parent's class 
    methods
'''

#              ISSUBCLASS()
'''
 Helps to check wherethere the specifed classes
 is inheriting another class or subclass.

 class cls1:
  pass
 class cls2(cls1):
  pass
 print(issubclass(cls2,cls1)) 
'''


#             REGULAR EXPRESSION

#  Functions in regular expression
'''
 NOTE: clickable link will not extracted EX:email id clickable in 
       a resume it cannot be extracted.
       
 SYMBOLS:

 1. ^ - startswith
   
   EX: import re
        text="rajakavintha@gmail.com" 
        Searcher=re.search("^r",text)
        print(Searcher.string)


 2. $ - endswith
      
      EX: import re
        text="rajakavintha@gmail.com" 
        Searcher=re.search("m$",text)
        print(Searcher.string)
 
 3. \s - spaces

      EX: txt = "The rain in Spain"
        x = re.search("\s", txt)
        print("The first white-space character is located in position:", x.start()) 

 4. ['a-z'] - List of character

      EX: txt='gfdcvgred'
          x=re.findall(['a-z'],txt)

 5. \d - find all digits 

     EX: def NameValidation(str):
            Validator=re.findall('[a-zA-Z\d]',str)
           return Validator
        print(NameValidation('raji123'))

 6. . - Allows any character in specified place
    
    EX: text='hello'
       x=re.findall('l.o',text) 
       print(x)
 
 7. * - Zero or more occurence
     
     EX: text='hello'
         x=re.findall('l*',text)
         print(x)

 8. + - One or more occurence

    EX: text='hello'
        x=re.findall('o+',text)
        print(x)

 9. ? - Finds Zero or one occurence

    EX: text='hello'
        x=re.findall('g?',text)
        print(x)

 10.{2} - Finds specified number of occurence

    EX: text='hello'
        x=re.findall('e{1}',text)
        print(x)


 11. | - Finds either or

    EX: text='hello'
        x=re.findall('l|1',text)# finds l or 1
        print(x)

 SPECIAL CHARACTER

 1. \A - Finds if the specifed charcter are in begining
     
    EX: re.findall('\Aain',ainini)
 
 2. \b - Finds is the specified char in start or end

    EX: re.findall(r'/bain',ain)
        re.findall(r'n/b',ain)

 3. \B - retuns match if the specified char are present

    EX: re.findall(r"\Bain",ain)

 4. \S - returns match where the string doesn't contains
         space 

      EX: text='h e ll o'
         x=re.findall('\S',text) # it returns atleast one match
         print(x)

 5. \w - Matches a string contains a-z0-1 and special characters

     EX: def NameValidation(str):
           Validator=re.findall('\w',str)
           return Validator
          print(NameValidation('hell_123'))

  SETS:

  [] - returns the specified match

  import re
  def NameValidation(str):
     Validator=re.findall('[0-9][0-10]',str)# returns 2 digit 
     return Validator

 REGEX FUNCTIONS:

 1. findall(patter,text) - returns all matches in an text as list
                           returns empty list if no match is found

                           EX: import re
                           txt = "The rain in Spain"
                           x = re.findall("ai", txt)
                           print(x)

 2. search(pattern,text) - returns first occurence of the
                           object else none.
    It has three methods

      1. start() - returns the start index of the 
                   specifed pattern
      2. span()- return star,end index of the specified
                 pattern
      3. string - returns sepcified pattern string 
      4.group()- returns the part of the string 
                 where there was a match  
      
 3. split(pattern,text,no_of_split)  - split's if the specified object is
                                        found and return list

                                        EX: import re
                                            txt = "The rain in Spain"
                                            x = re.split("\s", txt,1)
                                            print(x)

 4. sub(old,new,text,how_many_matches_should_be_replaced)  
         
       replace old string with new value
                         
                          EX: import re
                          txt = "The rain in Spain"
                          x = re.sub("\s", "9", txt)
                          print(x)
'''





#           FIX RANGE WITHOUT RANGE
'''
 End=int(input())
 Split=list(map(int,input().split(' ')))[:End]
 Set=set(Split)
 Runner_Up=sorted(Set,reverse=True)
 print(Runner_Up[1])
'''

#          USING * BEFORE VARIABLE
'''
 a,*b,c=1,2,3,4,5
 a=1
 c=5
 b=[2,3,4]
'''

#        DATABASE CONNECTION IN PYTHON
'''
 print("1.Insert, 2.Update, 3.Delete, 4.Select")
 import sqlite3
 Con=sqlite3.connect('Python/User.db')

 def Insert_new_data(Name,Age,Course):
  try:
   qry="INSERT INTO User (Name,Age,Course) VALUES (?,?,?)"
   Con.execute(qry,(Name,Age,Course))
   Con.commit() # Saves all changes into users table
   print("Row inserted")
  except Exception as e:
    print(e)

 def Update_data(Name,Age,Course,id):
  try:
   qry="UPDATE User set Name=?,Age=?,Course=? WHERE Id=?"
   Con.execute(qry,(Name,Age,Course,id))
   Con.commit() # Saves all changes into users table
   print("Row Updated")
  except Exception as e:
    print(e)

 def Delete_data(id):
  try:
   qry="delete from user where id=?;"
   Con.execute(qry,(id))
   Con.commit() # Saves all changes into users table
   print("Row Deleted")
  except Exception as e:
    print(e)

 def Select_data(id):
    qry="Select Name from User where id=?"
    e=Con.execute(qry,(id))
    for i in e:
      print(e)
    Con.commit()
    
    print(f'Your selected data is')

 ch=1
 while ch==1:
  c=int(input("Enter your choice: "))

  if c==1:
    Name=input("Enter name: ")
    Age=int(input("Enter your age: "))
    Course=input("Enter Course: ")
    Insert_new_data(Name=Name,Age=Age,Course=Course)

  elif c==2:
    Name=input("Enter name: ")
    Age=int(input("Enter your age: "))
    Course=input("Enter Course: ")
    Id=int(input("Enter Id: "))
    Update_data(Name=Name,Age=Age,Course=Course,id=Id)
    
  elif c==3:
    Id=(input("Enter Id: "))
    Delete_data(id=Id)

  elif c==4:
    Id=input("Enter ID: ")
    Select_data(Id)
  
  else:
    print("Please type any number")
  ch=int(input("Enter 1 to continue: "))
'''

#              PANDAS,DATAFRAME TYPES
'''
 * It is an open source library used in data 
   analysis
 * It helps to access different type of data
   format
 * You can be easily slicing big data

 DATAFRAMES

 * It is an collection row and column data
   that was stored as various data types

 * Dataframe can be created in 3 ways

   1. List

   EX: 
     import pandas
     data=[['raju',23],['raja',21],['rajesh',22]]
     DF=pandas.DataFrame(data,index=['a','b','c'],columns=['Name',"Age"])
     print(DF)

   2. Dict

      When we pass dict as an data the key name
      will be changed to column name

      EX: 

       import pandas
       data={'name':['raju','ragi','rajan'],'age':[22,23,23]}
       DF=pandas.DataFrame(data,index=['a','b','c'])
       print(DF)

        
   3. Series
    
    * A collection same data type is called series
    * It has dtype argument to specify data type

    EX: 

      import pandas
      data={'one':pandas.Series(['raju','ragi','rajan'],index=[1,2,3]),'two':pandas.Series(['rgu','ranjith','rahul'])}
      DF=pandas.DataFrame(data) 
      print(DF)
 
    * When you declare a dict as series the key
      values are changed as index.

      EX:   

       import pandas as p
       D={'a':100,'b':200,'c':300}
       DF=p.Series(data=D)
       print(DF)

    * We can declare data as list

      EX: import pandas
          D=['raju','chari']
          DF=pandas.Series(D)
          print(DF)
'''

#               SERIES METHODS
'''
 1. axes - returns index from start-end

    import pandas
    D=pandas.Series([100,200,300])
    print(D.axes)

 2. dtype - returns series dataype
 3. empty - returns bool
 4. ndin - returns no of diamensnal
 5. size - returns no of element
 6. values - returns list of items into series
            without index
 7. head(3) - returns specified number of items
             from top.
 8. tail(3) - returns specified number of items
             from bottom.
 9. plot(kind='bar') - helps to create a chart from series
 
 To work with this we need to import matplotlib
 EX:
 
 train_class_distributions.sort_values().plot(kind='bar')
 # Add axis labels and title
 plt.xlabel("Class Label")
 plt.ylabel("Frequency [count]")
 plt.title("Class Distribution in Training Set")
''' 

#          DATAFRAME FUNCTIONS
'''
 1. axes- returns index
 2  dtype - returns datype
 3. empty - returns bool
 4. ndim - diamansnal
 5. shape - returns number of row and column
 6. size 
 7. values 
 8. head()
 9. tail()
 10 T      - changes row wise data to column
              column wisw data to row
 EX: 

  import pandas
  D={'name':pandas.Series(['raju','kunaal','gokul']),'Age':pandas.Series([20,20,20])}
  DF=pandas.DataFrame(D,index=range(1,4))
  print(DF.T)
''' 

#           APPLY METHOD IN DF PANDAS
'''
 Apply method helps to apply functions to DF

 EX: 

    import pandas as p
    import numpy as n
    Data=n.random.randint(1,6,[3,3])
    DF=p.DataFrame(Data,columns=['col1','col2','col3'],index=['a','b','c'])
    def double_data(d):
          return d*2
    All=DF.apply(double_data) # it apply all side
    Col=DF['col2'].apply(double_data)
    Row=DF.loc[2:2,2].apply(double_data)
    #print('ALL',DF,All)
    #print(DF,Col)# applyies column side
     print(DF,Row)
'''

#      ITERATION IN SERIES AND DF PANDAS
'''
 When we iteratre series it returns items
 of the series

 import pandas
 Data=[10,20,30]
 Series=pandas.Series(Data)
 for i in Series:
   print(i)

 DF ITERATION
  
  iteritems()-It iterates the value by column return tuple
  iterrow()- It iterates data row wise returns tuple
  itertuples()- It returns row wise data with column name

  import pandas
 Data={"Growth":[1,2],"Items":['orange','Apples']}
 Series=pandas.DataFrame(data=Data)
 print(Series)

 for i in Series.iteritems():
    print(i)

 for i in Series.iterrows():
    print(i)

 for i in Series.itertuples():
   print(i)
'''

#            BASIC STATICS FUNCTION
'''
 SYNTAX: DF_name.count()

 1. count()- returns no of element in each column
 2. sum() - returns sum of each column
 3. mean() - returns average of each column
 4. median() - returns medium value
 5. mode() - returns repated data in each column
 6. min(),max() - returns min,max data
 7. abs() - returns positive values
 8. describe() - returns all of the above in
                 DF format
'''

#       ORDERING MULTIDIAMENSONAL ARRAY
'''
 # key supports less than 

 Name_Scoure=[['Tina', 5], ['harry', 4], 
              ['Berry', 2], ['Harsh', 1], 
              ['Akriti',6]]
 print(sorted(Name_Scoure,key=lambda x:x[1]))
 
 # Sorting dict by values in des
 max=sorted(dict.items(), key= lambda x: x[1], reverse=True)

'''

#                SWITCH CASE IN PYTHON
'''
 Python 3.10 supports this

 EX: 
  def days(number):
  match number
  case 1:
    return 'monday'
  case 2:
    return 'tuseday'



L = [int(i) for i in input().split()]
for i in L :
  if i>1:
    if i%2 == 0:
      continue
    if i%3== 0:
      continue
    else:
      print(i)
'''
#      SORTED FUNCTION IN PYTHON

'''
  * You can sort an list and dict 
  * Dict will be sorted as their key
  * And we can sort an list according
    to their elements lenght with the
    help of key. 

  Dict={1:'1',2:'2',3:'3'}
  print(sorted(Dict))

  List=["aaa","bb","cccccc","dddd"]
  print(sorted(List,key=(len)))

'''
#                    PATHLIB
'''
The pathlib module offers many advantages over the older os.path way, 
such as a consistent way to handle paths across different operating systems. 
The pathlib module does this by treating paths as objects rather 
than strings. The module also provides methods for common file operations, 
making tasks like listing directory contents, creating directories, 
and searching for files more straightforward.

 1. Home: Let's access the home directory with Path.home(). 
          Note that method-based operation is cross-platform, 
          thus the same code will work the same regardless 
          of the operating system.
 
 from pathlib import Path
 home_directory = Path.home()
 print(home_directory)
 
 2. CWD -  Find the current working directory using the cwd method on Path.

 current_working_directory = Path.cwd()
 print(current_working_directory)
 
 3. The forward slash (/) operator

    The forward slash (/) operator in pathlib is used for path joining. 
    The / operator allows you to combine multiple Path objects or strings     
    to create new paths. It automatically uses the correct path separator 
    for the current operating system (/ for Unix-based systems and \       
    for Windows). As a result, the same code can run on different operating 
    systems without any rewriting.

    Below is an example of creating a variable that combines a 
    Path object with several other elements. Note that since this only is a  
    variable right now, it does not need to reference an actual location.
    
    path = Path("folder") / "subfolder" / "file.txt"
    print(path)
    
    OUTPUT: 
    folder/subfolder/file.txt
    
    Create a variable that defines a folder named "scripts" in the current directory.
    
    current_working_directory = Path.cwd()
    scripts_path = current_working_directory / "scripts"
    print(scripts_path)
  
    Python Path objects are different from Python strings (str). 
    The addition operator (+) for Python string does not work with Python Path     
    objects. The forward slash (/) operator has to be used with Python 
    Path objects
    
    4. Absolute vs. Relative Paths:
    
       When working with paths, it's important to understand the distinction between 
       absolute and relative paths. Absolute paths provide the        
       complete route from the root directory to the specified location, while relative 
       paths are based on the current working directory.  pathlib allows you to create both 
       
       types: an absolute path might look like Path('/home/jovyan') and a relative 
       path could be Path('03-traffic-in-dhaka/lessons'). Note that a relative 
       path doesn't start with a root directory indicator (like "/" on Unix-based systems or "C:" on Windows).

       Below is an example of converting a relative path to an absolute 
       path by prepending the absolute path to the beginning of the relative path.
       
       relative_path = Path("config", "settings")
       absolute_path = Path.home() / relative_path
       print(absolute_path)
       
       OUTPUT: /root/config/settings
       
  5. Listing directory contents
  
     Instances of the Path class have the iterdir method which 
     iterates over the contents, files and subdirectories, of a 
     given directory. Calling the iterdir method returns an iterator 
     that doesn't load all the results into memory at once.

     Below is an example of using the iterdir method.
     
     current_working_directory = Path.cwd()
     print(current_working_directory.iterdir())
     
     current_working_directory = Path.cwd()
     for item in current_working_directory.iterdir():
         print(item)
         
    OUTPUT:
    /app/.ipynb_checkpoints
    /app/031-fix-my-code.ipynb
    /app/Arial.ttf
    /app/Test.ipynb
    
    iterdir() returns an iterator, not a list. That means you can't 
    directly print it or get its length.
    
    If you want to load the data into memory all at once, 
    the iterator can be cast into a list.
    
    # Cast to list before printing
    print(list(Path.cwd().iterdir()))
    
    [PosixPath('/app/.ipynb_checkpoints'), 
    PosixPath('/app/031-fix-my-code.ipynb'), 
    PosixPath('/app/Arial.ttf'), PosixPath('/app/Test.ipynb
    )]
    
    6. Making directories
    
    The pathlib module has a convenient way to create a 
    new directory. Create an instance of a Path class that 
    specifies the location of this new directory, then call 
    the mkdir method to actually create it.
    
    Below is an example of how this is done. If this cell is 
    run twice it will generate a FileExistsError.
    
    scripts_dir = Path.cwd() / "scripts"
    scripts_dir.mkdir()
    
    Adding the keyword argument exist_ok=True prevents raising 
    an error if the directory already exists.
    
    scripts_dir = Path.cwd() / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    
    7. Glob patterns
       
       Glob allows you to search for files and directories using 
       wildcard patterns, making it handy to find files with certain 
       suffixes. We can use the glob to find all the TrueType 
       font (.ttf) files in the current directory.
       
       current_working_directory = Path.cwd()
       all_ttf_files = current_working_directory.glob("*.ttf")
       for file in all_ttf_files:
          print(file)
          
      OUTPUT:
      /app/Arial.ttf
'''


#           MAKE COUNT ON NESTED LIST
'''
sum(sublist.count(1) for sublist in [['a', 1], ['b', 1]])
'''

#                      GETATTR
'''

getattr() is a built-in Python function that allows us to
dynamically access an object's attributes (such as methods) 
using a string name. This is useful when the method name is 
determined at runtime.

# Read input
n = int(input())  # Number of elements in set A
A = set(map(int, input().split()))  # Set A elements
N = int(input())  # Number of other sets

# Perform operations
for _ in range(N):
    operation, _ = input().split()  # Read operation name
    other_set = set(map(int, input().split()))  # Read the other set
    getattr(A, operation)(other_set)  # Execute the operation dynamically

# Print the sum of elements in set A
print(sum(A))

'''

#            TRY WITH ELSE
'''
  When we use try with else the blok of else executed only if
  there is no error on try block.

  EX:
  def lookup(my_list, index):
    try:
        value = my_list[index]
    except IndexError:
        return "Error: Index out of range."
    else:
        return f"The value at index {index} is {value}."


print(lookup(my_list=["a", "b", "c"], index=2))  # Index in range
print(lookup(my_list=["a", "b", "c"], index=5))  # Index out of range

OUTPUT:
The value at index 2 is c.
Error: Index out of range.
'''

#              SWAPCASE IN STR FUNCTION
'''
def swap_case(s): 
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''

#      BUILT IN ANY FUNCTION
'''
if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
'''


#     STRING FUNCTIONS
'''
In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
.center(width)

This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
.rjust(width)

This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
'''


#                  TEXTWRAPER
'''
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

INPUT:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

OUTPUT:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

#     CAPITALIZE METHOD      
'''
 
def solve(s):
    return ' '.join(word.capitalize() for word in s.split())

Sample Input

chris alan

Sample Output

Chris Alan
'''

#        GROUP METHOD IN REGEX
'''
group()
A group() expression returns one or more subgroups of the match.
Code

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')

groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
Code

>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
'''

#                   MEANS OF 1E+ 30
'''
while performing some divison operation we might got this
type of number it means 1*(10)**30
'''

#              OPERATORS
'''
 ------------------Operators Types:-------------------
Opeartors are used to perform operations on values and variables.

1]Arithmetic Operators
2]Assignment Operators
3]Logical Operators
4]Relational or Comparison Operators
5]Membership & Identity Operators
6]Bitwise Operators


----------------Arithmetic Operators:---------------
1]Addition        - [+]  1+1=2
2]Subtraction     - [-]  1-1=0
3]Multiplication  - [*]  2*2=4
4]Division        - [/]  10/5=2.0
5]Modulo Division - [%]  10%5=0
6]Exponentiation  - [**] 5**2=25   -----5*5=25
7]Floor Division  - [//] 10//5=2   
-----------------------------------------------------

Floor division operator (//)

a=10
b=3
print(a/b) 
print((a//b))

OUTPUT:

3.3333333333333335
3

                 ASSIGNMENT OPERATOR
                 
a = 10
b=20
b-=a   # assings minus value to b
print(b)                 

We can put +,//,%, **(exponential), *


                       COMPARISION OPERATOR

>,<,>=,<=, ==, !=


When we compare two string then the comparison is converted to
lexical comparison.

a='2300'
b='100'
print(a<=b)

Strings are compared character by character based on their ASCII values.
'2' (ASCII: 50) comes after '1' (ASCII: 49), so '2300' > '100'.

So the output will be false


              LOGICAL OPERATOR
              
              And, OR, NOT
              
a=1; b=3; c=3

# if the left hand side value is non zero
# than the right hand side value is printed
# here
print((a and b),(b and c), (c and a))

# It works in opposite way of and
print((a or b),(b or c), (c or a))

Using all this alone then it works in opposite way of above one
print(a and b) # 1



              
---------------Membership & Identity Operators--------------------


1]Membership Operators: 

   1) in     
   2) not in 

a = 'hel'
b = 'world of hello'
print(a in b) # True Compared substring from b

2]Identity Operators:
   1) is      
   2) is not

a = 'hell0'
b = 'world of hello'
print(a is b) # False Compares exact value

a = 'hello'
b = 'hello'
print(a is b) # True Compares exact value

'''

#                OPERATOR PRECEDENCE
'''

Precedence	    Operator	        Description
1 (Highest)	      ()	       Parentheses (Grouping)
2	              **	       Exponentiation
3	            +x, -x, ~x	Unary Plus, Unary Minus, Bitwise NOT
4	            *, /, //, %	Multiplication, Division, Floor Division, Modulus
5	+, -	Addition, Subtraction
6	<<, >>	Bitwise Left and Right Shift
7	&	Bitwise AND
8	^	Bitwise XOR
9	`	`
10	==, !=, >, >=, <, <=	Comparison Operators
11	is, is not, in, not in	Identity & Membership Operators
12	not	Logical NOT
13	and	Logical AND
14 (Lowest)	or	Logical OR

print(2+3-5) # if same precedence operator are there in a calculation
             # then the calculation will starts from right to left
             # so the answer is 3-5=-2  2-2 = 0

'''

#      CONTROL FLOW STATEMENT
'''
                NESTED IF
                
no = 155

if 100<= no <= 200:
    print("range of 100 200")

    if no>= 150 and no <= 160:
        print("inner range of 150 to 160")

        if(no==155):
            print("no is", no)

    else:
        print("inner no", no)
   
   
               DIFFERENCER BETWEEN CONTINUE AND PASS            

EX1:

list=["kumar","raja","sam","ram"]
for i in list:
    if i =="sam":
        continue # it stops printing same
        #pass # allows to print sam
    print(i)


EX2:

no = int(input('range: '))
while no<=5:
    print(no)
    if(no==3):
        #break
        #continue # continues the loop not the operations, so it
                 # doesn't goes to increment operations
        pass # continues to next statement that is increment
    
    no+=1
    
    
                NESTED WHILE
                
no = int(input('range: '))

while no<=5:
    print(no)

    j=2
    while j>=0:
        print("inner", j)
        j=j-1

    no+=1

OUTPUT:

range: 0
0
inner 2
inner 1
inner 0
1
inner 2
inner 1
inner 0
2
inner 2
....


                    REVERSE STRING WITH FOR
                        
a="sakthi"
b=""
for i in a:
    b=i+b
print(b)

                        SORT
list1=[1,8,3,4,9,6,7,5]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] >= list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)


                MIN AND MAX
                
number = [5, 2, 8, 1, 6, 100]
minimum = number[0]
maximum = number[0]
for a in number:
    if a < minimum: 
        minimum = a 1
    if a > maximum:
        maximum = a 100
print("Minimum number:", minimum)
print("Maximum_value:", maximum)


               FOR LOOP REVERSE RANGE

for i in range(10,0, -2):
    print(i)
               
'''

#     LIST METHOD
# Collction of unsimilar data types
'''
1. clear - clears items from original array and returns None
2. extend - allows to add more than one element in existing
            array, returns None
3. append - allows single element, returns None
4. insert - add element in specified index, not replaces a element
            it adds element in existing array, returns None
5. pop - removes last element and specified index element, 
         removes element from original list returns the
         removed element
6. removes - removes specified value from original array, 
             it removes only the first occurance, returns None
7. sort - if reverse=True orders desceding, sort original array
          returns None
8. count - returns the count of all occurances of a specified element
9. copy - returns new copied array

                     ORDERED DATA TYPE
a=['2',1,5,6]
print(a)
OUTPUT: ['2',1,5,6] Order of the data will not change while print  


                     ALLOWS DUPLICATE         
a=['2',1,5,6,1,1]
print(a)

OUTPUT: ['2',1,5,6,1,1] 

                           COUNT
                           
a=['2',1,5,6,1,1]
print(a.count()) # 3


'''

#                      SET
'''
          UNORDERED AND DUPLICATE NOT ALLOWED

when ever we tries to print the set element its
order gets changed.

a={1,4,5,'hi'}
print(a)

OUTPUT 1: {'hi', 1, 4, 5}
OUTPUT 2: {1, 5, 'hi', 4}


              INDEX CANNOT BE USED



                 ADD

adds element in random place, if all the elements in set
are int then it will add the element in first place
returns None

a={2,4,3}
a.add(100)
print(a)

a={2.0,4,3.3134}
a.add(100)
print(a)

Combination of string and numeric data type the order of
the add will be random


a={2.0,4,3.3134,'CHAR'}
a.add(100)
print(a)

OUTPUT1: {2.0, 3.3134, 100, 4, 'CHAR'}
OUTPUT2: {'CHAR', 2.0, 3.3134, 100, 4}

                 POP

We can't give position on this pop, deletes random element when combination
of data types given to the set like the add

Returns the deleted element

a={"helo",2,'hi',4,3}
a.pop()
print(a)

OUTPUT1:
{3, 4, 'helo', 'hi'}

OUTPUT 2:
{2, 3, 4, 'helo'}


For only string data elements it pops random
element

st={"raja","ram","kumar","sakthi"}
st.pop()
print("pop",st)


                UPDATE
                
Allows to add more than one elements into set
returns none

a={1,4,5,'hi'}
print(a.update({1,2,3}))
print(a)

                  CLEAR
             
Clears all the element in existing set.
It doesn't returns it.

a={1,4,5,'hi','hi'}
print(a.clear())
print(a)

                 SUB AND SUPER SET, DISJOINT

Returns bool

a={1,4,5}
b={1,2,4,3,8,10,5}
print(a.issubset(b)) Checks is a small set is
                     subset of large set
                     
print(b.issuperset(a)) checks is a large set is
                       subset of small set

OUTPUT:
True
True

For combination of data tpes it gets confused

a={1,4,5,'ji'}
b={1,2,4,3,8,10,5,'hi'}
print(a.issubset(b))
print(b.issuperset(a))

OUTPUT:
False
False


                   DISJOINT
                   
checks the second second it differ from current
set, returns bool

a={1,4,5,'ji'}
b={2,3,8,10,'hi'}
print(a.isdisjoint(b))

OUTPUT: True

                    UNION
              
returns grouped element

 
                    DIFFERENCE UPDATE
                    
a=[545,335,5366,86745,2425]
b=[545,335,43,42,1]
c=[545,335,5366,86745,2425,5523,2351,6353]

s1=set(a)
s2=set(b)
s3=set(c)

#updates the give set with all the uncommon values
#returns none

s3.difference_update(s2,s1)

print(s3)

OUTPUT: 5523,2351,6353


                INTERSECTION UPDATE
                
a=[545,335,5366,86745,2425]
b=[545,335,43,42,1]
c=[545,335,5366,86745,2425,5523,2351,6353]

s1=set(a)
s2=set(b)
s3=set(c)

# updates s1 with common values from all set
# returns none
s1.intersection_update(s2,s3)

print('common element', s1)


                SYMMETRIC DIFFERENCE
                                 
a=[545,335,5366,86745,2425]
b=[545,335,43,42,1]
c=[545,335,5366,86745,2425,5523,2351,6353]

s1=set(a)
s2=set(b)
s3=set(c)

# Removes common elements and remains
# the uncommon elements from both set that are combined
# into a single set and it returns that new set
# it has update method too
c=s1.symmetric_difference(s2)

print('common element', c)

'''


#                   FUNCTIONS
'''
1. Keyword function
2. default argument
3. variable argument function with * and **
'''
#                    DICT
'''
Doesn't allows duplicate values. It is ordered

keys()
values()
get()
items()
clear() - clears all items in orginal dict
copy()
pop()
update() - Helps to add new items and update specific
           item on original dict
           
           Return none

dic={"Name":"sakthi","age":"23"}
dic.update({"Name":'Akash', 'Age':'21', 'Course':'DS'})
print("Dictionary",dic)

OUTPUT:
Dictionary {'Name': 'Akash', 'age': '23', 'Age': '21', 'Course': 'DS'}

'''


#                 TUPLE
'''
Immutable, allows duplicate

slice() - built in function, does slicing
EX:
a=(1,3,4,4,2,4,2)
b=slice(3)
print(a[b])

OUTPUT:
(1,3,4)

Count() - returns count a specific element
Index() - returns first occurance index of specific element

EX:
a=(1,3,4,4,2,4,2)
print(a.index(4))

OUPUT:
2

len()
max()
min() 

           ADD TUPLE ITEMS WITH +

tpl1=("sam","ram","kumar")
tpl2=("1","2","3")
print(tpl1+tpl2)
OUTPUT:
('sam', 'ram', 'kumar', '1', '2', '3')

'''
#                    STRING
'''

Immutable data type

capitalize() - Captilize single starting char and returns it
EX:
str='hai helo hai'
print(str.capitalize())
OUTPUT:
Hai helo hai

lower()
upper()

center() - Aligns the text in center place with the give char
EX:
a='hello'
b=a.center(11,'*')
print(b)
OUTPUT:
***hello**

count()
index() - returns error if element is not found
find() - Returns the index of first occurence, returns -1
         if element is not found
EX:
a='hello'
b=a.find('l')
print(b)
OUTPUT:
2
  
replace() - 
The below code replace only the word, beacue we
specified 1
str='hai helo hai'
print(str.replace('hai','helo',1))
OUTPUT:
helo helo hai

split() - 
Here 1 in max split
str='hai helo hai'
print(str.split(' ',1))
OUTPUT:
['hai', 'helo hai']

strip() - removes spaces from both left right
lstrip() - removes spce from left
rstrip() - from right

title() - Converts capitalize in a paragraph
a="
this is the
sample paragraph
that explains how title
function 
in strings are 
worked in
python.
"
b=a.title()
print(b)

OUTPUT:
This Is The
Sample Paragraph
That Explains How Title
Function 
In Strings Are 
Worked In
Python.


All the above functions returns values, below return bool
isalnum()
isnumeric()
isupper()
islower()
           
'''

#                  SLICING AND INDEXING
'''
a=[10,20,30,40,50,60,70,80,90,100]
#   0  1  2  3  4  5 -4 -3 -2 -1
b=a[5:-2]
print(b)

OUTPUT:
[60, 70, 80]
---------------------------------------------

a=[10,20,30,40,50,60,70,80,90,100]
b=a[5::-1] # starts from 5th index it prints
           # element in reverser order
print(b)

OUTPUT:
[60, 50, 40, 30, 20, 10]
 
--------------------------------------------------

a=[10,20,30,40,50,60,70,80,90,100]
b=a[5::-2] # starts from 5th index it prints
           # element in 2 by 2 reverser order
print(b)


'''

#Python world - Not alpha num
user_input= list("hi iam raja")
dict={}
for char in user_input:
    dict[char] = user_input.count(char)
num=len(user_input)//2
some_char_index=list(dict.keys())[num]
some_char_frequency=dict[some_char_index]
print(some_char_index,'is occurred in ',some_char_frequency)













