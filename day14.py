# class Map:
#     def __init__(self,location,atm):
#         self.loaction=location
#         self.atm=atm
    
#     def draw(self):
#         return f"draw line at {self.loaction}"

# def main():
#     map1=Map((12.32,23.23),4)
#     print(map1)
#     print(map1.__dict__)
#     print(map1.draw())
# main()
# _____________________________________________________________________
# class House:
#     roof=True
    
#     def __init__(self,doors,windows,floors):
#         self.doors=doors
#         self.windows=windows
#         self.floors=floors
        
#     def clean_roof(self):
#         if self.roof:
#             return 'cleaning roof'
#         else:
#             return 'no roof to be cleaned'

# def main():
#     house1=House(4,16,3)
#     print(house1.clean_roof())
#     print(House.__dict__)
#     print(house1.__dict__)
#     print()
    
#     house1.roof=False
#     print(house1.clean_roof())
# main()
# ___________________________________________________________________
# class House:
#     roof=True
    
#     def __init__(self,doors,windows,floors):
#         self.doors=doors
#         self.windows=windows
#         self.floors=floors
        
#     def clean_roof(self):
#         if self.roof:
#             return 'cleaning roof'
#         else:
#             return 'no roof to be cleaned'
        
#     @classmethod
#     def mymethod(cls,roof):
#         cls.roof=roof
    
#     @staticmethod
#     def leaving_house(time_of_day):
#         return f'leaving house at {time_of_day}'
    
# def main():
#     house1=House(5,15,3)
#     House.mymethod(False)
#     print(House.roof)
#     print()
#     print(house1.leaving_house('2 pm'))
    
# main()
# ___________________________________________________________________
# inheritance

# class Car:
#     def __init__(self,wheels,doors,engine):
#         self.wheels=wheels
#         self.doors=doors
#         self.engine=engine
    
#     @staticmethod
#     def drive():
#         return f"driving"
    
#     @staticmethod
#     def brake():
#         return f'braking'
    
# class Suzuki(Car):
#     def __init__(self, wheels, doors, engine,fourwheeldrive):
#         super().__init__(wheels, doors, engine)
#         # Car.__init__(self,wheels,doors,engine)
#         self.fourwheeldrive=fourwheeldrive
    
#     @staticmethod
#     def drive():
#         return f'driving suzuki'
  
# def main():
#     suzuki=Suzuki(4,4,'fast',True)
#     car=Car(4,4,'fast')
    
#     print(car.drive())
#     print(suzuki.drive())
# main()
# __________________________________________________________________________________
# composition
class Processor:
  
  def __init__(self,core,speed):
    self.core=core
    self.speed=speed
  
  @staticmethod
  def processing():
    print('Processing -> processing')

class Ram:
  def __init__(self,capacity,speed):
    self.capacity=capacity
    self.speed=speed

  @staticmethod
  def storing():
    print('Ram -> storing')

class Motherboard:
  
  def __init__(self,dimm_slots,pci_slots):
    self.dimm_slots=dimm_slots
    self.pci_slots=pci_slots
  
  @staticmethod
  def controlling():
    print('Motherboard -> controlling')

class Computer:

  def __init__(self,processor,ram,motherboard):
    self.processor=processor
    self.ram=ram
    self.motherboard=motherboard

  @staticmethod
  def boot():
    print('Computer -> booting')

computer=Computer(Processor(4,3),Ram(8,266),Motherboard(4,3))
print(computer.boot())
print(computer.processor.processing())
print(computer.ram.storing())
print(computer.motherboard.controlling())