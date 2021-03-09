import requests

res = requests.post('http://127.0.0.1:8000/citizens/',json ={
    "citizen_id": "444",
    "phone_number": "555",
    "first_name": "ryan",
    "last_name": "abu",
    "email": "mail@mail.com",
    "address": "jesr el bacha",
    "birthdate": "2021-12-12",
    "authenticated": "false",
    "profile_pic": ""
})
print(res.text)

citizens = requests.get('http://127.0.0.1:8000/citizens')
print(citizens.text)