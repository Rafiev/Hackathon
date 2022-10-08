from views import *

def main():
    while True:
        print('Welcome, this is makers functionality:\n\n0 - Exit from  functionality\n1 - Get list of all courses \n2 - Get a certain course\n3 - Add course \n4 - Delete course \n5 - Update course\n6 - Filter by date\n')
        method = input('Enter number: ')
        if method == '1':
            request = input('Do you want to filter courses by price?\nIf yes, type "more" or "less" ,if you dont want to filter, type "no": ')
            if request == 'more': 
                print(get_data(ge_price = float(input('Enter the number to filter with: '))))
            elif request == 'less':
                print(get_data(le_price = float(input('Enter the number to filter with: '))))
            elif request == 'no':
                print(get_data())
                continue
            else:
                print('Invalid request')
                continue
            request2 = input('Do you want to see sale course, type "1" - If you want to see sold course type "0": ')
            if request2 == '1':
                print(get_data(sale = True))
            elif request2 == '0':
                print(get_data(sold = False))
            else:
                print('Invalid request')
        elif method == '2':
            id = int(input('Enter course id: '))
            print(get_one_data(id))
        elif method == '3':
            print(post_data())
        elif method == '4':
            id = int(input('Enter course id: '))
            print(delate_data(id))
        elif method == '5':
            id = int(input('Enter course id: '))
            print(data_update(id))
        elif method == '6':
            print(filter_by_date())
        elif method == '0':
            print('You exit from functionality')
            break
        else:
            print('No such functionality') 



if __name__ == '__main__':
    main()