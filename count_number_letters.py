#!usr/bin/python3

# Generate aphabetical representation of numbers
def numToWord(number):
    str_dict = {
    0:"", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
    14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",  18:"eighteen",
    19:"nineteen"
    }
    decDict = {
    2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy",
    8:"eighty", 9:"ninety"
    }
    word = ''
    if number < 20:
        word += str(str_dict[number])
    if 20 <= number < 100:
        strNum = str(number)
        word += decDict[int(strNum[0])]
        word += str_dict[int(strNum[1])]
    if (number >= 100) and (number < 1000):
        strNum = str(number)
        if strNum[1:] == "00":
            word += str_dict[int(strNum[0])]
            word += "hundred"
        elif strNum[1] == "0":
            word += str_dict[int(strNum[0])]
            word += "hundredand"
            word += str_dict[int(strNum[2])]
        elif strNum[1] == "1":
            word += str_dict[int(strNum[0])]
            word += "hundredand"
            word += str_dict[int(strNum[1:])]
        elif int(strNum[1:]) > 20:
            pass
            word += str_dict[int(strNum[1])]
            word += "hundredand"
            word += decDict[int(strNum[1])]
            word += str_dict[int(strNum[2])]
    if number == 1000:
        word += "onethousand"
    return word
# Count lettes in numbers

def count_letters(number_string):
    count = 0
    for i in number_string:
        count += 1
    return count


def count_letters_sequence(seqLength):
    count = 0
    for i in range(1, seqLength+1):
        count += count_letters(numToWord(i))
    return count
print(count_letters_sequence(1000))
