# Beginning: create variables
cat_points = 0
dog_points = 0

# Middle: Ask questions
# question 1:
answer = input ("On a weekend would you rather A) exercise all day, or B) chill all day?")
if answer == "A":
    dog_points += 1
elif answer == "B":
    cat_points += 1  

# question 2:
answer = input("Are you A) a person that likes to go outside, or B) a person that likes to stay in the house?")
if answer== "A":
    dog_points += 1
elif answer== "B":
    cat_points += 1

# question 3:
answer = input("Are you A) a person that likes hanging out with friends, or B) a person that likes being alone?")
if answer== "A":
    dog_points += 1
elif answer== "B":  
    cat_points += 1             

# question 4:
answer = input("Are you A) a person that talks a lot, or B) a person that doesn't talk a lot?")
if answer== "A":
    dog_points += 1
elif answer== "B":  
    cat_points += 1     

# question 5:
answer = input("Are you A) a person that plays sports, or B) a person that doesn't like sports?")
if answer== "A":
    dog_points += 1
elif answer== "B":  
    cat_points += 1     

# End: Determine results
if dog_points > cat_points:
    print("you are a dog")
elif cat_points > dog_points:
    print("you are a cat")        