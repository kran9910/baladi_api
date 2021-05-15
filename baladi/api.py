from rest_framework import routers
from api import views

router = routers.DefaultRouter()
#router.register(r'citizens', views.CitizenViewset)
#router.register(r'agents', views.AgentViewset)
router.register(r'complaints', views.ComplaintViewset)
router.register(r'complaintstrack', views.ComplaintTrackViewset)
router.register(r'requests', views.RequestViewset)
router.register(r'requeststrack', views.RequestTrackViewset)
router.register(r'proposals', views.ProposalViewset)
router.register(r'posts', views.PostViewset)
