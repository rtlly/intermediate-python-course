import random
def main():
  dice_roll = 2
  dice_sum = 0
  for i in range(0,dice_roll):
    roll = random.randint(0,6)
    dice_sum += roll
    print('You rolled a', roll)
    print('You have rolled a total of ', dice_sum)

if __name__== "__main__":
  main()