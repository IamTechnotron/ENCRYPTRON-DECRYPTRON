''' 
Logic:
>It takes a string input,
>Generates a random number => the key
>Starts adding the key with the ASCII of each charecter
>If after addition, the resultant charecter exceeds Z or z, it cycles backs from A or a. 
'''


from random import randint
print ("                W E L C O M E   T O   E N C R I P T R O N \n\n\n")
key=randint(1,9)
msg=list(input("Enter the message to be encripted:\n"))
p=-1                        # a counter to store the position of the charecter
for l in msg:
    intl=ord(l)             # stores the ASCII of the charecter
    p+=1
    if( (intl>=65 and intl<=90)):
        if(intl+key>90):
            msg[p]=chr(65+((intl+key)-90))
        else :
            msg[p]=chr(intl+key)
    elif ( (intl>=97 and intl<=122) ):
        if(intl+key>122):
            msg[p]=chr(97+((intl+key)-122))
        else:
            msg[p]=chr(intl+key)


msg="".join(msg)
print(msg,"\nKEY=",key)
