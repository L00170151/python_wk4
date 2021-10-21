"""
#
File    :question2.py
Created :21/10/2021
Author  : Eoin O'Mahony
"""

import crypt
import timeit


def test():
    password = "abcdefghijglmnop"
    encrypted_password = crypt.crypt(password)
    print("Pre encryption: " + password)
    print("Post encryption: " + encrypted_password)

def timing():
    print("Time taken to encrypt: "+ str(timeit.timeit(stmt=test, number=1)))
    return


timing()






