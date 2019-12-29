from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import cart





urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('feedback/', include('feedback.urls')),        
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),  
   
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

