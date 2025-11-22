
################# Banka hesabı ödev coursera ############

with open("bank.txt", "w") as f:
    f.write("Brandon, 5\n")
    f.write("Patrick, 18.9\n")
    f.write("Brandon, xyz\n")
    f.write("Jack, \n")
    f.write("Sarah, 825\n")
    f.write("Jack, 45\n")
    f.write("Brandon, 10\n")
    f.write("James, 3.25\n")
    f.write("James, 125.62\n")
    f.write("Sarah, 2.43\n")
    f.write(" \n")
    f.write("Brandon, 100.5\n")
    f.write("Betsy, 864.31\n")
    f.write("\n")
    f.write("\n")
    f.write("Betsy, 864.31\n")


with open("user.txt", "w") as f:
    f.write("Brandon - brandon123ABC\n")
    f.write("Jack\n")
    f.write("Jack - jac123\n")
    f.write("Jack - jack123POU\n")
    f.write("Patrick - patrick5678\n")
    f.write("Brandon - brandon123ABCD\n")
    f.write("James - 100jamesABD\n")
    f.write("Sarah - sd896ssfJJH\n")
    f.write("Jennie - sadsaca\n")


def import_and_create_accounts(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file should be in the following format:
        key: value
    The key is a user's name and the value is an amount to update the user's bank account with.  The value should be a
    number, however, it is possible that there is no value or that the value is an invalid number.

    What you will do:
    - Create an empty bank dictionary.
    - Read in the file.
    - Add keys and values to the dictionary from the contents of the file.
    - If the key doesn't exist in the dictionary, create a new key:value pair.
    - If the key does exist in the dictionary, increment its value with the amount.
    - You should also handle the following cases:
    -- When the value is missing or invalid.  If so, ignore that line and don't update the dictionary.
    -- When the line is completely blank.  Again, ignore that line and don't update the dictionary.
    -- When there is whitespace at the beginning or end of a line and/or between the name and value on a line.  You
    should trim any and all whitespace.
    - Return the bank dictionary from this function.

    For example, here's how your code should handle some specific lines in the file:
    The 1st line in the file has a name and valid number:
        Brandon: 5
    Your code will process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5}

    The 2nd line in the file also has a name and valid number:
        Patrick: 18.9
    Your code will also process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 3rd line in the file has a name but invalid number:
        Brandon: xyz
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 4th line in the file has a name but missing number:
        Jack:
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 5th line in the file is completely blank.
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 8th line in the file has a name and valid number, but with extra whitespace:
        Brandon:       10
    Your code will process this line and update the value associated with the existing key ('Brandon') in the dictionary.
    After it does, the value associated with the key 'Brandon' will be 10:
        bank = {"Brandon": 15, ...}

    After processing every line in the file, the dictionary will look like this:
        bank = {"Brandon": 115.5, "Patrick": 18.9, "Sarah": 827.43, "Jack": 45.0, "James": 128.87}
    Return the dictionary from this function.
    '''

    bank = {}

    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")

            if len(parts) != 2:
                continue

            name, amount = parts[0].strip(), parts[1].strip()

            try:
                amount = float(amount)

            except ValueError:
                continue

            if name in bank:
                bank[name] += amount

            else:
                bank[name] = amount

    return bank


def signup(user_accounts, log_in, username, password):
    if username in user_accounts:
        return False

    if not valid(password, username):
        return False

    user_accounts[username] = password
    log_in[username] = False
    return True


def valid(password, username):
    if len(password) < 8:
        return False
    if password == username:
        return False
    if not any(ch.islower() for ch in password):
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    return True


def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.

    For example:
    - Calling login(user_accounts, "Brandon", "123abcAB") will return False
    - Calling login(user_accounts, "Brandon", "brandon123ABC") will return True
    '''

    if username not in user_accounts:
        return False

    if user_accounts[username] != password:
        return False

    log_in[username] = True
    return True


def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.

    For example, if Brandon has 115.50 in his account:
    - Calling update(bank, log_in, "Brandon", 50) will return False, unless "Brandon" is first logged in.  Then it
    will return True.  Brandon will then have 165.50 in his account.
    - Calling update(bank, log_in, "Brandon", -200) will return False because Brandon does not have enough in his
    account.
    '''

    if username not in log_in or not log_in[username]:
        return False

    if username not in bank:
        bank[username] = 0.0

    if bank[username] < 0:
        return False

    bank[username] += amount
    return True


def transfer(bank, log_in, userA, userB, amount):
    if amount <= 0:
        return False

    # userA bank ve log_in'de olmalı, login durumu True olmalı
    if userA not in bank or userA not in log_in or not log_in[userA]:
        return False

    # userB log_in'de olmalı
    if userB not in log_in:
        return False

    # userA'nın bakiyesi yeterli olmalı
    if bank[userA] < amount:
        return False

    # userB bank'ta yoksa sıfır bakiye ile ekle
    if userB not in bank:
        bank[userB] = 0.0

    # transfer işlemi
    bank[userA] -= amount
    bank[userB] += amount
    return True


def delete_account(user_accounts, log_in, bank, username, password):
    '''
    Completely deletes the user from the online banking system.
    If the user exists in the user_accounts dictionary and the password is correct, and the user
    is logged in (the username is associated with the value True in the log_in dictionary):
    - Deletes the user from the user_accounts dictionary, the log_in dictionary, and the bank dictionary.
    - Returns True.
    Otherwise:
    - Returns False.

    For example:
    - Calling delete_account(user_accounts, log_in, bank, "BrandonK", "123abcABC") will return False
    - Calling delete_account(user_accounts, log_in, bank, "Brandon", "123abcABDC") will return False
    - If you first log "Brandon" in, calling delete_account(user_accounts, log_in, bank, "Brandon", "brandon123ABC")
    will return True
    '''

    if username not in user_accounts:
        return False

    if user_accounts[username] != password:
        return False

    if username not in log_in or not log_in[username]:
        return False

    user_accounts.pop(username)
    log_in.pop(username)
    bank.pop(username)

    return True


def change_password(user_accounts, log_in, username, old_password, new_password):
    # Kullanıcı var mı?
    if username not in user_accounts:
        return False

    # Kullanıcı giriş yapmış mı?
    if username not in log_in or not log_in[username]:
        return False

    # Eski şifre doğru mu?
    if user_accounts[username] != old_password:
        return False

    # Yeni şifre eskisiyle aynı mı?
    if new_password == old_password:
        return False

    # Yeni şifre kurallara uygun mu?
    if not valid(new_password, username):
        return False

    # Şifreyi değiştir
    user_accounts[username] = new_password
    return True

def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_accounts("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")


if __name__ == '__main__':
    main()
