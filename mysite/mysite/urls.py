"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ),
    path('/contact', views.contactus,name="contact"),
    
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name="logout"),
    path('checkout/',views.checkout,name="checkout"),
    path('tracker/',views.tracker,name="tracker"),
    path('chatbot/',views.chatbot,name="chatbot"),
    
    path('shirts/', views.render_shirts, name='shirts'),
    path('jeans/', views.render_jeans),
    path('saree/',views.render_saree),
    path('suits/',views.render_suits),
    
    path('wjeans/',views.render_wjeans),
    path('top/',views.render_top),
    path('earrings/',views.render_earrings),
    path('necklace/',views.render_necklace),
    path('about/',views.render_about),
    

    path('products/<int:myid>',views.productview,name="productview"),



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
