#Just a practice file to try different ideas without having to use my main

import re
f1 = open('f1.txt')
new_lines = []
nums = []
spl_lines = []
racers = []
with open('f1.txt') as f:
  lines = f.readlines()
  for x in lines:
    new_lines.append(x.strip())
    
  #print(new_lines)
  i = 0
  while i < len(new_lines):
    #print(i, end = " ")
    racers = new_lines[i]
    #print(racers)
    racers.replace(" ", ",")
    i += 1
    print(racers)
    break;  
    # if len(racers) < 25:
    #   print(racers)
    # else:
    #   print("broke")


  #print(racers)

  # for i in range(len(new_lines)):
  #   if i < 20:
  #     print(i, end = " ")
  #     racers = new_lines[i]
  #     print(racers)
  #   else:
  #     break
  # print(re.sub("\s+", ",", racers.strip()))


  # for r in racers:
  #     print(re.sub("\s+", ",", racers.strip()))
    
    #for i in range(len(racers)):
      #print(re.sub("\s+", ",", racers[i].strip()))

  #re.sub("[ ]", ",", racers)
  # for line in new_lines:
  #   l=line.strip().split(',')
  #   spl_lines.append(sorted(l[:2])+sorted(l[2:]))
    #print(spl_lines)

    # for i in spl_lines:
    #   print(','.join(i))


    # if y.isdigit():
    #   print(y)
    #   nums.append(int(y))
    # for words in f:
    #   if words.isdigit():
    #     nums.append(int(words))
        
#print(nums)
#print(f1)

# Class Drivers(racers):
# def __init__(self, number):
#         self.number = number
# drivers = []

# for i in range(len(new_lines)):
