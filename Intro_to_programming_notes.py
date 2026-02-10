#for loops = iteration


for i in range(10):
    print(i)
    
for word in ['hi','hello','goodday']: #This is a list
    #Word is a variable local to this loop 
    print (word)

    

#print some animal names
for animals in ['lion','penguin','turtle','zebra', 'coqui']:
    print (animals)

    
zoo= ['lion','penguin','turtle','zebra', 'coqui']
for animals in zoo:
    print (animals)


#'
#We want to add 1,2,3,4 together 
total = 0
for num in range(10,21):
    total = total + num
print (total)

# Use help to determine what best route to decide
# help (range)
#'
total=0
total_2= 0
for num_2 in range(100): # _ to show we are not using the variable 
    total += 1
    print('hi')
    total_2 -= 10
print(f' Here is toal: {total}, here is total_2: {total_2}')

#if the user types "yes" else if print 5 if "no" else print the zoo

def response():
    response= input('yes or no:')
    if response == 'yes':
            print (5)
    elif response == 'no':
        zoo = ['lion','penguin','turtle','zebra', 'coqui']
        for animals in zoo:
            print(animals)
