# print('Hellow World')
# a=10
# b=input("Vale is:" +str(a))
#-----------
###len() start from 1 , index starts from 0
'''
values=[1,2,'Yejas',3,4]
print(values[1:])
print(len(values))
print(values.index('Yejas'))
# print(values.insert(3,'Ahmad')) #Ans is :- [1, 2, 'Yejas', 'Ahmad', 3, 4]
# print(values)
print(values.append('Test')) #adding at end
# print(values)
values[2] = 'Test' ##Updating
print(values)
del values[0]
print(values)
'''
# jump for loop
# for i in range(1,10,2):
#     print(i)
###WHile Loop
# i = 4
# while i>1:
#     print(i)#(Infinite loop)
######
# i=4
# while i > 1:
#     print(i)
#     i -=1
##########
# i =4
# while i>1:
#     if i !=3:
#         print(i)
#     i -=1

#Break :- Break the iteration
#continue:- Skip the current iteration and continue with next iteration
# i=10
# while i>1:
#     if i == 9:
#         i=i-1
#         continue
#     if i == 3:
#         break
#     print(i)
#     i =i-1
#######--------------------------Opps
'''
Constructor:- Means is a one method which   is automatically when uou create  the object  for any class
Declare a constructor in python "__init__"
1.Self is :- Mandatory when you declare the method inside the class.
2.Self is nothing but object , that object passes as a first argument that called as self  in pythond
standards.
3, self keyword is mandatory for calling variable names into method
4.instance variables and class variables have whole different purpose.
5.constructor name should be "__init_".
----------------------Inheritance
What is mean by inheritance,
1.Acquaring properties of  parent class
'''

class A():
    def add(self):
        print('\n A Add is')

class B(A):
    def add(self):
        print('\n B add is')

class C(B):
    def add(self):
        print(' \n C add is ')
inst = B()
inst.add()


