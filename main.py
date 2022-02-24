from sys import * 
import os
from pathlib import *

    
Path_s = input("Enter path:")
file_name = input("Enter name of the file (don't forget to enter the extention):")

acces_file = os.path.join(Path_s, file_name)

file1 = open(acces_file, "w")
file1.write("Hello world")
file1.close()
