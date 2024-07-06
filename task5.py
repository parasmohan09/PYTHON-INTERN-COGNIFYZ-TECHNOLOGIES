#PROGRAMM TO FILE MANUPLATION IN THE PYTHON..

#FISRT WE CAN OPEN THE TEXT FILE IN THE PYTHON..

f=open("file.txt","w")#in this we can open the file but firstly we can open file in the writting mode.beacuse first we can write something in the file.

f.write("HI IAM PARAS MOHAN AND NOW I AM DOING  MY 5TH TASK WHICH IS PROVIDED BY COGNIFYZ TECHNOLOGIES..")# in this write method can be used to write something inside in the file in the python

# now we can open file and then we can read the file in the python
f=open("file.txt","r")#in this we can open the file but read method can be used beacuse with the help of read methods in the python we can read the file.
m=f.read()# in this 'm' variable stores the f.read() which means read method can be used to read the file in the python.
print(m)# it is used to print file text in alphabetical on console.

print(len(m))#this is used to print the lentgh of text write in the file.

f.close()# this can be used to close the file in the python.so, we can use it we can always the f.close() method can be used close the file.