def myfuntion():
    print("Hello World")
myfuntion()


def myadder(a, b):
    return (a + b)
myresult = myadder(1, 2)
print(myresult)


a = 2
b = 3

if a % 2 == 0 or b % 2 == 0:
    print("both are even")
else:
    print("at least one is odd")

#---------------------------------------------

a = 6
b = 7
def my_print_function(x,y):
    if a % 2 == 0 and b % 2 == 0:
        print("both are even")
    else:
        print("at least one is odd")

my_print_function(a,b)


def my_adder(a, b):
    """
    function to distinguish the even and odd numbers
    :param a:
    :param b:
    :return:
    """
    if a%2 == 0 and b%2 == 0:
        return (a + b)
    else:
        return(a)

my_adder(6,7)
print(my_adder(6,7))

my_adder.__doc__

#---------------------------------------------

mystring = "Hello World"
print(mystring[-1:])
print(mystring[:-4])
print(mystring[2:-1])

my_nouns = ['Dog', 'Cat', 'Elephant']
for elem in my_nouns:
    my_string = "Hello, I'm a  animal of type " + elem
    print(my_string)


my_nouns = ['Dog', 'Cat', 'Elephant']
for elem in my_nouns:
    print( f"hello I am {elem}")


my_nouns = ['Dog', 'Cat', 'Elephant']
for elem in my_nouns:
    print( "hello I am {} animal".format(elem))


dog_var = "dog"
cat_var = "cat"

print("Hello I'm a {} animal {}".format(dog_var, cat_var))

print("Hello I'm a {A}-{B} animal.".format(A='dog', B='cat'))


mydict = {"A": 'dog', "B": 'cat'}
print("Hello I'm a {A}-{B} animal.".format(**mydict))


mydict = {"A": "dog", "B": "cat"}
print("Hello I'm a {0[A]}-{0[B]} animal.".format(mydict))



#---------------------------------------just interpret in exam:

region = "world"
numbers = [123, 2399, 1, 40003]

for elem in numbers:
    print(f"Hello {elem:>5} {region}")

# {elem:>5} → elem’i 5 karakter genişliğinde sağa hizalar.
# print(f"Hello {elem:<5} {region}")  # sola hizala
# print(f"Hello {elem:^5} {region}")  # ortala

region = "world"
numbers = [123, 2399, 1, 40003]

for elem in numbers:
    print(f"Hello {elem=}")

# | Sembol      | Anlamı                            | Örnek çıktı |
# | ----------- | --------------------------------- | ----------- |
# | {elem}      | sadece değeri gösterir            | 123         |
# | {elem=}     | adı + değeri gösterir             | elem=123    |
# | {elem:>5}   | 5 karakterlik alanda sağa hizalar |    123      |




#---------------------------------------open a file:
# Dosya açma (manuel kapatma yöntemi)
file_object = open("data.txt", "r")   # 'r' = read mode (dosyayı okumak için açar)
content = file_object.read()          # dosyanın içeriğini okur
print(content)                        # ekrana yazdırır
file_object.close()                   # dosyayı kapatır (manuel olarak sen kapatırsın)

# -----------------------------------------------------
#  "with" yapısı ile otomatik kapatma (önerilen yöntem)
with open("data.txt", "r") as f:      # dosya açılır ve f değişkenine atanır
    content = f.read()                # dosya içeriği okunur
    print(content)                    # ekrana yazdırılır
# 'with' bloğu bittiğinde dosya otomatik olarak kapanır (close() gerekmez)

# -----------------------------------------------------
# Farklı dosya açma modları:
# 'r'  → read (okuma)
# 'w'  → write (yazma, dosya varsa sıfırlar)
# 'x'  → create (yeni dosya oluşturur, varsa hata verir)
# 'a'  → append (var olan dosyanın sonuna ekler)
# 'b'  → binary mode (ikili dosyalar için, örn. resimler)
# 't'  → text mode (varsayılan, metin dosyaları için)
# '+'  → hem okuma hem yazma izni verir

