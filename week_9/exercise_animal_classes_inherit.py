'''
Exercise Animals Inheritance:
Use the file animals.csv to read information about animals.

Part a)
Produce a class structure where Dog, Cat and Snake are implemented as child classes of a base class Animal. Create the object variables in the base class, along with a method 'print_basic_information', which prints 'type' and 'name' to the console.
In each child class, use the base class constructor with 'super' and add an additional method 'speak', specific to that child class.
In each child class, add an additional method where you return the sum of the object variables 'age' and 'legs'.

For each element in the animals.csv, create an object of the corresponding subclass, let it print basic information (method from 'Animal'), let it speak (method from child class) and get the sum of 'age' and 'legs' as a return value.

Part b)
Often, there are many different solutions how one can solve a particular task. Ideas like code readability and avoiding code duplication become more important in more complex applications. Do you find a way to reduce code duplication in the structure of part a)?

Part c)
Override the 'print_basic_information' method in the child class Dog by using the class name as a parameter instead of self.animal_type. You can access the name of the class by self.__class__.__name__
'''

#%%  Base Class
class Animal(object):

    def __init__(self, animal_type, name, age, weight, legs):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs

    def say_hi(self):
        print(f"Hi, I'm a {self.animal_type} and my name is {self.name}!")


#%%  Child Classes

class Dog(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("Wuff, wuff!")

    def sum_of_age_and_legs(self):
        value = self.age + self.legs
        return value

class Cat(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("Miaou!")

    def sum_of_age_and_legs(self):
        value = self.age + self.legs
        return value


class Snake(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("SSsshh, SSsshh!")

    def sum_of_age_and_legs(self):
        value = self.age + self.legs
        return value


#%% solution with file loop
obj_list = []
with open('/week_9/animals.csv') as f:
    for line in f.readlines()[1:]:
        animal_type = line.split(", ")[0]
        name = line.split(", ")[1]
        age = int(line.split(", ")[2])
        weight = int(line.split(", ")[3])
        legs = int(line.split(", ")[4])
        # create objects based on animal_type
        # add objects to obj_list
        if animal_type == 'dog':
            obj = Dog(animal_type, name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'cat':
            obj = Cat(animal_type, name, age, weight, legs)
            obj_list.append(obj)
        if animal_type == 'snake':
            obj = Snake(animal_type, name, age, weight, legs)
            obj_list.append(obj)


for elem in obj_list:
    print("--\n")
    elem.say_hi()
    elem.speak()
    c_sum = elem.sum_of_age_and_legs()
    print(c_sum)

# PART A için doğru test
first = obj_list[0]
first.speak()

second = obj_list[1]
second.say_hi()   # <-- print_basic_information() yok, say_hi() var

obj = Dog("dog", "Bello", 5, 20, 4)
obj.say_hi()      # <-- yine say_hi() kullanılacak


#%%  Part b) ve c) - Kod tekrarını azaltılmış + override yapılmış final çözüm

class Animal():

    def __init__(self, animal_type, name, age, weight, legs):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs

    def print_basic_information(self):
        # Base class versiyonu
        print("Hi, I'm a {} and my name is {}!".format(self.animal_type, self.name))

    def sum_of_age_and_legs(self):
        # Artık tüm çocuk sınıflar aynı kodu kullanıyor → kod tekrarı yok
        return self.age + self.legs


class Dog(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("Wuff, wuff!")

    # ---- OVERRIDE EDİLMİŞ METOT ----
    def print_basic_information(self):
        # Aşağıdaki satır ile sınıf adını otomatik yazdırıyoruz:
        # "Dog", "Cat" vs.
        print("Hi, I'm a {} and my name is {}!"
              .format(self.__class__.__name__, self.name))

        # | Kod                       | Anlamı                                |
        # | ------------------------- | ------------------------------------- |
        # | self                      | Nesnenin kendisi                      |
        # | self.__class__            | Nesnenin sınıfı (Dog, Cat, Snake…)    |
        # | self.__class__.__name__   | Sınıfın adı string olarak (“Dog”)     |
        # ---------------------------------------------------------------


class Cat(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("Miaou!")


class Snake(Animal):

    def __init__(self, animal_type, name, age, weight, legs):
        super().__init__(animal_type, name, age, weight, legs)

    def speak(self):
        print("SSsshh, SSsshh!")


#%% Nesneleri dosyadan oluşturma
obj_list = []
with open('/week_9/animals.csv') as f:
    for line in f.readlines()[1:]:
        animal_type, name, age, weight, legs = line.strip().split(", ")
        age = int(age)
        weight = int(weight)
        legs = int(legs)

        if animal_type == "dog":
            obj = Dog(animal_type, name, age, weight, legs)
        elif animal_type == "cat":
            obj = Cat(animal_type, name, age, weight, legs)
        elif animal_type == "snake":
            obj = Snake(animal_type, name, age, weight, legs)

        obj_list.append(obj)

for elem in obj_list:
    print("--\n")
    elem.print_basic_information()
    elem.speak()
    print(elem.sum_of_age_and_legs())


first = obj_list[0]
first.speak()

second = obj_list[1]
second.print_basic_information()

obj = Dog("dog", "Bello", 5, 20, 4)
obj.print_basic_information()

# Hi, I'm a Dog and my name is Bello! --> override çalışıyor
# Hi, I'm a dog and my name is Bello! --> eğer overrride çalışmasaydı
