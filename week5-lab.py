#while: depends on the condition
#for: sequence or number of the iterations are known

#continue: skip tge remaining steps of current iteration and move to next one
#break: stop the loop when called/ comes out of loop

#counter
#accumulator
#input validation using loops

# #while loop
# counter: int = 0
# while counter < 5:
#     print(counter,"Hello World")
#     counter += 1

# for loop
# print(list(range(5))): start from 0 to n-1, inc/dec: +1
# print(list(range(1,5))): start from 1 to n-1, inc/dec: +1
# print(list(range(1,10,2))): start from 1, to n-1, inc/dec: +2


# for counter in range(5):
#     print(counter,"Hello World")

#problem: check grade input and its range
# while True:
#     input_grade: str = input("Enter your grade: ")
#
#     if not input_grade.replace(".", "", 1).isnumeric():
#         print("Invalid Grade")
#         continue
#
#     grade: float = float(input_grade)
#     if not 0 <= grade <= 100:
#         print("Out of range")
#         continue
#
#     else:
#         print("Grade: ", grade, type(grade))
#         break


# problem: input 5 grades and check for validation
# counter: int = 1
# total: float = 0
# while counter < 6:
#     input_grade = str = input(f"enter your grade {counter}: ")
#
#     if not input_grade.replace(".", "", 1).isnumeric():
#         print("invalid input")
#         continue
#
#     grade: float = float(input_grade)
#     if not 0 <= grade <= 100:
#         print("out of range")
#         continue
#
#     total += grade
#     counter += 1
#
# print(f"total grade: {total:.2f}")

