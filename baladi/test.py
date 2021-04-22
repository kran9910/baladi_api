from datetime import datetime

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baladi.settings')
import django
django.setup()

from api.models import Citizen

from django.conf import settings

citizen = Citizen(user=123, citizen_id='12', phone_number='123', first_name='kam',last_name='last_name', address='address', email='email', profile_pic='', birthdate='2021-12-12')
print(citizen)
print('hi')