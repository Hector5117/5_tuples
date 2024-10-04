
#Tuples las lists se pueden modificar y comentar  pero las tuples son constantes y solo
#se le pueden agregar datos hasta q la conviertes  en lista
#Definicion


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Hector", "Sanchez", "Hector")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))


#Acceso a elementos y busqueda

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) #IndexError
#print(my_tuple[-6]) #IndexError

print(my_tuple.count("Hector"))
print(my_tuple.index("Sanchez"))
print(my_tuple.index("Hector"))

my_tuple[1] = 1.80 #'tuple' object does not support item assignment

#Concatenacion

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)



#subtuplas

print(my_sum_tuple[3:6])

#Tupla mutable con conversion a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "HectorDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#Eliminacion
#del my_tuple([1]) # object doesn't support item deletion
#print(my_tuple)

del my_tuple # object doesn't support item deletion
print(my_tuple) # is not defined

