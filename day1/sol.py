import re

#Solution 1 
def get_num(line):
    r = []
    for l in line:
        if l in '0123456789': 
            r.append(l) 
    
    first = r[0]
    last = r[0]
    if len(r) > 0:
        last = r[-1] 
    num = first + last 
    return int(num) 

#Solution 2
def get_num2(line):
    s = ['' for s in range(len(line))] 

    for i, n in enumerate(
        ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        if n in line:
            occurences = [m.start() for m in re.finditer(n, line)]
            for o in occurences:
                s[o] = str(i)
    
    for i,l in enumerate(line):
        if l in '0123456789':
            s[i] = l
    
    r = [] 
    for t in s:
        if t == "":
            continue 
        r.append(t)
    first = r[0]
    last = r[-1]
    num = first + last 
    return int(num) 

def read(file="problem.txt"):
    r = 0 
    with open(file, "r") as f:
        for l in f:
            if l == "" or l == "\n":
                continue 
            print(l[0:len(l)-1], ":", get_num2(l))
            r += get_num2(l)
    return r


testcases = [["two1nine", 29],
 ["eightwothree", 83],
 ["abcone2threexyz", 13],
 ["xtwone3four", 24], 
 ["4nineeightseven2", 42],
 ["zoneight234", 14],
 ["7pqrstsixteen", 76],
  ["eightthree8fiveqjgsdzgnnineeight", 88]]

def assert_all(testcases):
    for testcase in testcases:
        assert get_num2(testcase[0]) == testcase[1], testcase[0] + " failed!"

print(read())           