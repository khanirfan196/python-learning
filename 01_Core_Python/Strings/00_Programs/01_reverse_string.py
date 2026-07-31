

my_str = "seven wonders"

# Reverse of string, python way

print(my_str[::-1])

# Manual code to reverse string

s = len(my_str)+1

for i in range(-1, -s, -1):
    print(my_str[i], end="")