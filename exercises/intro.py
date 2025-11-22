#cd ~/PycharmProjects/proje1
#python3 -m venv venv
#source venv/bin/activate
#pip install --upgrade pip
#pip install numpy pandas matplotlib jupyterlab
#pip freeze > requirements.txt
#pip install -r requirements.txt
#deactivate



print("hello", "seda", sep=',')

print("today", "is a good day")

a= 3+2
print(a)

#bool(False)   # False
#bool(1)       # True
#bool(0)       # False
#bool("abc")   # True (çünkü boş değil)
#bool("")      # False (çünkü boş string)

x = 8

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# 1️⃣ Şifre doğrulama (while döngüsü)
password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorrect. Please try again.")

print("-" * 40)  # ayırıcı

# 2️⃣ Break ile döngüden çıkış
x = 1
while x <= 10:
    if x == 5:
        break   # döngüyü tamamen bitir
    print(x)
    x += 1

print("-" * 40)  # ayırıcı

# 3️⃣ Continue ile döngüden atlama
for number in range(1, 21):
    if number % 2 == 0:   # çift sayılar
        continue
    if number % 3 == 0:   # 3'ün katları
        continue
    print(number)


for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)

for i in range(1, 4):
    for j in range(1, 4):
        print("{} x {} = {}".format(i, j, i*j))

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")


def get_factors(x):
    """Returns a list of factors of given number x."""

    factors = []  # boş liste oluştur

    # 1'den x'e kadar (x dahil) sayıları sırayla dene
    for i in range(1, x + 1):
        # eğer x, i'ye tam bölünüyorsa (mod 0 ise)
        if x % i == 0:
            factors.append(i)  # i’yi listeye ekle

    return factors  # sonuç listesini döndür


print(get_factors(21))


def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    if x <= 1:
        return False

    for i in range(2, x):  # yani x-1 e kadar git
        if x % i == 0:
            return False

    return True


def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """

    if x <= 1:
        return False

    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)

    if len(factors) > 2:
        return True
    else:
        return False


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    if x == 1:
        return False

    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)

    if sum(factors) == x:
        return True
    else:
        return False


def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """

    if x == 1:
        return False

    factors = []
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)

    if sum(factors) > x:
        return True
    else:
        return False





def isTriangular(x):
    """Returns whether or not a given number x is triangular.

    The triangular number Tn is a number that can be represented in the form of a triangular
    grid of points where the first row contains a single element and each subsequent row contains
    one more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """

    if x == 1:
        return True

    for i in range(2, x + 1):
        if (i * (i + 1) / 2) == x:
            return True

    return False


def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    if x < 10:
        return True

    else:
        digits = str(x)
        n = len(digits)
        toplam = sum(int(i) ** n for i in digits)

    return toplam == x


def max_and_min(liste):
    return (max(liste), min(liste))


def main():
    values = [0,1,2,3]
    maxmin = max_and_min(values)

    print(maxmin)
    max = maxmin[0]
    print(max)
    min = maxmin[1]
    print(min)

if __name__ == "__main__":
    main()


def concatenate(strings):
    """
    Concatenates the given list of strings into a single string.
    Returns the single string.
    If the given list is empty, returns an empty string.

    For example:
    - If we call concatenate(["a","b","c"]), we'll get "abc" in return
    - If we call concatenate([]), we'll get "" in return

    Hint(s):
    - Remember, you can create a single string from a list of multiple strings by using the join() function
    """
    if len(strings) == 0:
        return ""

    else:
        return "".join(strings)


def remove_duplicates(lst):
    """
    Returns the given list without duplicates.
    The order of the returned list doesn't matter.

    For example:
    - If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
    - If we call remove_duplicates([]), we'll get [] in return

    Hint(s):
    - Remember, you can create a set from a string, which will remove the duplicate elements
    """

    if len(lst) == 0:
        return []

    else:
        uniqlist = list(set(lst))
        return uniqlist


def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particualr character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """

    if sentence.startswith("*"):
        sentence = sentence[1:].strip() #boşlukları temizle
        words = sentence.split() #böl
        new_words = []

        for w in words:
            if len(w) == 1:
                new_words.append(w.upper())

            else:
                new_word = w[0].upper() + w[1:-1] + w[-1].upper()
                new_words.append(new_word)

        return " ".join(new_words)

    else:

        return ",".join(sentence.split())


def move_zero(lst):
    """
    Given a list of integers, moves all non-zero numbers to the beginning of the list and
    moves all zeros to the end of the list.  This function returns nothing and changes the given list itself.

    For example:
    - After calling move_zero([0,1,0,2,0,3,0,4]), the given list should be [1,2,3,4,0,0,0,0] and the function returns nothing
    - After calling move_zero([0,1,2,0,1]), the given list should be [1,2,1,0,0] and the function returns nothing
    - After calling move_zero([1,2,3,4,5,6,7,8]), the given list should be [1,2,3,4,5,6,7,8] and the function returns nothing
    - After calling move_zero([]), the given list should be [] and the function returns nothing
    """

    non_zeros = [x for x in lst if x != 0]
    zero_count = len(lst) - len(non_zeros)
    zeros = [0] * zero_count
    new_lst = non_zeros + zeros

    for i in range(len(lst)):
        lst[i] = new_lst[i]


def load_expenses(filename):  # Dosyadan harcamaları okuyup sözlüğe dönüştüren fonksiyon
    expenses = {}  # Boş bir sözlük başlatıyoruz {isim: toplam_harcama}

    with open(filename, "r") as f:  # Dosyayı okuma modunda aç, iş bitince otomatik kapat
        for line in f:  # Dosyadaki her satır için döngü başlat
            parts = line.strip().split(",")  # Satırdaki boşlukları sil, virgül ile parçala → ["Brandon", "3.42"]

            if len(parts) != 2:  # Eğer satırda iki parça yoksa (örneğin eksik bilgi varsa)
                continue  # Bu satırı atla

            name, amount_str = parts[0].strip(), parts[1].strip()
            # parts[0] → isim, parts[1] → miktar (string olarak)

            try:
                amount = float(amount_str)  # Miktarı sayıya (float) çevir
            except ValueError:  # Eğer sayı değilse (ör. "twenty-two")
                continue  # Bu satırı da atla

            if name in expenses:  # Eğer kişi zaten sözlükte varsa
                expenses[name] += amount  # Üzerine ekle (toplam harcamayı artır)
            else:
                expenses[name] = amount  # Yoksa yeni giriş oluştur

    return expenses  # Sözlüğü döndür

# dosya açma modları:
#####################

# "r"   : read (okuma) → dosya var olmalı, yoksa hata verir.
# "w"   : write (yazma) → dosya varsa içeriğini siler, yoksa yeni dosya oluşturur.
# "a"   : append (ekleme) → dosya varsa sonuna ekleme yapar, yoksa oluşturur.
# "x"   : create (oluşturma) → dosya yoksa oluşturur, varsa hata verir.
# "r+"  : read + write → okuma ve yazma yapılabilir, dosya var olmalı.
# "w+"  : write + read → dosya içeriğini siler, hem okuma hem yazma yapılabilir.
# "a+"  : append + read → sona ekleme ve okuma yapılabilir, dosya yoksa oluşturur.


# Merhaba
# Dünya
# Python

f = open("test.txt", "r")
print(f.read())       # "Merhaba\nDünya\nPython\n"

f = open("test.txt", "r")
print(f.readline())   # "Merhaba\n"
print(f.readline())   # "Dünya\n"

f = open("test.txt", "r")
print(f.readlines())  # ["Merhaba\n", "Dünya\n", "Python\n"]


