import random 

print("Welcome to the Python PEMMDDAS Quiz Generator!\n")

num_q = int(input("Select number of questions: "))
num_d = int(input("Select difficulty (0-3): "))
# num_t = int(input("Select number of numerical terms per statement (2-10): "))
num_t = random.randint(2,5)
print("\n")

operators = ["+", "-", "*", "%", "/", "//", "**"]

for i in range(num_q):
    print("Question ", i+1)

    ques = []
    limit = 10 ** num_d

    for j in range(num_t):
        if limit == 1:
            rx = random.randint(1,5)
        else:
            rx = random.randint(1, limit)
        ques.append(rx)
        ques.append(random.choice(operators))
        num_t = random.randint(2,5)
    
    ques = ques[:-1]

    st = ""
    for q in ques:
        st += str(q) + " "

    st += "= "
    que = input(st)

    ans = eval(st[:-2])

    if "." in que:
        que = float(que)
    else:
        que = int(que)
    
    if que == ans:
        print("Correct!")
    else:
        print("Correct Answer: ", ans)
    print("")

    





