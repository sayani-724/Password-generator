from random import  *
import string

n=int(input("Enter password length: "))

a=string.ascii_uppercase
b=string.ascii_lowercase
c=string.punctuation
d=string.digits

chrs=a+b+c+d

pwd="".join(sample(chrs, n))

print(f"Random password of {n} characters: {pwd}")
    