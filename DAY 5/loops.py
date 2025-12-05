fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

    # loops allows us to execute thesame lines of code multiple times

student_scores =[150, 142, 120, 300, 184]

sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    
print(max_score)

sum = 0
for number in range(1, 10):
    sum += number
print(sum)





