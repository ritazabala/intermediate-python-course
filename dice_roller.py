import random 

def main():
  rolls = 2
  dice_sum = 0
  for i in range(0,rolls):
    roll = random.randint(1,6)
    if roll == 1:
       print(f'¡Has obtenido un {roll}! Fallo critico')
    else:
    print(f'haz lanzado un {roll}')
    dice_sum = dice_sum + roll
    
  print ( f'Has obtenido un total de {dice_sum}' )

if __name__== "__main__":
  main()