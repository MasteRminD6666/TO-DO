
# def prime(number):
#     for i in range(2, number):
#         if number %i ==0:
#             return False
#
#         else:
#             return True
#
# print(prime(2))
# def isprime (num):
#      for i in range(2,num):
#          if (num%i) == 0:
#              return False
#          if num ==2:
#              return True
#          else:
#              return True
# print(isprime(3))
#
# def ispr(num , j):
#     if num<2 :
#         return False
#     if num == j:
#         return True
#     if (num%j)==0:
#         return False
#     return ispr(num,j+1)
#
# def multiply(a,b):
#     count =0
#     for i in range(1 , b+1):
#
#         count = count+a
#     return count
# print(multiply(5,0))
#
# def multiply(a,b):
#     if b == 0:
#         return 0
#     if b == 1:
#         return a
#     else:
#          return  a + multiply(a,b-1)
# print(multiply(4,4))
x = 0
class Girl():
    calls_var = 'class varible'
    def __init__(self , name , age):
        self.names = name
        self.age = age


    def semsma(self):
        print(f"im {self.names} And my Age is {self.age}")


class Khaloooody(Girl):
    def __init__(self):
        super().__init__('khaloody' ,24)



    def semsma(self):
        print ( f"im {self.names} And my Age is {self.age}" )



man = Khaloooody( )
girl = Girl("Simsma" , 24)

man.semsma()
girl.semsma()
test = Girl('test', 22)
test.semsma()



