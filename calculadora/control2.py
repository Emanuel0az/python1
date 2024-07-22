import calculadora.calculator2 as calculator2

def main():
    while True:
        print("Welcome to my calculator. Please choose an operation")
        option = input("(+,-,*,/,q): ")
        
        if option == "q":
            print("Quitting the program")
            break
        
        if option not in ["+", "-", "*", "/"]:
            print(f"Error: invalid option {option}")
            continue
    
        try:
            numbers = input("Input the numbers separated by space: ").split()
            numbers = [float(num) for num in numbers]
            
            if len(numbers) < 2:
                print("Error: Please input at least two numbers.")
                continue
            
        except ValueError:
            print("Error: invalid input. Please input numbers separated by spaces.")
            continue
        
        if option == "+":
            result = calculator2.add(numbers)
        elif option == "-":
            result = calculator2.subtract(numbers)
        elif option == "*":
            result = calculator2.multiply(numbers)
        else:
            result = calculator2.divide(numbers)
            
        print(f"The result is {result}")

if __name__ == "__main__":
    main()
