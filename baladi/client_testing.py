import requests

#CHANGE URL IN COMMENTED SECTIoN
#citizen = requests.get('http://127.0.0.1:8000/api/citizens/1')
#print("Citizen with id 1: ")
#print(citizen.text)

#citizens = requests.get('http://127.0.0.1:8000/api/citizens/')
#print("\nAll the Citizens before adding a new citizen")
#print(citizens.text)

from api.models import Citizen


#citizen = Citizen.objects.create(user=123, citizen_id='12', phone_number='123', first_name='kam',last_name='last_name', address='address', email='email', profile_pic='', birthdate='2021-12-12')
#citizen = Citizen.objects.all()
#print(citizen)
print('hi')
res = requests.post('http://127.0.0.1:8000/api/app/citizens/',json ={
    "user" : 123,
    "citizen_id": "12345",
    "phone_number": "555",
    "first_name": "ryan",
    "last_name": "abu",
    "email": "mail@mail.com",
    "address": "jesr el bacha",
    "birthdate": "2021-12-12",
    "profile_pic": ""
})

print("\nAdding this new Citizen: ")
print(res.text)

citizens = requests.get('http://127.0.0.1:8000/api/app/citizens/')
print("\nAll Citizens after adding the new citizen: ")
print(citizens.text)

#requests.delete('http://127.0.0.1:8000/api/citizens/5')
#print("\nThe new Citizen added now was deleted")

#citizens = requests.get('http://127.0.0.1:8000/api/citizens/')
#print("\nAll Citizens after deleting the new citizen: ")
#print(citizens.text)


print("\nAdding a new agent: ")
res = requests.post('http://127.0.0.1:8000/api/app/agents/',json ={
    "employee_id": "12345",
    "role":"Manager",
    "phone_number": "555",
    "first_name": "ryan",
    "last_name": "abu",
    "email": "mail@mail.com",
})
print(res.text)
agents = requests.get('http://127.0.0.1:8000/api/app/agents/')
print("\nAll Agents after adding the new citizen: ")
print(agents.text)

print("\nAdding a new Complaint: ")
res = requests.post('http://127.0.0.1:8000/api/app/complaints/',json ={
    "citizen_id" : "12345",
    "current_agent_id" : "12345",
    "type" : "complaint",
})
print(res.text)
complaints = requests.get('http://127.0.0.1:8000/api/app/complaints/')
print("\nAll Complaints after adding the new citizen: ")
print(complaints.text)

print("\nAdding a new Request: ")
res = requests.post('http://127.0.0.1:8000/api/app/requests/',json ={
    "citizen_id" : "12345",
    "current_agent_id" : "12345",
    "type" : "request",
})
print(res.text)
reqs = requests.get('http://127.0.0.1:8000/api/app/requests/')
print("\nAll Requests after adding the new citizen: ")
print(reqs.text)

print("\nAdding a new Post: ")
res = requests.post('http://127.0.0.1:8000/api/app/posts/',json ={

"text" : "Post 1",
"category" : "Info"
})
print(res.text)
posts = requests.get('http://127.0.0.1:8000/api/app/posts/')
print("\nAll Posts after adding the new citizen: ")
print(posts.text)
