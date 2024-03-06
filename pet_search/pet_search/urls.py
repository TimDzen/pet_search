from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pet.views import all_animal, animal_detail , home, about


from pet.views import Add_animal, RegisterUser,LoginUser,custom_logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', all_animal, name='all_animal'),
    path('animal/<int:animal_id>/', animal_detail),
    path('add_animal/', Add_animal.as_view(), name='add_animal'),
    path('', home, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name = 'about'),
    path('logout/', custom_logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]

admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Поиск домашних животных'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)