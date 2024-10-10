# simple
a = 33
b = 200

if b > a:
    print(b, "es mayor que ",a)

#doble
y = 200
z = 333
if y > z:
    print(y,"es mayor que",z)
else:
     print(y,"no es mayor que ",z)





#multiplicacion
e = 200
p = 207
if e > p:
    print(e,"es mayor que",p)

elif e < p:
    print(e,"es mayor que",p)

else:
    print(e,"es igual que",p)

x = 28
if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")


#parametros END Y SEP
print("estudiar los sabados ", end='')
print("es genial")


 #parametros END Y SEP
print("daniela", "luis","carlos", "camila") #agrepa un espacio por defecto

print("daniela", "luis", "carlos", "camila",sep="") #quita el espacio
print("daniela", "luis", "carlos", "camila",sep=",")#agrega una coma

print("daniela", "luis", "carlos", "camila", sep="_", end='_Curso_python')#implementacion end y sep

