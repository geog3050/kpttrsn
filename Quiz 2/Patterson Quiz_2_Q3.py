Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList = [2,8,64,16,32,4,16,8]
myList= myList.sort()
for i in range (1, len(myList)-1):
    if myList[i]==myList[i-1]:
        print("The list contains duplicates")
    else:
        print("The list does not contain duplicates")
    
