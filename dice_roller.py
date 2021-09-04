import random 

def main():
  rolls = 2
  dice_sum = 0
  for i in range(0,rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    print(f'haz lanzado un {roll}')
  print ( f'Has obtenido un total de {dice_sum}' )

if __name__== "__main__":
  main()
