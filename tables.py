#Table of any random number till 10
#No installation of any library required
#By - Atul Jha

def main():
    num = int(input('Which number you want to multiply:'))
    print('Here is your table')
    for i in range(1, 11):
        print(num, 'x' , i, '=' ,num*i)

if __name__ == '__main__':
    main()
