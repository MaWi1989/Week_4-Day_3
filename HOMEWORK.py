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




# Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

# first approach:
def get_count(sentence):
    vowel_count = 0
    for ch in sentence:
        if ch in 'aeiou':
            vowel_count += 1 
    return vowel_count



# better approach:
def get_count2(sentence):
    count = [sentence.count('a'), sentence.count('e'), sentence.count('i'), sentence.count('o'), sentence.count('u')]
    result = sum(count)
    return result

sentence = 'falalalala sweet in and out'

print(get_count(sentence))
print(get_count2(sentence))


# since there are only 5 possible vowels, it might be better to count each one of them, list the counts and then sum up that list, 
# than to have a for loop with an if statement and a membership test as in the first approach




# cats and shelves
# https://www.codewars.com/kata/62c93765cef6f10030dfa92b
# first approach:
def solution(start, finish):  
    current_shelf = start
    moves_count = 0
    while current_shelf < finish:
        if finish < (current_shelf + 3):
            current_shelf += 1
            moves_count += 1
        else:
            current_shelf += 3 
            moves_count += 1
      
    return moves_count


# better approach:
# num of shelves to climb = finish - start
# devide num of shelves to climb by 3: result = how many '3-step-moves'
# if remainder: remainder = how many '1-step-moves'
# add num of moves together for final count

def solution2(start, finish): 
    steps = finish - start
    final_count = [(steps // 3), (steps % 3)]
    return sum(final_count)


# second approach has no while loop, no if - else statements, just a couple of equations and a sum(), nothing nested


print(solution2(1,35))
