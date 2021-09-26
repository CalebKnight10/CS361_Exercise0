#My original steps and thought process of the exercise

f1 = open('f1.txt')
new_lines = []
nums = []
spl_lines = []
racers = []

1. Read File and prints (FN  LN  NUM  CAR)
f1 = open('f1.txt')
with open('f1.txt') as f:
  lines = f.readlines()
  for x in lines:
    new_lines.append(x.strip())
  print(new_lines)


2. Take info out and make list of indiviual drivers
for element in range(len(new_lines)):
    print(element, end = " ")
    racers = new_lines[element]
    print(racers)

3. Sort (abc and 123)

4. Put it all back together

5. Print
