

class MyClass():  # Yeni bir sınıf tanımlıyoruz (MyClass)

    def __init__(self):  # Yapıcı (constructor) metot
        print("I'm created.")  # Nesne oluşturulunca bu mesajı yazdırır


myobj = MyClass()  # MyClass sınıfından bir nesne (object) oluşturduk
# Çalışınca __init__() otomatik olarak çağrılır ve
# ekrana "I'm created." yazar

print(myobj.__str__())  # __str__() metodunu çağırıyoruz.
# Ama biz MyClass içinde tanımlamadık,
# bu yüzden Python 'object' sınıfındaki
# varsayılan __str__() metodunu kullanır.
# O da nesnenin RAM adresini döndürür:
# <__main__.MyClass object at 0x77395433c040>

#---------------------------

class MyClass():
    def mymethod(self):
        print("Hello")

myobj = MyClass()     # init() yok ama Python varsayılan birini kullanıyor
myobj.mymethod()      # metodu çağırdığında "Hello" yazıyor

#--------------------------------------

class MyClass():
    def __init__(self, name):
        self.name = name
        print("Hello, I'm created")


class SubClassOne(MyClass):
    def __init__(self, name, length):
        super().__init__(name)       # Üst sınıfın (MyClass) constructor'ını çağırıyor
        self.length = length         # Ekstra özellik (sadece bu alt sınıfta var)


class SubClassTwo(MyClass):
    def __init__(self, name, width):
        super().__init__(name)       # Üst sınıfın (MyClass) constructor'ını çağırıyor
        self.width = width           # Ekstra özellik (sadece bu alt sınıfta var)


one = SubClassOne('AndreasOne', 2)
two = SubClassTwo('AndreasTwo', 114)

two.lenght    # yanlış (hem yazım hatası hem de bu sınıfta length yok)
two.length    # yanlış (çünkü SubClassTwo'da "width" var)

#---------------------------------

class MyClass():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        print("Hello, I'm created")

class SubClassOne(MyClass):
    def __init__(self, name, length):
        super().__init__(name, "One")   # Burada ikinci argüman "One" olarak sabitlenmiş
        self.length = length

one = SubClassOne('AndreasOne', 2)
# Hello, I'm created

#---------------------------------

class MyClass():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        print("Hello, I'm created")


class SubClassOne(MyClass):
    def __init__(self, name, lastname, length):
        super().__init__(name, lastname)   # Üst sınıfın (MyClass) __init__'ini çağırıyor
        self.length = length               # Bu sınıfa özel yeni bir özellik ekleniyor


one = SubClassOne('AndreasOne', 'One', 2)

#---------------------------------

class MyClass():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        print("Hello, I'm created")

    def __str__(self):                     # Nesne yazdırıldığında çağrılır
        return f"MyClass: {self.name} {self.lastname}"


class SubClassOne(MyClass):
    def __init__(self, name, lastname, length):
        super().__init__(name, lastname)   # Parent sınıfın constructor'ını çağırır
        self.length = length               # Yeni özellik

    def __str__(self):                     # Üstteki __str__ metodunu override ediyoruz
        return f"SubClassOne: {self.name} {self.lastname}, Length = {self.length}"


# Nesne oluşturma
one = SubClassOne('AndreasOne', 'One', 2)

# Çıktılar
print(one.name)        # AndreasOne
print(one.lastname)    # One
print(one.length)      # 2
print(one)             # __str__() metodunu otomatik çağırır
# SubClassOne: AndreasOne One, Length = 2

"""
✔ Parent constructor → super() ile çağrıldı
✔ Alt sınıflar → kendi özelliklerini ekledi
✔ __str__() → override edildi
✔ Nesneler → doğru attribute’lara sahip
✔ Sınavlık bir OOP örneği
✔ Hem inheritance hem override net gösteriyor"""

#---------------------------------

class MyClass():
    def __init__(self, name):
        self.name = name
        print("Hello, I'm created")

    def say_my_name(self):
        print(self.name)


class SubClassOne(MyClass):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length


one = SubClassOne('Ramon', 2)
one.say_my_name()

two = SubClassOne('Andreas', 2)
two.say_my_name()

#---------------------------------
class MyClass():
    def __init__(self, name):
        self.name = name
        print("Hello, I'm created")

    def say_my_name(self):
        print(self.name)


class SubClassOne(MyClass):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

one = SubClassOne('Ramon', 2)
one.say_my_name()


class SubClassTwo(MyClass):
    def __init__(self, name):
        super().__init__(name)

    def say_my_name(self):
        super().say_my_name()    # Üst sınıftaki metodu çağırır
        print("-------")         # Ekstra bir şey ekler

two = SubClassTwo('Andreas')
two.say_my_name()


#----------------------------------------------

