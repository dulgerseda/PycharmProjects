from networkx.algorithms.approximation.distance_measures import diameter
from pyparsing import empty


class Car:
    """
    My documentation
    """
    car_nr=0 #class varibles

    def __init__(self, brand, color):
        print("Hello I am a car")
        self.brand = brand
        self.color = color
        Car.car_nr += 1

mycar=Car("BMW", "red")

print(mycar.brand)
print(mycar.color)

print(Car.car_nr)
print(mycar.car_nr)

#----------------------------------------

class Square:

    obj_nr=0
    ref_list=[]

    def __init__(self, lenght_of_side):
        self.lenght = lenght_of_side
        Square.obj_nr += 1
        Square.ref_list.append(self)


    def calculate_area(self):
        return self.lenght*self.lenght

    @classmethod
    def gm(cls):
        return cls.obj_nr

Square.gm()

one = Square(1)
print(one.lenght)

two = Square(2)
print(two.lenght)
print(one.obj_nr)


#-----------------
class Square:

    obj_nr=0
    ref_list=[]

    def __init__(self, lenght_of_side):
        self.lenght = lenght_of_side
        Square.obj_nr += 1
        Square.ref_list.append(self)

    def calculate_area(self):
        return self.lenght*self.lenght

    @staticmethod
    def calculate_area(self):
        return self.lenght * self.lenght

    @classmethod
    def c_area(cls,side_lenght):
        if cls.obj_nr > 3:
            return 0
        else:
            return side_lenght*side_lenght

one = Square(1)
two = Square(2)
print(one.lenght)
#-----------------

class Square:

    def __init__(self, length_of_side):
        self.length = length_of_side

    def calculate_area(self):
        return self.length * self.length

    def __str__(self):
        return "hello I am a square"


# Bir Square nesnesi oluştur
one = Square(10)
print(one)                   # hello I am a square
print(one.calculate_area())  #100

#-----------------solution
class Cylinder:

    set_level=100

    def __init__(self, diameter, height, empty=True):
        self.diameter = diameter
        self.height = height
        self.empty = empty
        self.level = 0

    def fill(self):
        if self.empty == True:
            self.level = Cylinder.set_level
            self.empty = False
            return self.level
        else:
            return self.level

    def release(self):
        if self.empty == True:
            return Cylinder.set_level
        else:
            self.level -= 10
            if self.level <= 0:
                self.level = 0
                self.empty = True
            return self.level

    def calculate_weight(self):
        return self.diameter * self.height * 0.001

c1 = Cylinder(10, 20)
print(c1.fill())              # 100
print(c1.release())           # 90
print(c1.calculate_weight())  # 0.2

#-----------------explain

class Cylinder:

    set_level = 100   # tüm silindirler için maksimum seviye (class variable)

    def __init__(self, diameter, height, empty=True):
        self.diameter = diameter    # çap (m)
        self.height = height        # yükseklik (m)
        self.empty = empty          # boş mu dolu mu bilgisi
        self.level = 0              # doluluk oranı (%)

    def fill(self):
        if self.empty == True:
            self.level = Cylinder.set_level  # doldur
            self.empty = False               # artık dolu
            return self.level                # 100 döndürür
        else:
            return self.level                # zaten doluysa seviyesi değişmez

    def release(self):
        if self.empty == True:
            return Cylinder.set_level        # boşsa 100 döndürür
        else:
            self.level -= 10                 # 10 azalt
            if self.level <= 0:
                self.level = 0
                self.empty = True            # artık boş
            return self.level                # yeni seviye döner

    def calculate_weight(self):
        # çok basit hacim tahmini: çap * yükseklik * 0.001
        return self.diameter * self.height * 0.001

    def __str__(self):
        return f"Cylinder(diameter={self.diameter}, height={self.height}, level={self.level}, empty={self.empty})"

c1 = Cylinder(10, 20)
print(c1)

#-----------------methods

class Cylinder:

    set_level = 100   # class variable (tüm silindirler için ortak)

    def __init__(self, diameter, height, empty=True):
        self.diameter = diameter    # instance variable
        self.height = height        # instance variable
        self.empty = empty          # instance variable
        self.level = 0              # instance variable

    def fill(self):                 # instance method
        if self.empty == True:
            self.level = Cylinder.set_level
            self.empty = False
            return self.level
        else:
            return self.level

    def release(self):              # instance method
        if self.empty == True:
            return Cylinder.set_level
        else:
            self.level -= 10
            if self.level <= 0:
                self.level = 0
                self.empty = True
            return self.level

    def calculate_weight(self):     # instance method
        return self.diameter * self.height * 0.001

    @staticmethod
    def convert_liters_to_kilos(liters):    # static method
        """Yoğunluğu 1 kg/L kabul ederek litreyi kilograma çevirir."""
        return liters * 1                   # 1 litre = 1 kg

    def __str__(self):              # special instance method
        return f"Cylinder(diameter={self.diameter}, height={self.height}, level={self.level}, empty={self.empty})"


c1 = Cylinder(10, 20)
print(c1)

print(c1.fill())                    # 100
print(c1.release())                 # 90
print(c1.calculate_weight())        # 0.2
print(Cylinder.convert_liters_to_kilos(5))  # 5


class Cylinder:
    # class variable → tüm silindirler için ortak maksimum seviye (100)
    set_level = 100

    # instance method → her silindir nesnesi oluşturulduğunda çalışır
    def __init__(self, diameter, height, empty=True):
        self.diameter = diameter     # instance variable (çap)
        self.height = height         # instance variable (yükseklik)
        self.empty = empty           # instance variable (boş mu dolu mu)
        self.level = 0               # instance variable (doluluk oranı %)

    # instance method → silindiri doldurur
    # Eğer boşsa: seviye 100 yapılır, empty False olur, 100 döner.
    # Eğer zaten doluysa: seviyesi değişmeden mevcut değer döner.
    def fill(self):
        if self.empty == True:
            self.level = Cylinder.set_level
            self.empty = False
        return self.level

    # instance method → silindiri 10 birim boşaltır
    # Eğer boşsa: maksimum seviye (100) döndürür.
    # Eğer doluysa: level 10 azalır, 0 olursa empty True yapılır.
    def release(self):
        if self.empty == True:
            return Cylinder.set_level
        else:
            self.level -= 10
            if self.level <= 0:
                self.level = 0
                self.empty = True
            return self.level

    # instance method → basit ağırlık hesaplaması (örnek formül)
    def calculate_weight(self):
        return self.diameter * self.height * 0.001

    # static method → litreyi kilograma çevirir (bağımsız işlem)
    @staticmethod
    def convert_liters_to_kilos(liters):
        return liters * 1

    # special method → print(c1) çağrıldığında nesneyi okunabilir şekilde gösterir
    def __str__(self):
        return f"Cylinder(diameter={self.diameter}, height={self.height}, level={self.level}, empty={self.empty})"

c1 = Cylinder(10, 20)
print(c1)

"""fill() is an instance method because
 it accesses object-specific data (self.level) through
 the self parameter."""

"""convert_liters_to_kilos() is a static method because 
it does not use self or cls and works independently 
of any object."""







