import hashlib


def func_make_hash():
    mystring = input('Enter String to hash: ')
    hash_object = hashlib.sha1(mystring.encode())
    hex_dig = hash_object.hexdigest()
    print("Your hash is: ", hex_dig)


def simple_hash():
    mystring = input('Enter String to hash: ')
    new_sum = 0
    for el in range(len(mystring)):
        new_sum = new_sum + ord(mystring[el])
        print(ord(mystring[el]))

    return print("Your hash is: ", new_sum)


func_make_hash()
simple_hash()
