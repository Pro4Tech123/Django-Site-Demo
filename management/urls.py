from django.urls import path

from . import views

urlpatterns = [

		path('register/', views.registerPage, name='register'),
		path('login/', views.loginPage, name='login'),
		path('logout/', views.logoutUser, name='logout'),

	path('', views.home, name = 'home'),
	path('about/', views.about, name = 'about'),
	path('menu/', views.menu, name = 'menu'),
	path('contact/', views.contact, name = 'contact'),
	path('blog/', views.blog, name = 'blog'),
	path('reservation/', views.reservation, name = 'reservation'),

	path('checkout/<int:pk>', views.checkout, name = 'checkout'),
	path('complete/', views.paymentcomplete, name = 'complete'),

]