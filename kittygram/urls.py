from django.urls import include, path

from cats.views import ApiCat

urlpatterns = [
   path('cats/', ApiCat.as_view()),
]


