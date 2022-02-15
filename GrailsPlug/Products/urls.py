from django.urls import URLPattern, path, include
from Products import views
urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view())
]