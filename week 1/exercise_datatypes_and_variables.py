###############
# Exercise 1
###############

"""
What does Python return as result of the following calculations?
"""
a = 10 + 10 +10
print(type(a))

10 - 3    
10 * 2

b = 5.0/ 2
print(type(b))

5.0 / 2
5 % 2

c = 10 % 3
print(c)

d = 9 ** .5 # karekök aldı
print(d)


e = 10 + 3 * 3
print(e)

f = (10 + 3) * 3
print(f)


"""
Try to find out: What happens?
"""
a=23
b=23
print(a)
print(id(a))                          # https://docs.python.org/3/library/functions.html#id 
                                      # Return the “identity” of an object. This is an integer 
                                      # which is guaranteed to be unique and constant for this 
                                      # object during its lifetime. Two objects with non-overlapping 
                                      # lifetimes may have the same id() value

# id() fonksiyonu:
# Bir nesnenin "identity" (kimlik) değerini döndürür.
# Bu değer nesnenin ömrü boyunca sabit kalan bir tamsayıdır.
# Aynı nesneyi gösteren değişkenler aynı id() değerini taşır.
# Farklı nesnelerin id() değerleri farklı olur.
# Ancak, yaşam süreleri çakışmayan nesneler
# (ör. biri silinip sonra yeni biri oluşturulursa)
# aynı id() değerini alabilir.



                
print(type(a))                        # https://docs.python.org/3/library/functions.html#type
                                      # With one argument, return the type of an object. 
                                      # The return value is a type object and generally the same object 
                                      # as returned by object.__class__.

# type() fonksiyonu:
# Tek argümanla çağrıldığında bir nesnenin tipini (class türünü) döndürür.
# Dönen değer bir "type object"tir.
# Genellikle object.__class__ ifadesinin döndürdüğüyle aynıdır.

print(b)
print(id(b))
print(type(b))


"""
change the value of variable 'a'
"""
a=123
print(a)
print(id(a))
print(type(a))
print(b)
print(id(b))
print(type(b))


"""
what happens now? why? 
"""
c = 23
print(c)
print(id(c))
print(type(c))


"""
try the same thing with a float variable!!!
"""
f = 3.14159
pi = 3.14159

f = 2.71828

"""
try the same thing with a float variable!!!
"""

f = 3.14159
pi = 3.14159

print(id(f))   # f'nin kimliği (adres gibi)
print(id(pi))  # pi'nin kimliği (adres gibi)

f = 2.71828

print(id(f))   # f artık başka bir float nesnesini (2.71828) gösteriyor
print(id(pi))  # pi hâlâ 3.14159'u gösteriyor

# id() → nesnenin bellekteki adresini (veya kimliğini) verir.
# Eğer id() değişirse, bu demektir ki değişken artık farklı bir nesneyi gösteriyor →
# yani bellekte farklı bir adreste duran kutuya bağlanmış oldu.

# Özet:
# Aynı nesne → aynı id (adres değişmez).
# Yeni nesne  → yeni id (adres değişir).




"""
... and so on - do it (programming ;-) !!)  yourself 


Hint: remember, in Python all variables are always objects references!
"""


"""
printing of text (strings)
"""
print ("HSLU's Python course is cool")

print("This is Line 1")
print("This is Line 2")
print("\nWhat does the \\n control character do? Are you sure?")

print("\tWhat does the \\t control character do? Are you sure?")

print("I want to learn python because....")
print("\n\n\t....it's a cool data science programming language. Ok - there are also others ;-) !")

print("What" + "is" +"wrong?" + "\nAdd some space between the words without removing the '+' signs!")

print("what" + "+" + "\t" + "is" + "+" + "\t" + "wrong")
print("what" + "+" + "\n" + "is" + "+" + "\n" + "wrong")
print("what" + "\n\n" "+" + "\n\n""is" + "\n\n""+" "\n\n" + "wrong")
print("what" + "+" + "\\" + "is" + "+" + "\\n" + "wrong")



# \n  → new line (yeni satır). Yazıyı bir alt satıra geçirir.
# \t  → tab (sekme). Araya boşluk ekler, sanki "TAB" tuşuna basılmış gibi.
# \\  → ters eğik çizgi (\) karakterini yazdırır......DİKKAT !!!! option + * \\
# \'  → tek tırnak (') karakterini string içinde yazdırır.
# \"  → çift tırnak (") karakterini string içinde yazdırır.

"""
try to understand the behaviour
"""
g=h='hslu'
print(g)
print(h)
h=456
print(h) #456
h=h+1
print(h) #457
h+=1
print(h) #458
p='hslu'
q=p
print(p==q)
print(p is q)

# - Variables store references to objects, not the actual value
# - '=' assignment makes a variable point to a new object
# - '==' compares contents
# - 'is' compares object identity (whether they are the same object)

