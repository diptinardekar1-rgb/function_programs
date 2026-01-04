# using arithmetic oprator

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "//":
        return a//b
    elif operator == "**":
        return a**b
    else:
        return "Invalid operator"
    
    
print(calculator(40,60, "+"))
print(calculator(40,60,"-"))
print(calculator(40,60,"*"))
print(calculator(40,60, "/"))
print(calculator(40,60, "//"))
print(calculator(4,5, "**"))

#100
#-20
#2400
#0.6666666666666666
#0
#1024


#using assignment  oprator

def update_balance(balance,action):
    if action == "deposit":
        balance += 10000
        return balance
    elif action == "withdraw":
        balance -= 1000
        return balance
    else:
        return "invalid balance"
    
    
ot = update_balance(10000,"deposit")
print(ot)
ot = update_balance(10000,"withdraw")
print(ot)

#20000
#9000
    
    
def bank_balance(balance):
    balance += 500
    balance -= 200
    balance *= 2
    balance //= 3
    return balance

ot = bank_balance(1000)    #866
print(ot)


# using  and, or oprator
def exam_result(marks,attendence):
    if marks >= 35 and attendence >= 75 :
        return "pass"
    else:
        return  "fail"  
    
ot =exam_result(40,80)
print (ot)  
ot=exam_result(30,70)
print(ot) 


#pass
#fail

                        




  
           
    
 
   