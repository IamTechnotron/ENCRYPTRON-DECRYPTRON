from random import randint
import os
import codecs

#C:\Users\Avik Mukherjee\Desktop\EDtron\en_file.txt

print("\t\t\tW E L C O M E   T O   E N C R I P T R O N_v1.0\n\n\n")
rfile_directory = input("Enter the file name with the directory to be decrypted:\n")
assert os.path.exists(rfile_directory), "File Not Found at specified location !!!"
wfile_directory = input("Enter the file name with the directory where encrypted file will be stored:\n")
wfile = open(wfile_directory, 'w')

file = open(rfile_directory)
s = "".join(list(file))
key = int(s[-1:])
file.close()

with open(rfile_directory, 'r') as rfile:
    for line in rfile:
        p = -1                                                        # a counter to store the position of the character in the line
        line = list(line)
        for char in line:
            char_ascii = ord(char)                                    # stores the ASCII of the character
            p += 1
            if 65 <= char_ascii <= 90:                                # for changing A to Z
                if char_ascii - key < 65:
                    line[p] = chr(90 + 1 - (65 - (char_ascii - key)))
                else:
                    line[p] = chr(char_ascii - key)
            elif 97 <= char_ascii <= 122:                             # for changing a to z
                if char_ascii - key < 97:
                    line[p] = chr(122 + 1 - (97 - (char_ascii - key)))
                else:
                    line[p] = chr(char_ascii - key)
            elif char_ascii == 124:                                    # for changing '|'
                line[p] = chr(32)
            elif char_ascii == 126:                                    # for changing '~'
                line[p] = chr(44)
        wfile.write("".join(line))
wfile.close()
size = os.path.getsize(wfile_directory)
with open(wfile_directory,"ab+") as file:
    file.truncate(size-1)

