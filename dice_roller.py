import random 

def main():
  rolls = int(input('¿Cuántos dados te gustaría tirar?'))
  size  =  int ( input ( '¿Cuántos lados tienen los dados?' ))
  dice_sum = 0
  for i in range(0,rolls):
    roll = random.randint(1,size)
    if roll == 1:
       print(f'¡Has obtenido un {roll}! Fallo crítico')
    elif roll == size:
       print(f'Has obtenido un {roll} !Éxito crítico!')
    else:
       print(f'haz lanzado un {roll}')
    dice_sum = dice_sum + roll
    
  print ( f'Has obtenido un total de {dice_sum}' )

if __name__== "__main__":
  main()