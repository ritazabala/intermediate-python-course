import random 

def main():
  rolls = 2
for i in range(0, rolls):
  roll = random.randint(1,6)
  print(f'haz lanzado un {roll}')

if __name__== "__main__":
  main()
