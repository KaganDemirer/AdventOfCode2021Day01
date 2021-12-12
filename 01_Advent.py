with open('01_Advent.txt') as input_file:
    lines = input_file.readlines()

list_of_depths = []
larger_measurments = 0

for x in lines:
    list_of_depths.append(x.replace("\n",""))

def first_exercise():
    global larger_measurments
    for x in range(len(list_of_depths)):
        if x!=0:
            if list_of_depths[x]>list_of_depths[x-1]:
                larger_measurments+=1

def second_exercise():
    global larger_measurments
    for x in range(len(list_of_depths)-3):
        a = int(list_of_depths[x]) + int(list_of_depths[x+1]) + int(list_of_depths[x+2])
        b = int(list_of_depths[x+1]) + int(list_of_depths[x+2]) + int(list_of_depths[x+3])
        if b>a:
            larger_measurments+=1
        print()

second_exercise()
print(larger_measurments)