# Review MathsIsFun: Definition of Average. Create a program that asks the user 
# to enter grade scores. Start by asking the user how many scores they would like
# to enter. Then use a loop to request each score and add it to a static 
# (fixed-size) array. After the scores are entered, calculate and display the high, 
# low, and average for the entered scores.
def main():
    print("\t\t\tMy Scores")
    print("\t\t\t_________\n")
    amount = get_amount()
    scores = get_scores(amount)
    summation = sum(scores)
    average = summation/amount
    print("The lowest score is: ", min(scores))
    print("The highest score is: ", max(scores))
    print("the average is: ", average)

def get_amount():
    print("Enter amount of scores")
    amount = int(input('-> '))
    return amount

def get_scores(amount):
    grades = []
    print("Enter scores")
    count = 0
    while True:
        count = count + 1
        entry = input('-> ').strip()
        # the program doesn't count the last enry 'scores'
        if (amount == count):
            break
        try:
            grades.append(float(entry))
        except ValueError:
            print("ERROR: {!r} you must enter a number, please try again.".format(entry))
    return grades

main()