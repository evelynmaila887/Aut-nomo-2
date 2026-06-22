import random


print("¡Bienvenido al juegp de Piedra, Papel o Tijera!")
jugando = True
while jugando == True:
    jugador = input("Elije piedra, papel o tijera (o escribe 'salir' para terminar)")
    if jugador == "salir":
     print("!Gracias por jugar¡ Hasta la próxima.")
     jugando = False

else:
   opciones = ["piedra", "papel", "tijera"]
   computadora = random.choice(opciones)
   print("La computadora eligió:", computadora)

   if jugador == computadora:
      print("¡Es un empate!")
   elif jugador == "piedra":
      if computadora == "tijera":
         print("¡Ganaste! Piedra rompe tijeras.¡Buen trabajo!")
      else:
         print("Perdiste... El papel envuelve a la piedra. Suerte para la próxima.")