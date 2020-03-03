file = open("userinfo.txt" , "r" , encoding= "UTF-8")
lines = list()
for i in file:
  lines.append(i)

eMail = lines[0]
passWord = lines [1]

file.close()