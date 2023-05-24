from mapping import MAPPING

string = input('What would you like to convert to Morse Code?\n')
print(f'Input:  {string}')

morse_code = ''
for letter in string:
    cap_letter = letter.upper()
    morse_code += MAPPING[cap_letter]

print(f'Output: {morse_code}')
