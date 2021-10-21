"""
#
File    :question1.py
Created :14/10/2021
Author  : Eoin O'Mahony
"""

import os
import sys


if __name__ == '__main__':
    my_os = os.uname()
    my_path =  sys.path
    path_to_pkg = my_path[0]

    print(f"My path to packge is {path_to_pkg}, my OS is {my_os[0]}, my node is {my_os[1]} ")