class NameClass():
    def __init__(self, name):
        # Public (her yerden erişilebilir)
        self.name = name

        # Protected (genellikle sadece sınıf ve alt sınıflar kullanır)
        self._name_sub = name + "_sub"

        # Private (sadece sınıf içinde erişilebilir)
        self.__name_current_only = name + "_current_only"

    def say_my_name(self):
        print(self.name)

    def change_current_name_only(self):
        # Private değişkenin değerini sınıf içinden değiştirme
        self.__name_current_only = "Hello"


# Nesne oluşturuluyor
myobj = NameClass("andreas")

# -------------------------------
# 1️⃣ Public değişkene erişim
print(myobj.name)
# Çıktı: andreas  (her yerden erişilebilir)
# -------------------------------

# 2️⃣ Protected değişkene erişim
print(myobj._name_sub)
# Çıktı: andreas_sub  (dışarıdan erişebilirsin ama tavsiye edilmez)
# -------------------------------

# 3️⃣ Private değişkene doğrudan erişim (hata verir)
# print(myobj.__name_current_only)
# AttributeError: 'NameClass' object has no attribute '__name_current_only'
# -------------------------------

# 4️⃣ Private değişkene dolaylı erişim (name mangling)
print(myobj._NameClass__name_current_only)
# Çıktı: andreas_current_only
# -------------------------------

# 5️⃣ Private değişkenin değerini sınıf içinden değiştirme
myobj.change_current_name_only()
print(myobj._NameClass__name_current_only)
# Çıktı: Hello


# -------- 1) STRING EXAMPLE --------
class MyStr(str):
    def bi_rev(self):
        print(self.upper())
        print(self.lower())
        print(self.capitalize())
        print(self.title())
        print(self[:-5])
        return self[::-2]     # sondan başlayıp her 2. karakter

txt = MyStr("z!me ngosdf nsjir zbgocjx aewh!T")
print(txt.bi_rev())



# -------- 2) LIST EXAMPLE --------
class MyList(list):
    def last_two(self):
        print(self[-2])
        print(self[1:3])
        print(self[:-2])
        return self[-2:]      # son iki eleman

lst = MyList([10, 20, 30, 40, 50])
print(lst.last_two())


# -------- 3) INT EXAMPLE --------
class MyInt(int):
    def squared(self):
        return self * self    # kendisiyle çarp

num = MyInt(7)
print(num.squared())



# ---------- musicians with class structure -----------

class Musician:
    def __init__(self, first_name, last_name, artist_name):
        self.first = first_name
        self.last = last_name
        self.artist = artist_name.upper()

    def __str__(self):
        return f"{self.first} {self.last} ({self.artist})"

    # EXTRA → override olmayan özel print methodu
    def pretty_print(self):
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Artist Name: {self.artist}")


input_path = "/week_9/musiciansclass.txt"
output_path = "/week_9/musiciansclass2.txt"

musicians = []    # list of Musician objects

with open(input_path, "r") as f:
    lines = [line.strip() for line in f]

for i in range(0, len(lines), 3):
    first = lines[i]
    last = lines[i + 1]
    artist = lines[i + 2]

    musician_obj = Musician(first, last, artist)
    musicians.append(musician_obj)

print(musicians) # location of the data

print(musicians[0].first)
print(f"first name: {musicians[0].first}") # sadece instance variablelara erişiyoruz. str, rpr, override yok.

for m in musicians:
    print(m)          # __str__() OVERRIDE kullanır, Çünkü m bir NESNE ve print(m) → m.__str__() çağrılır

for m in musicians:
    print(m.first)    # Bu SATIR __str__ kullanmaz, sadece attribute string olarak yazılır
    m.pretty_print()  # Bu SATIR override DEĞİL, normal bir instance method çağrısı


"""
| Print edilen şey   | Python hangi metodu çağırır? | Neden?                                                      
| ------------------ | ---------------------------- | ---------------------------------------
| `print(musicians)` | `__repr__`                   | Çünkü musicians = **list**, 
                                                      liste elemanlarını repr ile yazar             
| `print(m)`         | `__str__`                    | Çünkü m = **tek bir nesne**, nesneyi 
                                                     yazdırırke str override devreye girer 
"""

#-----------------------------

"""
| Durum                   | `print(m)` ne yapar?                 | Override var mı?      
| ----------------------- | ------------------------------------ | ---------------------
| `__str__` TANIMLANMIŞ   | senin metodun çalışır                |  EVET override       
| `__str__` TANIMLANMAMIŞ | Python’ın default `__repr__` çalışır |  HAYIR override değil 
"""


with open(output_path, "w") as f_out:
    for m in musicians:
        f_out.write(str(m) + "\n")


with open(output_path, "r") as f:
    for line in f:
        print(line.strip())





















