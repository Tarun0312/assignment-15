# 7. Write a python script to determine whether a string contains a specific substring.

x,y=input("Enter a string: "),input("Enter substring: ")

p=x.find(y)
print("Substring Not found "if(p==-1) else "Substring found at index starts with {}".format(p))
    