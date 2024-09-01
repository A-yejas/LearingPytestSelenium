# for i in range(10,0,-1):
#     print(i)
############
# for i in range(10):
#     if i == 5:
#         pass
#     else:
#         print(i)
#############
# for i in range(6):
#     if i ==5:
#         print(i)
####### Below code have to check version python 3.10, present is not working
# def fun(*args):
#     for i in args:
#         print(i, end='-')
# fun(*args :"yejas","amit")
####### Factorial
# n=5
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial *i
# print(factorial)
# Ans:- 120
####
# a=lambda a:'Even' if a%2==0 else'odd'
# print(a(21))
########
# def deco1(func):
#     def test():
#         print('deco1')
#         func()
#     return test
# def deco2(func):
#       def test2():
#           print('deco2')
#           func()
#       return test2
#
# @deco2
# @deco1
# def fun():
#     print(">>>>>>>>{}".format('yejas'))
#
# fun()
##########

# def adding(func):
#     def wrapper(a,b):
#         print('testinh')
#         return [a[i] + b[i] for i in range(len(a))]
#     return wrapper
# @adding
# def add(a,b):
#     return a,b
#
# a=[1,2,3]
# b=[4,5,6]
# res = add(a,b)
# print(res)
#####
# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator_repeat
#
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")
#######
# alph=['a','b','c','d','e','f','g','h','i','j','o','u']
# def vowel(list):
#     vow=['a','e','i','o','u']
#     return list in vow
#
# test = filter(vowel, alph)
# print(list(test))
##########
#pick 1 item and apply the function
#give the same number of elements
# alph=[1,2,3,4,5,6,7,8,9,10]

# def fun(n):
#     return n + 2
# list1=map(fun, alph)
# print(list(list1))
# Ans: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
######
# Filter:- Filters works as true or false conditions.
# pick if item m is true keep it, false, remove it
# it can give less number of items as compared to actual
# def fun(n):
#     return n % 2 == 0
# list1=filter(fun, alph)
# print(list(list1))
# Ans:-[2, 4, 6, 8, 10]
###########
# Recursion is a programming technique where a function calls itself in order to solve a problem
# def sum_of_digit(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         n = n * sum_of_digit(n-1)
#     return n
# print(sum_of_digit(5))
# one more example:-
# def sum_of_digit(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digit(n // 10)
# print(sum_of_digit(12345))
########## Details how it is working
# n=12345
#
# r1=n%10
# q1=n//10
# print(r1)
# print(q1)
# r2=q1%10
# q2=q1//10
# print(r2)
# print(q2)
# r3=q2%10
# q3=q2//10
# print(r3)
# print(q3)
# r4=r3%10
# q4=q3//10
# print(r4)
# print(q4)
# r5=r4%10
# q5=q4//10
# print(r5)
# print(q5)
# print(r1+r2+r3+r4)
##One more method in same
# def sum_of_digit(n):
#     sum_digits = 0
#     while n > 0:
#         sum_digits += n%10
#         n = n//10 #quotient
#         # / :- div
#         # // :- quotient
#         # % "- Remainder
#     return sum_digits
# print(sum_of_digit(12345))
###### OPPS :- >>>>>>>>>>>>>>>>>>>>>>>>>>
# Object:-
# An object is an instance of a class, created and using the class as a template.
# Objects have their own unique state and can access the attributes and behaviors defined in the class.
# Classes  provide a way to organize and structure code, enabling code reusability and modular design.
##Constructor:-
# 1.Constructor is a special method which is invoked automatically at the time of object creation.
# 2.it is used to initilize the data members of the new objects generally.
# 3.Constructors have the same name as class or structure.
# 4.Constructor dont have a return type.(Not even void).
# 5.Constructor are only called once, at object creation.
# def __init__()   ->default constructor
# Constructor which has parameters is called a parameterized constructor.it is used to provide different values&distinct objects
# def __init__(self,name,id)  --> parameterize constructor

##Encapsulation:-
# In python every thing is an public, is availbel every where
# __Private :- Private things are not allowwed to access the out of the class but Private things basically allowed
# _Protect:-  prodtect available with in the modules
#to things in class.
# class Car:
#     name = None
#     password =123
#     def __init__(self):
#         print("i am auto")
#     # def change_pwd(self):
#     #     self.password=456
#
# vehcle=Car()
# vehcle.password='345'
# vehcle.change_pwd()
# print(vehcle.password)
#####
# class Car:
#     name = None
#
#     def __init__(self):
#         self.public='public'
#         self.__private= 'pass@123'
#         self._protect='protect123'
#
#         print("i am auto")
#     def __private_method(self):
#         print('private')
#     def printName(self):
#         self.__private_method()
#         if self.__private_method == '123':
#             print('Hi',123)
#         print('I am public')
# alto = Car()
# alto.printName()
#Real Time Example
#
# class login:
#
#     def __init__(self,email,password,name):
#         self._email=email
#         self.__password = password
#         self.name = name
#     def allow_to_change(self):
#         if self._email=='yejas@gmail.com' and self.__password=="pwd@123":
#             print("allowed")
#         else:
#             print("not allowed")
#
# call=login('yejas@gmail.com', 'pwd@123', 'yejas')
# call.allow_to_change()
# print(list(call))
####Inheritance user super metchod call the functions
# class Father:
#     def home(self):
#         print('Father Homes')
# class Children(Father):
#     def home(self):
#         super().home()
#         print('Children Home')
# obj = Children()
# obj.home()
##Exception:
# An exception as an event that occurs during the execution of program that disrupts the normal
# flow of instructions
# ------------------
#gitpath name:- https://github.com/PramodDutta/Py3xATBLearning/blob/main/ex02_July/24072024/test_Lab186.py


# -----
import pytest
'''
when ever you run the tests first run the conftest.py file
---> .gitignore file works which dont want to push in git repositrory
'''
import pytest

@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@pytest.mark.smoke
def test_sub2():
    assert 1 - 1 == 0


@pytest.mark.sanity
def test_sub3():
    assert 0 - 0 != 0

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 == 0
