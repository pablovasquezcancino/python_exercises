print ("bienvenido al Quiz bostero ")

playing = input("querés jugar pibe? ")
if playing != "si":
    quit()
    
print("BOCA NO TEME LUCHAR!.")
print("Querido bostero, ingrese solo numeros en su respuesta, gracias :)")
puntaje = 0

# PREGUNTA UNO
pregunta = input("¿En que año fue fundado boquita? ")
if pregunta == "1905":
    print("Excelente, es correcto bostero. Boquita fue fundado el 3 de abril de 1905")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. Boquita fue fundado el 3 de abril de 1905")
    
    
# PREGUNTA DOS
pregunta = input("¿En que año debuto como dt. Carlos Bianchi? ")
if pregunta == "1998":
    print("Excelente, es correcto bostero. El virrey debutó como técnico xeneise el 9 de agosto de 1998 contra ferro,con victoria por 4-2")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. El virrey debutó como técnico xeneise el 9 de agosto de 1998 contra ferro,con victoria por 4-2")
    

# PREGUNTA TRES
pregunta = input("¿Cuántos goles hizo Martín Palermo con la azul y oro? ")
if pregunta == "236":
    print("Excelente, es correcto bostero. Martín hizo 236 goles en 404 partidos, siendo el máximo artillero en la historia del club")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. Martín hizo 236 goles en 404 partidos, siendo el máximo artillero en la historia del club")
    
    
# PREGUNTA CUATRO
pregunta = input("¿En que año debuto JUAN ROMAN RIQUELME con la camiseta xeneise? ")
if pregunta == "1996":
    print("Excelente, es correcto bostero. El último romántico debuto un 10 de noviembre del año 1996")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. El último romántico debuto un 10 de noviembre del año 1996")
    
# PREGUNTA CINCO
pregunta = input("¿En que año Boca ganó su primera copa libertadores? ")
if pregunta == "1977":
    print("Excelente, es correcto bostero. Boca ganó su primera conmebol libertadores un 14 de septiembre de 1977, ganandole la final en un tercer partido a Cruzeiro")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. Boca ganó su primera conmebol libertadores un 14 de septiembre de 1977, ganandole la final en un tercer partido a Cruzeiro")
    

# PREGUNTA CINCO
pregunta = input("¿En que año Maradona gano el metropolitano vistiendo la camiseta del más grande? ")
if pregunta == "1981":
    print("Excelente, es correcto bostero. El Diego gano el Metropolitano 81.")
    puntaje += 1
else:
    print("Lo siento, es incorrecto :c. El Diego gano el Metropolitano 81.")
    
print ("***********************************************")
print("Gracias por jugar. Su puntaje a sido de ")
print(puntaje)
print( "de un total de 6 preguntas.")
print ("***********************************************")