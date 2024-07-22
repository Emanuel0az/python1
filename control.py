import calculator

def main():
    while True:
        print("welcome to my first calculator. pleas choose an operation")
        option = input("(+,-,*,/,q)")
        
        if option == "q":
            print("quitting the program")
            break
        
        if option not in ["+","-","+","/"]:
            print(f"Error: invalid option{option}")
            continue
    
        try:
            num1 = float(input("input the first number: "))
            num2 = float(input("input the second number: "))
        except ValueError:
            print("Error: invalid input. please input a number")
            continue
        
        if option == "+":
            resullt = calculator.add(num1, num2)
        elif option == "-":
            resullt = calculator.subtract(num1, num2)
        elif option == "*":
            resullt = calculator.multiply(num1, num2)
        else:
            result = calculator.divide(num1, num2)
            
        
        print(f"the result is {resullt}")
        
        
if __name__ == "__main__":
    main()