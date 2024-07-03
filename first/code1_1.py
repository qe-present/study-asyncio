import requests

response = requests.get('http://www.example.com')  # I/O 密集型操作
item = response.headers.items()
headers = [f'{key}: {value}' for key, value in item]  # CPU 密集型操作
formattered_headers = '\n'.join(headers)  # CPU 密集型操作
with open('headers.txt', 'w') as f:
    f.write(formattered_headers)  # I/O 密集型操作
