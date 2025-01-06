from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about_page, name='about'),
    path('blog', blog, name='blog'),
    path('portfolio', portfolio, name='portfolio'),
    path('project-details/<int:pk>/', project_details, name='project_details'),
    path('contact-us', contact_us, name='contact-us'),
    path('category', categorysdata, name='category'),
    path('services', services, name='services'),
    # path('upload-project/', project_upload, name='project_upload'),
    path('edit-project/<int:pk>/', edit_project, name='edit_project'),
]
