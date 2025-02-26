# Advent of Code
# Day 9
# Part 1
# n8trium

total=0
data = []
disk_map = []
with open('input.txt') as fp:
    for line in fp:
        data+=line
print(data)

for i in range(len(data)):
    if i%2==0:
        x=0
        while x < int(data[i]):
            disk_map.append(str(i//2))
            x+=1
    else:
        x=0
        while x < int(data[i]):
            disk_map.append('.')
            x+=1

j=len(disk_map)-1
for i in range(len(disk_map)):
    if disk_map[i]=='.': # find next free spot
        while j > i:
            if disk_map[j]!='.': # find last spot with data
                print(f'Swapping: {i} {j}')
                disk_map[i] = disk_map[j]
                disk_map[j] = '.'
                break
            else:
                j-=1

for i in range(len(disk_map)):
    print(disk_map[i], end='')
    if disk_map[i].isdigit():
        total+=i*int(disk_map[i])
print(f'\n\nTotal: {total}')