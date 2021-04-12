with open("lista de puntos.txt","r") as file:
	content=file.readlines()

content = [x.strip() for x in content] 

for i in range(len(content)):
	content[i]=content[i]+" "

content[0:len(content)]= [''.join(content[0:len(content)])]


string=content[0].split(", ")
string=string[:len(string)-1]
for j in range(len(string)):
	string[j]=int(string[j])

lista=string


j=1
for i in range(len(lista)):
	if i>0:
		if j%20==0:
			j+=1

			print(lista[i])
			print("pasaste 20")
			input()

		else:
			j+=1
			print(lista[i])
			input()
	else:
		j+=1
