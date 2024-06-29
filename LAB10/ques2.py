import random 
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for i in range(6_00_000):
    die = random.randrange(1,7)

    if die == 1:
        frequency1+=1
    elif die == 2:
        frequency2+=1
    elif die == 3:
        frequency3+=1
    elif die == 4:
        frequency4+=1
    elif die == 5:
        frequency5+=1
    else:
        frequency6+=1

print("Frequency 1 = ",frequency1)
print("Frequency 2 = ",frequency2)
print("Frequency 3 = ",frequency3)
print("Frequency 4 = ",frequency4)
print("Frequency 5 = ",frequency5)
print("Frequency 6 = ",frequency6)

# import random

# def randomm_values(n):
#     for i in range(n):
#         return (random.randrange(1,7))

# frequency1 = 0
# frequency2 = 0
# frequency3 = 0
# frequency4 = 0
# frequency5 = 0
# frequency6 = 0

# def freq(die):
#     if die == 1:
#         frequency1+=1
#     elif die == 2:
#         frequency2+=1
#     elif die == 3:
#         frequency3+=1
#     elif die == 4:
#         frequency4+=1
#     elif die == 5:
#         frequency5+=1
#     else:
#         frequency6+=1

# def counts():
#     print("Frequency 1 = ",frequency1)
#     print("Frequency 2 = ",frequency2)
#     print("Frequency 3 = ",frequency3)
#     print("Frequency 4 = ",frequency4)
#     print("Frequency 5 = ",frequency5)
#     print("Frequency 6 = ",frequency6)

# inp = int(input("Enter the rolls = "))
# die = randomm_values(inp)
# freq(die)
# counts()