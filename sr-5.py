print('Введите число 2 для перевода в двоичную систему счисления')
print('Введите число 8 для перевода в восьмеричную систему счисления')
k=int(input()) # 2 или 8
print('Введите число для перевода в', k, "систему счисления")
n=int(input())
n1=''
if k==2:
    while n>0:
        n1=str(n%2)+n1
        n=n//2
else:
    while n>0:
        n1=str(n%8)+n1
        n=n//8
print(n1)
