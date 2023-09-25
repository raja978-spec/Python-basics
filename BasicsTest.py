'''
 1. Describe primitive and non primitive data types
 2. Describe numeric,muttable,immutable data types
 3. Describe sequence data types, can we add two tuples
 4. Which data type has no index, can we perform slicing operation on
    that datatype?
 5. Describe unordered data types
 6. What is type checking, remmember the ways of type checking
 7. What is PEP8 and give abbrevation
 8. Memory management in python 
 9. What is namespace ? Remmember it's types
 10.What is scope ? Remmember type of scopes with example 
 11.What is decorators explain with example 
 12.Type of argument passing in function
 13.Add tuple into list and set with Comprehension 
 14.What is the use of froozen set
 15.What is lambda function ?
 16.What is the use of isinstance keyword?
 17.What is the difference between shallocopy and deepcopy
 18.Create dict using comprehension?
 19.Is set can contain duplicate value?
 20.Difference between remove and pop?
 21.What is the use of del?
 22.Can we you use same key name in dict?
 23.Can we add list into set?
 24.Difference between xrange and range, which python version use this xrange?
 25.Create constructor and str inside a class, remember the use of str
 26.What is access modifiers in python and define the type of modifiers?
 27.What is the use of self keyword?
 28.What is unit testing?
 29.What is pip?
 30.What is Polymorphism?
 31.What is the use of pickle module?, remember the
 use of dump and load functions
 32.What is the use of recursion and what is the main two
 parts of recursion 
 33.What is pythonPath?
 34.What is the use of with keyword in python, write a python program
  to read file called test and write files and use with keyword
 35.What are the different file modes used in python?
 36.What is the use of variable * and ** in python?
 37.What is the use of help, dir function?
 38.Is python has mainfunction, how to declare it.
 39.Difference between .py and .pyc file?
 40.Difference between instance variable, class variable and
    Instance method?
 41.How to define class method and static method?
 42.Can we use self instead of any other keyword?
 43.Can we  create a function inside class without self keyword?
 43.Describe the flow of python interpreter
 44.What does the split function?
 45.What is the use of super method?
 46.What are the common built in decorators in python?
 47.What is the use of operator overloading, perform on 
   operation
 48.Difference between pass by value pass by reference
 49.What is the use of try,except,finally block ?
 50.What is the use of ennumerate function, How can we define?
 51.What is iterator and generator, what is the use of __iter__
    __next__, Is generator is like music player?

    1. Is string can be performed as iterables?
    2. can we use int as iterator?

 52.Difference between methods overloading,
    overriding
 53. How to delete a file in python?
 54. Difference between split and join
 55. How to delete files in python?
 56. What are the different methods to access 
     parent class members.
 57. * Are access speifiers are used in python?
     * What is the use of _ and __ 
 58. How can we create a class without memebers?
 59. What are the difference between new and
     override modifiers.
 60. How will you check if the class is subclass
     of another class?
 61. How can we define regular expression in python?
     What is the use of complie, search, findall 
     functions in re?

 62. * Can we use int as function and input as 
       iterables in map?
     * Can we fix range without range keyword 
       using []

 63. Can we assign muliple values to one varibale?
     How can we assign it ?
    
 64. * How can we connect sqllite with python
     * What is the use of commit and execute 
       function in python

 65. * What is pandas?
     * How can we create Dataframe?
     * Remember type of Dataframe

     * What is the use of following series methods
       and functions

       1. axes
       2. dtype
       3. empty
       4. ndim
       5. size
       6. values
       7. head()
       8. tail()

    * Can we use this all methods in Dataframe
    * What is the use of T and shape method
      in DF
    * What is the use of apply function in pandas
    * Remember basic Statatics function in pandas
 
 66. *  What is kivy?
     *  What is the four steps to create an app?

 67. How to sort multidiamensnoal array

 68. Can we sort list according to their 
     elements length, and can we sort an
     dict

 69. Can we use switch case in Python 10
'''
'''
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
'''
def LongestWord(sen):
    lenght=[len(i) for i in sen]
    return (max(lenght))

Input=list(map(str, input().split(' ')))
Input.remove(r'[0-1]')
s=LongestWord(Input)
print(s)

'''
no_of_students=int(input())
Details=[]
result=[]
for i in range(no_of_students):
    Name=input()
    marks=float(input())
    Details.append([Name,marks])

Details.sort(key=Details[1])
print(result)
'''

'''

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

class Solution:
    
    def twoSum(self,List,target):
        return
obj=Solution()
s=obj.twoSum([3,2,3],6)
print(s)
'''







