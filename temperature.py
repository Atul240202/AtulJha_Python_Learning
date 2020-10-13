#Converting celcius to Farenhite and viceversa
#By- Atul Jha


def main():
    temp = int(input('Enter 1 for celcius or 0 for fahrient'))
    if temp==1:
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
    elif temp==0:
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
    else:
        print('Wrong input')

if __name__ == "__main__":
    main()
