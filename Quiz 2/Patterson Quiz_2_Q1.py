Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mystr = input('enter a string:')
for i in range(0,len(mystr)-1):
    if mystr[i]=="z":
        print("Yes")
    else:
        print("No")
