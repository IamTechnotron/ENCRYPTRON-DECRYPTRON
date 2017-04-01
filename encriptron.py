'''
Logic:
> takes the directories to read and write file
> It breaks the file in a list of the lines, which is again broken into a list of the characters
> Then iterates through each character and changes whenever needed!
> Changes made:
    1. ASCII of letters are added by key and proceed accordingly (like before)
    2. spaces are replaced by | in the encrypted file
    3. commas are replaced by ~
'''

from random import randint
import os

print("\t\t\tW E L C O M E   T O   E N C R I P T R O N_v1.0\n\n\n")
key = randint(1, 9)
rfile_directory = input("Enter the file name with the directory to be encrypted:\n")
assert os.path.exists(rfile_directory), "File Not Found at specified location !!!"
wfile_directory = input("Enter the file name with the directory where encrypted file will be stored:\n")
wfile = open(wfile_directory, 'w')
with open(rfile_directory, 'r') as rfile:
    for l in rfile:
        p = -1                                                        # a counter to store the position of the character in the line
        line = list(l)
        for char in line:
            char_ascii = ord(char)                                    # stores the ASCII of the character
            p += 1
            if 60 <= char_ascii <= 90:                                # for changing A to Z
                if char_ascii + key > 90:
                    line[p] = chr(65 + ((char_ascii + key) - 90))
                else:
                    line[p] = chr(char_ascii + key)
            elif 97 <= char_ascii <= 122:                             # for changing a to z
                if char_ascii + key > 122:
                    line[p] = chr(97 + ((char_ascii + key) - 122))
                else:
                    line[p] = chr(char_ascii + key)
            elif char_ascii == 32:                                    # for changing 'space'
                line[p] = chr(124)
            elif char_ascii == 44:                                    # for changing ','
                line[p] = chr(126)
        wfile.write("".join(line))


wfile.write(str(key))
rfile.close()
wfile.close()
