"""Shop URL Configuration

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
from rest_framework.authtoken.views import obtain_auth_token
from main.views import ProductView
from main.views import CategoryView
from main.views import LoginView
from main.views import SignupView
from main.views import StaffView
from main.views import VendorView
from main.views import comment_view
from main.views import like_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view(), name="products"),
    path('products/<int:product_id>/likes', like_view),
    path('products/<int:product_id>/likes/<int:like_id>', like_view),
    path('category/', CategoryView.as_view(), name="categories"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('comment/<int:product_id>', comment_view, name="comment"),
    path('comment/<int:product_id>/<int:comment_id>', comment_view, name="comment"),
    path('vendor/', VendorView.as_view(), name="vendor"),
    path('vendor/<int:id>', VendorView.as_view()),
    path('staff/', StaffView.as_view()),
    path('staff/<int:staff_id>', StaffView.as_view())
]
