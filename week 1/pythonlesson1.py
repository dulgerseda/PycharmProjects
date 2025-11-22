print("hello world")

a = 3
print (a + 3)

#cd ~/PycharmProjects/proje1
#python3 -m venv venv
#source venv/bin/activate
#pip install --upgrade pip
#pip install numpy pandas matplotlib jupyterlab
#pip freeze > requirements.txt
#pip install -r requirements.txt
#deactivate

a = [1,2,3]
print(type(a))

b = 3
print(type(b))

# tuple = immutable

my_dict = {"a:1", "b:2"}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())

d = [1,1,2,2,3]
b = set(d)

x = 3
y = 5

z = x ** y
print(z)

##################  week-2 ################

to_transform = "3"

my_int = to_transform
print(type(my_int))
my_float = to_transform
print(my_float)

val = 3.9
print(type(val))
i = int(val)
print(type(i))

print(bool())
print(bool(""))


my_age = input("hello, how old are you?:")
print(my_age)


objects = ["hello", "world"]
print(*objects, sep=' ', end='\n', file=None, flush=False)



# Python'da bool() fonksiyonu ile değerlerin True/False karşılığını görebiliriz.

print(bool(None))        # None -> False
print(bool(0))           # 0 -> False
print(bool(""))          # Boş string -> False
print(bool([]))          # Boş liste -> False
print(bool({}))          # Boş dict -> False
print(bool(set()))       # Boş set -> False

print(bool(1))           # 0 dışında her sayı -> True
print(bool("Merhaba"))   # Boş olmayan string -> True
print(bool([1, 2, 3]))   # Boş olmayan liste -> True
print(bool({"a": 1}))    # Boş olmayan dict -> True

# Zincirleme karşılaştırma örneği:
print(bool("") == bool(0) == bool(None) == False == (not True))
# Açıklama:
# bool("") -> False
# bool(0) -> False
# bool(None) -> False
# not True -> False
# Hepsi False olduğu için eşitlik True döner.

def f():
    print("f() çalıştı")
    return True

def g():
    print("g() çalıştı")
    return False

# OR (x or y)
# İlk ifade True ise -> ikinciyi çalıştırmaz (lazy evaluation)
print(True or f())   # f() çalışmaz
print(False or f())  # f() çalışır

# AND (x and y)
# İlk ifade False ise -> ikinciyi çalıştırmaz (lazy evaluation)
print(False and g())  # g() çalışmaz
print(True and g())   # g() çalışır

# Örnek: sıfıra bölme hatasını önlemek
x = 0
# Burada "x != 0" False olduğu için ikinci kısım çalışmaz.
# Böylece ZeroDivisionError oluşmaz (lazy evaluation sayesinde).
print(x != 0 and (10 / x > 1))  # False


True and False
True or False
(True and False) or True

a = 3
b = 4
a == b
a != b
a < b

a = 6      # 110 (ikilik)
b = 3      # 011 (ikilik)

print(a & b)   # 2  -> 010 (bitwise AND)
print(a | b)   # 7  -> 111 (bitwise OR)
print(a ^ b)   # 5  -> 101 (bitwise XOR)
print(~a)      # -7 -> tüm bitler ters
print(True and False)  # False
print(True & False)    # False (ama bitwise olarak 1 & 0 → 0)

print(6 and 3)   # 3  (çünkü 6 True, sonra 3 döner)
print(6 & 3)     # 2  (bitwise: 110 & 011 = 010)

# Mantıksal operatörler: and, or, not
# Bitwise operatörler: &, |, ^, ~, <<, >>

# 4 = 100 representation on binary

a = 4   # 0100 (ikilik gösterim)
b = 9   # 1001
c = 11  # 1011

# 1) a & b
#  0100 (a = 4)
#& 1001 (b = 9)
#  ----
#  0000 = 0
result = a & b
print(result)  # 0

# 2) c & b
#  1011 (c = 11)
#& 1001 (b = 9)
#  ----
#  1001 = 9
result = c & b
print(result)  # 9

lst=[]

for i in range(12, 21):   # 12'den 20'ye kadar (21 dahil değil)
    if i % 2 == 0:        # 2'ye bölünebilenler
        lst.append(i)     # listeye ekle

print(lst)


lst = []

# for i in range(12, 20):
# ####if i % 2 == 0:          # 4
# ########lst += [i]          # 8

print(lst)  # [12, 14, 16, 18]

x = 3

if x > 2:
    print(x)
    if x > 8:
        print(x)

print("I'm done!")


age = 15
if age > 18:
    print("you are allowed to drink!")
else:
    print("sorry! you are too young")

print("tschüs!")


x = 5

if x > 10:                         # Eğer x, 10'dan büyükse
    print("ok")                    # ekrana "ok" yazdır
else:                              # değilse
    print("setting new value")     # bilgi mesajı yazdır
    x = x + 10                     # x değerini 10 artır


x = 9

if x > 100:
    print("oh that's a big number")
elif x > 10:
    print("oh still a relatively big number")
elif x > 8:
    print("oh still a relatively big number, but not that much")
else:
    print("oh no its below 10")
print("tschüs!")


x = 9
y = x if x*2 < 5 else x+1
print(y)


x = 9

if x*2 < 5:
    y = x
else:
    y = x + 1

print(y)

x = 2

if x == 0:
    print("number is 0")
elif x == 1:
    print("number is 1")
elif x == 2:
    print("number is 2")
else:
    print("number unknown")



# Python 3.10+ match-case ile
x = 2
match x:
    case 0:
        print("number is 0")
    case 1:
        print("number is 1")
    case 2:
        print("number is 2")
    case _:
        print("number unknown")   # default case




point = (1, 2)   # Bir nokta tanımlandı (x=1, y=2)

match point:     # 'point' tuple'ı incelenecek
    case (0, 0):   # Eğer nokta (0,0) ise
        print("Origin")  # Orijinde olduğunu yaz
    case (x, 0):   # Eğer nokta (x,0) şeklindeyse (yani x ekseni üzerinde)
        print(f"On the X-axis at x = {x}")
    case (0, y):  # Eğer nokta (x,0) şeklindeyse (yani x ekseni üzerinde)
        print(f"On the y-axis at y = {y}")
    case _:
        print("not on axis")


























