from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.views import *
from baladi.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csrf_cookie', GetCSRFToken.as_view()),
    path('authenticated', CheckAuthView.as_view()),
    path('register_citizen', CitizenSignupView.as_view()),
    path('register_agent', AgentSignupView.as_view()),
    path('citizen_profile', GetCitizenProfileView.as_view()),
    path('agent_profile', GetAgentProfileView.as_view()),
    path('update_citizen_profile', UpdateCitizenProfileView.as_view()),
    path('update_agent_profile', UpdateAgentProfileView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('api/app/', include(router.urls)),
]

