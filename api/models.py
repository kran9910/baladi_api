from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    citizen_id = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=511)
    last_name = models.CharField(max_length=511)
    email = models.CharField(max_length=511)
    address = models.CharField(max_length=16000)
    birthdate = models.DateField()
    authenticated = models.BooleanField(default=False)
    profile_pic = models.URLField(max_length=16000, blank=True)

    def __str__(self):
        return self.citizen_id


class Agent(models.Model):
    employee_id = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=511)
    last_name = models.CharField(max_length=511)
    email = models.CharField(max_length=511)
    role = models.CharField(max_length=511)

    def __str__(self):
        return self.employee_id


class Complaint(models.Model):
    citizen_id = models.ForeignKey(Citizen, to_field='citizen_id', on_delete=models.CASCADE)
    current_agent_id = models.ForeignKey(Agent, to_field='employee_id', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=2047, blank=True)
    picture = models.URLField(max_length=16000, blank=True)
    details = models.CharField(max_length=16000, blank=True)
    status = models.CharField(max_length=2047, default='Just Arrived')
    is_completed = models.BooleanField(default=False)
    date_arrived = models.DateTimeField(auto_now_add = True)
    date_completed = models.DateTimeField(blank=True, null=True)
    private = models.BooleanField(default=False)


# Each time a Complaint changes its current agent id this class will have a new entry with a new agent and statuses
class ComplaintTrack(models.Model):
    complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Agent, to_field='employee_id', on_delete=models.CASCADE)
    status_on_arrival = models.CharField(max_length=255)
    status_on_departure = models.CharField(max_length=255, blank=True)
    date_arrived = models.DateTimeField(auto_now_add = True)
    date_completed = models.DateTimeField(blank=True, null=True)


class Request(models.Model):
    citizen_id = models.ForeignKey(Citizen, to_field='citizen_id', on_delete=models.CASCADE)
    current_agent_id = models.ForeignKey(Agent, to_field='employee_id', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=2047, blank=True)
    picture = models.URLField(max_length=16000, blank=True)
    details = models.CharField(max_length=16000, blank=True)
    status = models.CharField(max_length=2047, default='Just Arrived')
    is_completed = models.BooleanField(default=False)
    date_arrived = models.DateTimeField(auto_now_add = True)
    date_completed = models.DateTimeField(blank=True, null=True)


# Each time a Request changes its current agent id this class will have a new entry with a new agent and statuses
class RequestTrack(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Agent, to_field='employee_id', on_delete=models.CASCADE)
    status_on_arrival = models.CharField(max_length=255)
    status_on_departure = models.CharField(max_length=255, blank=True)
    date_arrived = models.DateTimeField(auto_now_add = True)
    date_completed = models.DateTimeField(blank=True, null=True)


class Post(models.Model):
    picture = models.URLField(max_length=16000, blank=True)
    text = models.CharField(max_length=16000, blank=True)
    category = models.CharField(max_length=2047)
