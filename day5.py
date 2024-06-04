# def main():
#     animals=("dog","cat","tiger","monkey","lion")
    
#     number_of_animal=len(animals)
    
#     print(number_of_animal)
    
#     print(animals[0])
#     print(animals[3])
#     print()
    
#     for animal in animals:
#         print(animal)
#     print()
    
#     for i in range(0,len(animals)):
#         print(animals[i])

# main()
# _______________________________________________________
# # unpacking tuple
# def main():
#     elements=(True,1,2.3,"hello")
    
#     (is_raining,apple,weight,greet)=elements
#     print(is_raining)
#     print(apple)
#     print(weight)
#     print(greet)
    
#     fruits=('apple','orange','grape','bannana','lime','pineapple')
#     (fruit1,fruit2,fruit3,*otherfruits)=fruits
#     print(fruits)
#     print(fruit2)
#     print(fruit3)
#     print(otherfruits)
#     print(type(otherfruits))
# main()
# ________________________________________________________
# def main():
#     animals=("goat","sheep","dog","elephant")
    
#     print(animals[1])
#     print(animals[1:3])
#     print(animals[0:3])
#     print()
#     print(animals[-1])
#     print(animals[-3:-1])
    
#     extract=animals[0:2]
#     print(extract)
    
#     text="I am a boy"
#     print(text[3])
#     print(text[0:3])
# main()
# ____________________________________________________
def main():
    num=1,2,3,4,5,6,7,8,9,10,3
    print(len(num))
    print(min(num))
    print(max(num))
    
    print(num.count(3))
    print(num.index(9))
    
    print(num+(100,200))
    print((1,2)*3)
    
    a=2,3
    b=(2,)
    print(a,type(a))
    print(b,type(b))
main()