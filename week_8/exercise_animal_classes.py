'''
Exercise Animals:
Use the file animals.txt to read information about animals.

Part a)
For each animal, print "Hi, I'm a {animal_type} and my name is {name}!"
Solve the exercise by writing a class 'Animal' and adding a method allowing to print the requested string. Note that it is not necessary for this task, to differentiate between animal types!
'''


print("Part a): \n\n")
class Animals:
    animal_list = []  # class attribute – tüm hayvanları saklar

    def __init__(self, animal_type, name, age, weight, legs):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        Animals.animal_list.append(self)  # her yeni nesneyi listeye ekle

    def say_hi(self):
        print(f"Hi, I'm a {self.animal_type} and my name is {self.name}!")


with open('/week_8/animals.csv') as f:
    for line in f.readlines()[1:]:  # başlık satırını atla
        parts = line.strip().split(",")
        animal_type = parts[0]
        name = parts[1]
        age = int(parts[2])
        weight = float(parts[3])
        legs = int(parts[4])

        # create objects
        obj = Animals(animal_type, name, age, weight, legs)

for i in Animals.animal_list:
    i.say_hi()



'''
Part b)
Now we are interested in the various sounds the animal types make.
Write a separate class for each animal type. Provide a method "speak", which depending on the animal type prints different sounds.
'''

print("\n\nPart b): \n\n")

class Dog:
    animal_list = []

    def __init__(self, name, age, weight, legs):
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        self.speak = "havhav"
        Dog.animal_list.append(self)

    def say_hi(self):
        print(f"Hi, I'm a dog and my name is {self.name} and ı say  {self.speak}!")


dog1 = Dog("Max", 5, 20, 4)
dog1.say_hi()


class Dog:
    animal_list = []  # tüm hayvan nesnelerini tutan liste

    def __init__(self, name, age, weight, legs):
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        self.speak = "Hav hav!"   # köpek sesi
        Dog.animal_list.append(self)

    def say_hi(self):
        print(f"Hi, I'm a dog and my name is {self.name}!")
        print(f"I say: {self.speak}\n")


class Cat:
    def __init__(self, name, age, weight, legs):
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        self.speak = "Meow!"   # kedi sesi

    def say_hi(self):
        print(f"Hi, I'm a cat and my name is {self.name}!")
        print(f"I say: {self.speak}\n")


class Snake:
    def __init__(self, name, age, weight, legs=0):  # yılanın bacağı yok
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        self.speak = "Ssssss..."   # yılan sesi

    def say_hi(self):
        print(f"Hi, I'm a snake and my name is {self.name}!")
        print(f"I say: {self.speak}\n")









#%% solution with file loop
obj_list = []
with open('./animals.csv') as f:
    for line in f.readlines()[1:]:
        animal_type = line.split(", ")[0]
        name = line.split(", ")[1]
        age = int(line.split(", ")[2])
        weight = int(line.split(", ")[3])
        legs = int(line.split(", ")[4])
        #create objects
        if animal_type == 'dog':
            obj = Dog(name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'cat':
            obj = Cat(name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'snake':
            obj = Snake(name, age, weight, legs)
            obj_list.append(obj)

for elem in obj_list:
    elem.speak()
