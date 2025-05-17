from django.urls import path
from .views.contactus import contactus
from .views.homepage import firsthomepage
from .views.aboutus import aboutus
from .views.review import review
from Shopping.middlewares.auth import auth_middleware

urlpatterns = [
    path('', firsthomepage, name='homepage'),
    path('aboutus', aboutus, name='aboutus'),
    path('contactus', contactus.as_view(), name='contactus'),
    path('review', auth_middleware(review.as_view()), name='review')
]
