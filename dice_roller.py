import random
def main():
  dice_sum = 0
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  for i in range(0,dice_rolls):
    roll = random.randint(0,dice_size)
    dice_sum += roll
    if roll == 1:
    	print('You rolled a', roll,'! Critical Fail')
    elif roll == 6:
    	print('You rolled a', roll,'! Critical Success!')
    else:
    	print('You rolled a', roll)
    print('You have rolled a total of ', dice_sum)

if __name__== "__main__":
  main()