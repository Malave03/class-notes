# Bugs in refactored checking for winners.
# Find the bugs, consider how you would correct it

##########################
# Drawing code from homework 5
##########################

import turtle as t

### Make your draw_board() function here.

def teleport(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_board():
    # This draws the tic -tac-toe board 
    teleport(-250,100)
    t.forward(500)
    teleport(-250,-100)
    t.forward(500)
    teleport(-100,250)
    t.right(90)
    t.forward(500)
    teleport(100,250)
    t.forward(500)

def center_coords_for_drawing(x_coord, y_coord, x_or_o):
    # We center the x and y coords
    # This function also adds and "x" or "o" to the board list

    # center the x
    if x_coord < -100:
        x_coord = -175
        col_idx = 0
    elif x_coord > 100:
        x_coord = 175
        col_idx = 2
    else:
        x_coord = 0
        col_idx = 1
        
    # center the y
    if y_coord < -100:
        y_coord = -175  # bottom row in board
        row_idx = 2
    elif y_coord > 100:
        y_coord = 175   # top row in board
        row_idx = 0
    else:
        y_coord = 0    # middle row in board
        row_idx =1
        
    board[row_idx][col_idx] = x_or_o
    
    return x_coord, y_coord

def draw_x(x_coord,y_coord):
     
#     'x' == x
    
    x_or_o = "x"
    
    x_coord, y_coord = center_coords_for_drawing(x_coord,y_coord, x_or_o)
    
    winner = check_for_winners()

    update_scores_txt(winner,x_or_o)
    
    
    teleport(x_coord,y_coord)
    t.setheading(45)
    t.forward(50)
    t.backward(100)
    teleport(x_coord,y_coord)
    t.setheading(135)
    t.forward(50)
    t.backward(100)
    t.update()       # Update the screen after the x is drawn only needed for tracer(o)
    t.onscreenclick(draw_o) # After the x is drawn switch to draw o. 
    

def draw_o(x_coord,y_coord):
    
#     'o' == o
    
    x_or_o = "o"
    x_coord, y_coord = center_coords_for_drawing(x_coord,y_coord,x_or_o)
    
    winner = check_for_winners()
    
    update_scores_txt(winner,x_or_o)
    
    
    teleport(x_coord,y_coord)
    t.dot(100, "black")
    t.dot(98, "white")
    t.update()    # Update the screen (see draw_x)
    t.onscreenclick(draw_x)   #Switch to other shape ( see draw_o())
 
# Todo 1 experiment with tracer


# Todo 4 Remember that we need to update our board_list to check for winners,
# how can we do that with the centered x_coord, y_coord? Hint: the board is a list
# and lists are defined globally and the index should be [0,1,2] We'll do this together
# before merging our code

def print_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}  ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}  ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}  ")

#board[row][column]
board = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("Welcome to tic-tac-toe")

# We don't need to print board, but we'll keep it for now as a check to our GUI. 
print_board()


def check_for_winners():
    # initialize game variables
    winner = False
    
    #print("check for winners is being called")
    
    for idx in range(3):
        # check rows for winners
        if board[idx][0]==board[idx][1]==board[idx][2]:
            winner = True
        #check columns for winners
        if board[0][idx]==board[1][idx]==board[2][idx]:
            winner = True
    # check diags
    if board[0][0]==board[1][1]==board[2][2]:
        winner = True
    if board[2][0]==board[1][1]==board[0][2]:
        winner = True

    print_board()
    if winner == True:
        #print(f"The winner is: {x_or_o}")
        print("Game Over")
        
    return winner
#         t.mainloop
        #return x_or_o


def update_scores_txt(winner,x_or_o):
        if winner == True:
        scores[x_or_o] =+ 1
        print(scores)# del;ete this part 
        with open('scores.txt', 'w') as hs:
            hs.write('x'+str(scores['x'])+ '\n')
            hs.write('o'+str(scores['o']))
    

t.onscreenclick(draw_x)       
t.tracer(0) #make drawing seem instantanious
t.ht() # make the little triangle turtle disappear    
draw_board()
t.listen()  
t.update()

# 1. Read in old scores, add to dictionary
scores = {}
with open('scores.txt', 'r') as hs:
    for line in hs:
        scores[line[0]] = int(line[2])
        

    
#     hs.read()
    
    #********with open('dictionary.py', a') as d***********
    
    
    
#     with open('winner_tracker.txt', 'a') as wt:
#         wt.append()
    

#2. Add x or o to the scores
# scores['x'] += 1
# 
# scores['o'] += 1


        
        #*********find where to uses these****
# 'x' += 1
# 
# 'o' += 1

# winner_x = x + 1
# 
# winner_o = o + 1
#         #*************************************
# 
# #3. Write the scores in scores.txt






# 
# while True:
#     if winner == t.onscreenclick(draw_x):
#         with open('scores.txt', 'a') as hs:
#             
#             for line in hs:
#                 hs.seek[0]
#                 hs.read()
#                 hs.write(winner_x)
#                 
#     if winner == t.onscreenclick(draw_x):           
#         with open('scores.txt', 'a') as hs:
#             
#             for line in hs:
#                 hs.seek[1]
#                 hs.read()
#                 hs.write(winner_o)        
# 
# #4. Add score to tic tac toe screen




#                 
# 
#     
#     
# with open ('tic-tac-toe-4.py', 'a') as tt:
#     tt.seek(screen)
#     tt.append(line) 



t.done()

#the_winner = game_loop()

# write high scores,
# Todo we still need a better way to form about this
# with open("scores.txt", "a") as hs:
#     hs.write("player \t wins\n")
#     hs.write(the_winner+"\n")
    # write discards previous text










# read the txt file, display winners
# play game
# get the winner x, o
# write the winner to a txt file
# 


# TODO Implement a play again feature

if __name__ == "__main__":
    game_loop()
