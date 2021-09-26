# This is exercise 0 where I am going to try to extract the information from a text file,
# read it in, convert each string into an index and then index each part of those strings,
# and then use sorting methods to achieve our goal


def main():
    abc_sort()
    num_sort()

def abc_sort():
    with open('f1.txt') as f:
        for line in sorted(f):
            print(line, end='')


def num_sort():
    nums = []
    with open('f1.txt') as f:
        for words in f.split():
            if words.isdigit():
                nums.append(int(words))
        
        print(nums)


