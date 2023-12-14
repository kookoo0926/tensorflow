
####################################################
# if / else (&&, ||, ! )

#---------------------------------------------------
# Sample 1)
"""
x = int(input("Input x : "))

if ( x % 2 == 0 ):  # Code Block
    print(f"Even Number")
    print("END")
else:
    print(f"Odd Number")
"""

#---------------------------------------------------
# Sample 2)
# score = float(input("Inout Score : "))
"""
if score >= 90:
    print("GP is A+")
elif score >=70 and score < 90:
    print("GP is A")
elif score >=50 and score < 70:
    print("GP is B")
elif score >=30:
    print("GP is C")
elif score >=10:
    print("GP is D")
else:
    print("See you again!!")
"""

#---------------------------------------------------
# Sample 3) - BMI
# height = float(input("Height (m) : "))
# weight = float(input("Wight (kg) : "))
# bmi = weight/(height*height)
# print(f"BMI = {bmi} : 몸무게(kg) / 키(m)*키(m)")
"""
if bmi >= 40:
    print("심각한 비만")
elif bmi >= 30 and bmi < 40:
    print("비만 2단계")
elif bmi >= 25 and bmi < 30:
    print("비만 1단계")
elif bmi >= 23 and bmi < 25:
    print("과체중")
elif bmi >= 18.5 and bmi < 23:
    print("정상")
elif bmi < 18.5:
    print("저체중")
"""

#---------------------------------------------------
# Sample 4)
val1, op, val2 = input("입력 : Input val1 op val2 : ").split()
val1 = float(val1)
val2 = float(val2)

if op == "+":
    print(f"출력 : Result (+) : {val1 + val2}")
elif op == "-":
    print(f"출력 : Result (-) : {val1 - val2}")
elif op == "*":
    print(f"출력 : Result (*) : {val1 * val2}")
elif op == "/":
    print(f"출력 : Result (/) : {val1 / val2}")
elif op == "%":
    print(f"출력 : Result (%) : {val1 % val2}")
else:
    print("잘못된 입력....")
