from rest_framework import routers
from .views import *
from django.urls import path, include


router=routers.SimpleRouter()
router.register(r'rating', ReviewViewSet, basename='rating' )
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('urls/',include(router.urls)),
    path('', HotelListAPIView.as_view(), name='hotel_list'),
    path('<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('rooms/create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('rooms/create/<int:pk>/', RoomEDITAPIView.as_view(), name='room_edit'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('hotel/create/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('hotel/create/<int:pk>/', HotelEDITAPIView.as_view(), name='hotel_edit'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]


