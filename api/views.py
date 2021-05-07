from django.contrib import auth
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from . import models
from . import serializers
from .models import Citizen, Agent
from .serializers import CitizenSerializer, AgentSerializer


class CitizenViewset(viewsets.ModelViewSet):
    queryset = models.Citizen.objects.all()
    serializer_class = serializers.CitizenSerializer

class AgentViewset(viewsets.ModelViewSet):
    queryset = models.Agent.objects.all()
    serializer_class = serializers.AgentSerializer

class ComplaintViewset(viewsets.ModelViewSet):
    queryset = models.Complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer

class ComplaintTrackViewset(viewsets.ModelViewSet):
    queryset = models.ComplaintTrack.objects.all()
    serializer_class = serializers.ComplaintTrackSerializer

class RequestViewset(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer

class RequestTrackViewset(viewsets.ModelViewSet):
    queryset = models.RequestTrack.objects.all()
    serializer_class = serializers.RequestTrackSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

@method_decorator(csrf_protect, name= 'dispatch')
class CitizenSignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        citizen_id = data['citizen_id']
        phone_number = data['phone_number']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        address = data['address']
        birthdate = data['birthdate']
        profile_pic = data['profile_pic']
        if password == re_password:
            try:
                if User.objects.filter(username = username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error' : 'Password must be at least 6 characters'})
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(username=username)
                        citizen = Citizen(user=user, citizen_id=citizen_id, phone_number=phone_number, first_name=first_name,last_name=last_name,address=address,email=email,profile_pic=profile_pic, birthdate=birthdate)
                        citizen.save()
                        return Response({'success' : 'Citizen Created'})
            except:
                return Response({'error':'Something went wrong when registering account'})

        else:
            return Response({'error' : 'Passwords do not match'})

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self,request, format = None):
        return Response({'success' : 'CSRF Cookie set'})

@method_decorator(csrf_protect, name= 'dispatch')
class CheckAuthView(APIView):
    def get(self,request, format = None):
        try:
            isAuthenticated = User.is_authenticated
            if isAuthenticated:
                return Response({'isAuthenticated':'success'})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':'Something went wrong when checking authentication status'})

@method_decorator(csrf_protect, name= 'dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        try:
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request,user)
                return Response({'success':'User authenticated','username':username})
            else:
                return Response({'error':'Error Authenticating'})
        except:
            return Response({'error':'Something went wrong when Logging In'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success':'Logged Out'})
        except:
            return Response({'error':'Something went wrong when Logging Out'})

class DeleteAccountView(APIView):
    def delete(self, request, format = None):
        try:
            user = self.request.user
            user = User.objects.filter(id = user.id).delete()
            return Response({'success':'User Deleted Successfully'})
        except:
            return Response({'error':'Something went wrong when deleting user'})

class GetCitizenProfileView(APIView):
    def get(self,request, format=None):
        try:
            user = self.request.user
            username = user.username
            user = User.objects.get(id= user.id)
            citizen = Citizen.objects.get(user = user)
            citizen = CitizenSerializer(citizen)
            return Response({'profile':citizen.data, 'username':str(username)})
        except:
            return Response({'error':'Something went wrong while getting profile'})

class UpdateCitizenProfileView(APIView):
    def put(self,request,format = None):
        try:
            user = self.request.user
            username = user.username
            data = self.request.data
            phone_number = data['phone_number']
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            address = data['address']
            birthdate = data['birthdate']
            profile_pic = data['profile_pic']
            user = User.objects.get(id=user.id)
            Citizen.objects.filter(user=user).update(phone_number=phone_number, first_name=first_name,last_name=last_name,address=address,email=email,profile_pic=profile_pic, birthdate=birthdate)
            citizen = Citizen.objects.get(user = user)
            citizen = CitizenSerializer(citizen)
            return Response({'profile':citizen.data, 'username':str(username)})
        except:
            return Response({'error':'Something went wrong while updating profile'})

@method_decorator(csrf_protect, name= 'dispatch')
class AgentSignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        data = self.request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        employee_id = data['employee_id']
        phone_number = data['phone_number']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        role = data['role']
        if password == re_password:
            try:
                if User.objects.filter(username = username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error' : 'Password must be at least 6 characters'})
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(username=username)
                        print(user)
                        agent = Agent(user=user, employee_id=employee_id, phone_number=phone_number, first_name= first_name,last_name=last_name,email=email,role=role)
                        agent.save()
                        return Response({'success' : 'Agent Created'})
            except:
                return Response({'error':'Something went wrong when registering account'})

        else:
            return Response({'error' : 'Passwords do not match'})

class GetAgentProfileView(APIView):
    def get(self,request, format=None):
        try:
            user = self.request.user
            username = user.username
            user = User.objects.get(id= user.id)
            agent = Agent.objects.get(user = user)
            agent = AgentSerializer(agent)
            return Response({'profile': agent.data, 'username': str(username)})
        except:
            return Response({'error':'Something went wrong while getting profile'})

class UpdateAgentProfileView(APIView):
    def put(self,request,format = None):
        try:
            user = self.request.user
            username = user.username
            data = self.request.data
            phone_number = data['phone_number']
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            role = data['role']
            user = User.objects.get(id=user.id)
            Agent.objects.filter(user=user).update(phone_number=phone_number, first_name=first_name,last_name=last_name,role=role,email=email)
            agent = Agent.objects.get(user = user)
            agent = AgentSerializer(agent)
            return Response({'profile':agent.data, 'username':str(username)})
        except:
            return Response({'error':'Something went wrong while updating profile'})

