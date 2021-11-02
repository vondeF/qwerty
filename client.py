import requests

response = requests.get('http://127.0.0.1:5000/currentTime')  # get-запрос по соответсвующему адресу

if response.status_code == 200:
    print('Данные найдены')
elif response.status_code == 404:
    print('Данные не найдены')

print('По запросу получили: ' + response.text)
