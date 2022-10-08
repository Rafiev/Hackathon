import json
import datetime

FILE_PATH = 'data.json'

def get_data(ge_price = None, le_price = None, sale = None, sold = None):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        new_data = [i for i in data if i['price'] >= ge_price]
        return new_data
    if le_price:
        new_data = [i for i in data if i['price'] <= le_price]
        return new_data
    if sale:
        new_data = [i for i in data if i['status'] is True]   
        return new_data
    if sold:
        new_data = [i for i in data if i['status'] is False]
    
    return data


def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]    
    if one_data:
        return one_data[0]
    return 'There are no such courses.'



def post_data():
    data = get_data()
    max_id = max([i['id'] for i in data ])
    data.append({
        'id': max_id + 1,
        'name': input('Enter name of course: '),
        'price': float(input('Enter price for course: ')),
        'date of creation': str(datetime.date.today()),
        'date of update': str(datetime.datetime.now()),
        'description': input('Enter course descriptions: '),
        'status': True
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'Courses successfully added'


def data_update(id):
    data = get_data()
    update_data = [i for i in data if i['id'] == id]
    if update_data :
        index_ = data.index(update_data[0])
        data[index_]['date of update'] = str(datetime.datetime.now())
        if input('Do you want change name: (yes/no) ') == 'yes':
            data[index_]['name'] = input('Enter new name: ')
        if input('Do you want change price: (yes/no) ') == 'yes':
            data[index_]['price'] = input('Enter new price: ')
        if input('Do you want change description: (yes/no) ') == 'yes':
            data[index_]['description'] = input('Enter description: ')
        if input('Do you want change status: (yes/no) ') == 'yes':
            data[index_]['status'] = input('Enter status of course sale(True)\sold(False): ')
        json.dump(data, open (FILE_PATH, 'w'))
        return 'Course successfully updated'
    return 'There are no such courses.'    

def delate_data(id):
    data = get_data()
    data_delate = [i for i in data if i['id'] == id]
    if data_delate:
        data.remove(data_delate[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Course successfully daleted'
    return 'There are no such courses'

def filter_by_date():
    data = get_data()
    request = input('When the courses was added(year-month-day): ')
    new_data = [i for i in data if i['date of creation'] == request]
    if new_data:
        return new_data
    else:
        return 'There are no such courses'
