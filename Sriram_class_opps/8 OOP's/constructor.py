## Uusing constructor we can create instance varables.
# class One():
#     def __init__(self):
#         pass
#     def add(self, uname, password):
#        print('\n ADD ', uname , password)
#
#     def sub(self, uname, password, hostname,port):
#         print(uname, password )
#
#     def mul(self, uname, password):
#         print(uname, password )
# inst = One()
# inst.add(10,20)
# inst.sub(10,20,'admin', 23)
# inst.mul(10,20)

class One():
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        print('__INIT__')

    def add(self):
       print(self.uname , self.password)
       
    def sub(self, hostname,port):
        print(self.uname, self.password )

    def mul(self):
        print(self.uname, self.password )

inst = One('admin','admin123')
inst.add()
inst.sub('admin', 23)
inst.mul()
