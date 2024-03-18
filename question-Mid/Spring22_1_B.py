#spring-2022-1-B
stu=float(input('enter your result :'))
if stu>4.00:
    print("something  is wrong .")
elif stu>=3.5:
    print("20 % waiver") 
elif 3.00<= stu <3.50:
    print("10% waiver")
elif stu<3.00:
    print("5% waiver")    
    
def calculate_waiver(semester_fee, cgpa):
    if cgpa > 3.50:
        waiver_percent = 20
    elif 3.00 <= cgpa <= 3.50:
        waiver_percent = 10
    else:
        waiver_percent = 5
    
    waiver_amount = (waiver_percent / 100) * semester_fee
    return waiver_amount

def main():
    semester_fee = float(input("Enter your semester fee: "))
    cgpa = float(input("Enter your CGPA: "))
    
    waiver_amount = calculate_waiver(semester_fee, cgpa)
    print(f"Your net waiver amount is: ${waiver_amount}")

if __name__ == "__main__":
    main()
    
           