# -----------------------------------------------------
# Dosyaya yazma
with open("output.txt", "w") as f:    # 'w' = write mode (dosyayı yazar, varsa sıfırlar)
    f.write("Merhaba Seda!\n")        # dosyaya metin ekler
    f.write("Bu satır Python tarafından yazıldı.\n")

# -----------------------------------------------------
# Dosyaya ekleme (append)
with open("output.txt", "a") as f:    # 'a' = append mode (dosyanın sonuna ekler)
    f.write("Yeni satır eklendi!\n")

# -----------------------------------------------------
# Binary dosya okuma (örneğin bir resim)
with open("photo.jpg", "rb") as img:  # 'rb' = read binary mode
    data = img.read()                 # dosyayı byte olarak okur
    print(len(data))                  # kaç byte okunduğunu yazdırır

# ----------------------------------------
# Belirli miktarda veri okuma
# ----------------------------------------
with open("data.txt", "r") as f:      # 'r' = read mode (okuma)
    content = f.read(10)              # ilk 10 karakteri okur
    print(content)                    # örn: "Hello Seda"

# Eğer size (10) belirtilmezse, yani:
# f.read() yazarsan → tüm dosyayı okur.

# ----------------------------------------
# Satır satır okuma (loop ile)
# ----------------------------------------
# a) while döngüsüyle:
with open("data.txt", "r") as f:
    line = f.readline()               # ilk satırı okur
    while line:                       # satır boş değilse (EOF değil)
        print(line.strip())           # satırı ekrana yaz (boşlukları sil)
        line = f.readline()           # bir sonraki satırı oku

# b) for döngüsüyle (daha pratik yöntem):
with open("data.txt", "r") as f:
    for line in f:                    # dosyadaki her satır için
        print(line.strip())           # satırı yazdır

# c) Tüm satırları liste olarak almak:
with open("data.txt", "r") as f:
    lines = f.readlines()             # tüm satırları liste olarak döner
    print(lines)                      # örn: ['Hello\n', 'How are you?\n']

# ----------------------------------------
# Dosyanın tamamını bir kerede okuma
# ----------------------------------------
with open("data.txt", "r") as f:
    content = f.read()                # tüm dosya içeriğini okur
    print(content)

# f.read(size): Belirtilen kadar karakter okur
# f.read()    : Tüm dosyayı okur
# Eğer dosya sonuna (EOF) ulaşırsa, '' (boş string) döner.



# ----------------  Dosyaya yazma (write) -------------------------

# 'w' → write mode: dosyayı yazar, varsa eski içeriği siler.
file_object = open("example.txt", "w")    # dosyayı aç
file_object.write("hello world")          # buffer'a veri yazar
file_object.flush()                       # veriyi hemen diske gönder (flush)
file_object.close()                       # dosyayı kapatır, buffer'ı da otomatik temizler


#------------ "with" yapısı ile güvenli yazma

# 'with' kullanırsan, close() ve flush() otomatik yapılır.
with open("example.txt", "w") as f:       # dosya açılır
    f.write("hello world")                # dosyaya yazar
# 'with' bloğu bitince Python otomatik olarak flush + close yapar ✅


# ----------  Aynı dosyaya ekleme (append)

with open("example.txt", "a") as f:       # 'a' = append mode
    f.write("\nThis line was added later!")  # sonuna yeni satır ekler

# Ex:
with open("mytextfile.txt", "r") as file_obj:
    content = file_obj.read()
    print(content)


#### SW06 ####

words = ["hello", "world", "python", "Seda"]

def strcut(words, n):
    for w in words:
        print(w[:n])

strcut( words, 3)

#----------------------strcut *arg ile sınırsız string alıyor

def strcut(*args, n):
    for word in args:
        print(word[:n])

strcut("hello", "world", "python", "music", "rock", "love", "metallica", n=3)

#----------------------strcut *arg ile sınırsız string alıyor

def strcut(*args, n):
    result = []
    for word in args:
        cut = word[:n]
        print(cut)             # ekrana da yaz
        result.append(cut)     # listeye de ekle
    return result,

strcut("hello", "world", "python", "music", "rock", "love", "metallica", n=3)

