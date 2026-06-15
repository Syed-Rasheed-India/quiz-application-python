quiz_list = {
    "What keyword is used to define a function in Python?": "def",
    "What keyword is used to create a class in Python?": "class",
    "Which data type stores True or False values?": "bool",
    "What method adds an item to a list?": "append",
    "What method removes the last item from a list?": "pop",
    "Which loop is used when the number of iterations is known?": "for",
    "Which loop runs until a condition becomes False?": "while",
    "What symbol is used for comments in Python?": "#",
    "What function is used to get user input?": "input",
    "What function is used to display output?": "print",
    "What keyword is used for inheritance?": "inheritance",
    "What special method is called when an object is created?": "__init__",
    "Which data structure stores key-value pairs?": "dictionary",
    "What keyword is used to handle exceptions?": "try",
    "What keyword is used to define an anonymous function?": "lambda",
    "Which keyword exits a loop immediately?": "break",
    "Which keyword skips the current iteration?": "continue",
    "What does OOP stand for?": "object oriented programming",
    "What keyword is used to create an object of a class?": "none",
    "Which method converts a string to lowercase?": "lower"
}

result =0

for ques,ans in quiz_list.items():
    print(ques)
    answer = input("please enter your answer : ")
    if answer == ans:
        print(f"{ans} is correct")
        result+=1
    else:
        print(f"{answer} is incorrect")

user=input("Do you want to see your marks : ")

if user == "y" or user == "Y" or user == "yes" or user == "Yes":
    print("your mark is ",result)
else:
    print("thank you for using this system !!! All The Best !!!")