import json
from pprint import pprint
with open('books.json') as data_file:    
    data = json.load(data_file)

print(len(data['bookstore']['book']))