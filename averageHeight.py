listOfHeights = []
answer = 'Not Done'
totalHeight = 0
countHeights = 0

print('Please enter a list of heights. To finishing adding heights reply anytime with [done].')
while answer != 'done':
    answer = input('\nWhat is the height in cm?\nType [done] to end adding additioanl heights\n').lower()
    if answer != 'done':
        if isinstance(float(answer), float) == True:
            listOfHeights.append(answer)
            countHeights += 1
            
        else:
            print('\nPlease enter a number.')

for i in listOfHeights:
    totalHeight += float(i)
    
print(f'\nThe average height is {totalHeight/countHeights}, with {countHeights} people participating.')