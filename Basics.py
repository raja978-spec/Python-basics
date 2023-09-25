
#                DATA TYPES
#          PRIMITIVE DATATYPES
'''
 Primitive data types are the basic data type. 

 * Integer 
 * Float
 * String
 * Bool
 * None it is also an data type
'''
#          KEYWORD PACKAGE
'''
from keyword import kwlist
print(kwlist)

returns the dictionary of all keywords in python
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
                * dictinoary has some methods,get is the one of 
                  the method, with the help of that we get value
                  of that key if the key is not found it will
                  return an default value, to achive this we do
                  this dict.get("name","raja") here it tries to
                  get name if it has no value then raja will 
                  be returned.
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

 #       GLOBAL KEYWORD

'''
 y = "python " # global scope variable

 def Outterfun():
    z = 123 # local variable
    global x # global helps to access inner function's function on outside 
    x= 'Hello ' 
    def innerfunc(): # Enclosing scope
      print('Welcome ')
    innerfunc()

 Outterfun()
 print(x+ y+'Programmers')
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

 Set = {12,3,4,55,6}
 Frozen = frozzenset(Set)
 Frozen.add(22) # Raises error
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
print(obj("raja"))
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
  def __init__(s,name,color):
    s.__Name = name
    s.__Color = color
  def DisplayDetails(s):
    print("Pet Name:", s.__Name,"\n" "Pet color:",s.__Color)

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


#       ORDERING MULTIDIAMENSONAL ARRAY
'''
 # key supports less than 

 Name_Scoure=[['Tina', 5], ['harry', 4], 
              ['Berry', 2], ['Harsh', 1], 
              ['Akriti',6]]
 print(sorted(Name_Scoure,key=lambda x:x[1]))
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


#          SERIALIZATION AND DE-SERIALIZATION
'''
 * Serialization is an process of converting object
   into memory and memory into an byte string data.
   This is ca be stored on database and send over an
   network.
'''

#      CPYTHON AND JYTHON
'''
 * CPYTHON supports c programming with python language
 * JYTHON created with the combination of java an d python

 You can see flavors of python in google 

 * Python is plat form indenpandent and cross platform it 
   means it can be run on multiple os.
'''

#              ID FUNCTION
'''
All the variables are consider as memeory location of an
variable so id returns the memory address of the variable

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2 # returns int value instead of float 
            if(nums[mid]==target):
              return mid 
            elif(target>nums[mid]):
                start=mid+1
            elif(target<nums[mid]):
                end=mid-1        

obj=Solution()
print(obj.searchInsert([1,3,5,6],5))

class Solution:
    def plusOne(self,digits=[9] ):
        digits[-1]+=1
        if digits[-1] >= 10:
            digits=str(digits).
            print(d)
            digits=[int(i) for i in d]
            return digits
        else:
          return digits
        
obj=Solution()
res=obj.plusOne()
print(res)
'''
from os import *
from sys import *
from collections import *
from math import *

def bitInsertion(x, y, a, b):
    # write your code here
    # return an integer denoting the result of inserting Y in X starting from A and ending at B
    BinX=''.join(bin(x)[2:])
    Biny=''.join(bin(y)[2:])

    BinX.remove(BinX[-b:-a])
    print(BinX)

bitInsertion(1536,7,1,5)
