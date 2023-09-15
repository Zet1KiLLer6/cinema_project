from applications.movie.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', MovieAPIView)

urlpatterns = []

urlpatterns += router.urls