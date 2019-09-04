numbers = list()

# for i in range(1, 101):
#     if i % 5 == 0 and i % 7 == 0:
#         print("ChickenMonkey")
#     elif i % 7 == 0:
#         print("Monkey")
#     elif i % 5 == 0:
#         print("Chicken")
#     else:
#         print(i)

for i in range(1, 101):
    output = ""
    if(i % 5 == 0):
        output = f'Chicken'
    if(i % 7 == 0):
        output = f'{output}Monkey'

    print(output if output != "" else i)
