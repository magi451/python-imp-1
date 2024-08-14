def parse_input(input_string):
    output = ""
    i = 0
    while i < len(input_string):
        char = input_string[i]
        i += 1
        count = 0
        while i < len(input_string) and input_string[i].isdigit():
            count = count * 10 + int(input_string[i])
            i += 1
        output += char * count
    return output

while True:
    input_string = input("Enter a string: ")
    output_string = parse_input(input_string)
    print(output_string)
"""example :
in output if you enter a3d10
the out put will be
aaaddddddddd
3 a's and 10 d's
"""
