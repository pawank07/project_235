import requests

for i in range(1,1000):
    URL= f'https://networking-ecommerce-new.onrender.com/profile?id={i}'
    req= requests.get(url=URL)
    if req.status_code == 200:
        print(URL)