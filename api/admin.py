from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Agent)
admin.site.register(Complaint)
admin.site.register(ComplaintTrack)
admin.site.register(Request)
admin.site.register(RequestTrack)
admin.site.register(Post)
