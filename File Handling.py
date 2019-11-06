f = open('MyData.txt',"r")
print(f.read())


print('\n ###### Next Program Read only one Line #########')


f = open('MyData.txt',"r")
print(f.readline())


print('\n ###### Next Program Read first to lines #########')


f = open('MyData.txt',"r")
print(f.readline())
print(f.readline())


print('\n ###### Next Program Read first to lines without Lines Spaces #########')


f = open('MyData.txt',"r")
print(f.readline(), end="")
print(f.readline())


print('\n ###### Next Program Read all lines from the file and Print in the same Line #########')


f = open('MyData.txt',"r")
print(f.readlines())


print('\n ###### Next Program Read all lines from the file in One by One #########')


f = open('MyData.txt',"r")
for data in f:
    print(data)



print('\n ###### Next Program to copy a data from a file to a new File #########')


f = open('MyData.txt',"r")
f1 = open('abc.txt', 'w')
for data in f:
    f1.write(data)
f1 = open('abc.txt', 'a')
f1.write('\nMay Native is Marthandam, Kanyakumari District')
f1.write('\nI am Married')

print('\n Note: Please remember that if you want to write something in existing program use append "a"')
print('\n Note: If write something in existing program with write "w" then the existing data will be erases and only the date you write will be there in the file')


print('\n ###### Next Program to write additional data in a existing File #########')


f = open('MyData.txt',"r")
f1 = open('abc.txt', 'a')
f1.write('\nMay Native is Marthandam, Kanyakumari District')
f1.write('\nI am Married')



print('\n ###### Next Program to Print the data of Image file #########')

print('\n Note: Data of Image file will be in Binaryformat so use "rb" to read the image file')

f = open('2X8A0238.JPG',"rb")
for i in f:
    print(i)


print('\n ###### Next Program to Copy Image file into a new Image #########')

print('\n Note: Data of Image file will be in Binaryformat so use "rb" to rad the image file')

f = open('2X8A0238.JPG',"rb")
f1 = open('My_Marriage_Photo.JPG',"wb")
for i in f:
    f1.write(i)



print('\n ###### Next Program to write additional data in a existing File #########')


f = open('MyData.txt',"r")
f1 = open('abc.txt', 'a')
f1.write('\nMay Native is Marthandam, Kanyakumari District')
f1.write('\nI am Married')




print('\n ###### Next Program to copy data from existing file and write additional data in a existing File #########')


f = open('MyData.txt',"r")
f1 = open('abc.txt', 'a')
for data in f:
    f1.write(data)
f1.write('\nMay Native is Marthandam, Kanyakumari District---2')
f1.write('\nI am Married---2')

