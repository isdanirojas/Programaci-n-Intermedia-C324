#//Digitalar una persona
#cedula
#nombre
#apellidopaterno
#apellidomaterno
#fecha de nacimiento
#correo
#direccion
#numero de telefono
#sexo
#edad se puede calcular


#el diccionaro de datos se construye o se declara

personadiccionario = {    
    "cedula" : "123",
    "nombre" : "Mario",
    "apellidopaterno" : "Jimenez",
    "apellidomaterno" : "Espinoza",
    "fechadenacimiento" : "12 setiembre",
    "correo": "mjimeneze@ufidelitas.com",
    "direccion":"Puntarenas",
    "numerodetelefono": "61383453",
    "sexo":"hombre",
    "activo" : True
}

print(personadiccionario)
print(personadiccionario["nombre"])

personadiccionario["nombre"] = "Nuevo Nombre"

print(personadiccionario["nombre"])

#eliminar un valor???
del personadiccionario["nombre"]
print(personadiccionario)