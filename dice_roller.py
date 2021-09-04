import random 

def main():
  dice_rolls  =  int ( input ( '¿Cuántos dados te gustaría tirar?' ))
  dice_size  =  int ( input ( '¿Cuántos lados tienen los dados?' ))
  dice_sum  =  0 
  for i in range(0,dice_rolls):
    rollo = random.randint(1,dice_size)
    dice_sum  + =  rollo 
    if rollo == 1:
       print(f'¡Has obtenido un {roll}! Fallo crítico')
    elif rollo == dice_size:
       print(f'Has obtenido un {roll} !Éxito crítico!')
    else:
       print(f'haz lanzado un {roll}')
        
  print (f'Has obtenido un total de {dice_sum}')

if __name__== "__main__":
  main()