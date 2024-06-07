# class Student:
#     def __init__(self,name,age,mark):
#         self.name=name
#         self.age=age
#         self.mark=mark

# def main():
#     s1=Student("Jack",18,400)
#     print(s1)
#     print(s1.name)
#     print(s1.age)
#     print(s1.mark)
    
#     print()
#     s2=Student("Naing",20,440)
#     print(s2.name)
#     print(s2.age)
#     print(s2.mark)
    
# main()
# ________________________________________________________________
# method
# class Student:
#     def __init__(self,name,age,mark):
#         self.name=name
#         self.age=age
#         self.mark=mark
#     def result(self):
#         if self.mark>=240:
#             return "pass"
#         else:
#             return "fail"
# def main():
#     s1=Student("tom",24,360)
#     s2=Student("jack",22,210)
#     print(s1.result())
#     print(s2.result())

# main()
# ________________________________________________________________
# method exercise
# class Man:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def old_or_not(self):
#         if self.age>=65:
#             return "old"
#         else:
#             return "not old"
# def main():
#     m1=Man("John",45)
#     m2=Man("U Hla",84)
#     m3=Man("Luke",78)
#     m4=Man("Tom",34)
    
#     mans=[m1,m2,m3,m4]
#     old_man=[]
#     not_old_man=[]
#     man_result={}
    
#     for x in mans:
#         if x.old_or_not()=="old":
#             old_man.append(x.name)
#             man_result["old_man"]=old_man
#         else:
#             not_old_man.append(x.name)
#             man_result["not_old_man"]=not_old_man
    
#     print(man_result)
    
# main()
# ________________________________________________________________
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
    
#     def discount(self,discountval):
#         discountAmount=(self.price/100)*discountval
#         final_price=self.price-discountAmount
#         return final_price
# def main():
#     latptop=Product("Lenovo",1000000)
#     print(latptop.discount(20))

# main()
# ________________________________________________________________
# class Student:
#     gender="male"
#     def __init__(self,name,age,mark,*other,**detail):
#         self.name=name
#         self.age=age
#         self.mark=mark
#         self.other=other
#         self.detail=detail
# def main():
#     s1=Student("mg mg",18,200,34,234,234,234,myanmar=190)
#     print(s1.name)
#     print(s1.age)
#     print(s1.mark)
#     print(s1.other)
#     print(s1.gender)
#     print(s1.detail)
#     print(Student.gender)

# main()
# ____________________________________________________________________________
# class Circle:
#     pi=3.142
#     def __init__(self,radius):
#         self.radius=radius
#     def circle_circum(self):
#         formula=2*Circle.pi*self.radius
#         return formula
#     def circle_area(self):
#         formula=Circle.pi* (self.radius**2)
#         return formula
    
# def main():
#     c1=Circle(10)
#     c2=Circle(20)
    
#     print(c1.circle_area())
#     print(c1.circle_circum())
#     print(c2.circle_area())
#     print(c2.circle_circum())
#     print()
    
#     print(c1.__dict__)
#     print(c2.__dict__)
#     print()
    
#     c1.radius=50
#     print(c1.__dict__)
#     print(c1.circle_area())
# main()
# _______________________________________________________
class Student:
    other="Star"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @staticmethod
    def printstatement():
        return 'this is staticmethod'
    @classmethod
    def anotherstatement(cls,other):
        return f'{cls.other} is classmethod'
def main():
    s1=Student("Kitty",29)
    print(s1.__dict__)
    print(s1.printstatement())
    print(s1.anotherstatement('sample'))

main()

