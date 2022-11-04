alphs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 'y', "z"]
word = input("enter the word u want to code or decode")
shift = int(input("enter the shift"))
code = []
decode = []
def codes(word):
    for letter in range(0, len(word)):
        for let in range(0, 26):
            if alphs[let] == word[letter]:
                if(let+shift) > 25:
                    code.append(alphs[shift-1])
                else:
                    code.append(alphs[let+shift])
    print(code)
def decode (word):
    for letter in range(0, len(word)):
        for let in range(0, 26):
            if alphs[let] == word[letter]:
                if(let+shift) > 25:
                    code.append(alphs[shift-1])
                else:
                    code.append(alphs[let-shift])
    print(code)
choice = input("do u want to code or decode the message press c for code and d for decode")
if("c" == choice):
    codes(word)
elif("d" == choice):
    decode(word)