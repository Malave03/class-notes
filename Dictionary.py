
scores = {
    "x" : 0,
    "o" : 0
    }

#x_or_o

tracker = open('tic-tac-toe-4.py', 'r')



winners = [x_or_o] + 1
for winner in winners:
    scores[winner] += 1
#print(scores)
# write scores to a text file.

with open("scores.txt","w") as hs:
    for key, value in scores.items():
        hs.write(key+ " ")
        hs.write(str(value))
        hs.write("\n")
        
new_scores ={}
        
with open("scores.txt", "r") as hs:
    
# read in high scores and add them to the dict
    for line in hs:
        new_scores[line[0]] = int(line[2])
        
print("ns: ", new_scores)

new_scores["x"]+=1

print("ns: ", new_scores)

