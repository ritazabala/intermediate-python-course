import random 
def main():
  dice_rolls = 2
  for i in range(0,dice_rolls):
  	rollo = random.randint(1,6)
	  print ( f'Has lanzado un { rollo } ' )

if __name__== "__main__":
  main()
