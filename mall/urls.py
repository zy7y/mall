from apps.areas.urls import urlpatterns as ares
from apps.user.urls import urlpatterns as user

urlpatterns = [*user, *ares]
