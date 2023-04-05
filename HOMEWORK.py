# alphabet wars
# https://www.codewars.com/kata/59377c53e66267c8f6000027



# original solution:

# a dictionary for each side (left, right)
# add keys and values inside each dictionary
# loop through input
# 2 variables (right / left)
# add values to matching variable
# loop over each dictionary and compare each key
# if else to determine who wins
# return result!!!

left_side = {
    "w":4,
    "p":3,
    "b":2,
    "s":1,
    }

right_side = {
    "m":4,
    "q":3,
    "d":2,
    "z":1,
    }

def alphabet_war(fight):
    left_side_count = 0
    right_side_count = 0
    for ch in fight:
        if ch in left_side:
            left_side_count += left_side[ch]
        elif ch in right_side:
            right_side_count += right_side[ch]
            
    if left_side_count > right_side_count:
        return("Left side wins!")

    elif right_side_count > left_side_count:
        return("Right side wins!")

    else:
        return("Let's fight again!") 
    

# updated and (hopefully) better solution:

# 1 dict for both sides
# --> 1 side pos values 
# --> other side neg values 
# sum for both sides after 'fight'
# if sum pos --> "left side wins"
# if sum neg --> "right side wins"


dict = {"w":4,
        "m":-4,
        "p":3,
        "q":-3,
        "b":2,
        "d":-2,
        "s":1,
        "z":-1,
        }

def alphabet_war2(fight):
    battle = sum(dict[ch] for ch in fight)
    
    if battle > 0:
        return("Left side wins!")

    elif battle < 0:
        return("Right side wins!")

    else:
        return("Let's fight again!") 
    


fight = "wwwwwwz"

# I think this way might be better for space and time complexity, because not only do we only have 1 dictionary to loop through, 
# but all the parts of this code should just be linear, or constant, and nothing is nested into anyhting else to make it quadratic.



print(alphabet_war(fight))
print(alphabet_war2(fight))