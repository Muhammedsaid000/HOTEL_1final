from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['username', 'email', 'password', 'first_name','last_name',
                'age','phone_number','user_role',]
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        user=authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh=RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError({'detail': 'Недействительный или уже отозванный токен'})



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['last_name','first_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelImage
        fields=['hotel_image']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_images=RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model=Room
        fields=['id', 'room_number', 'room_type','room_status', 'room_price','room_images']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images=RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model=Room
        fields=['room_number', 'room_type','room_status', 'room_price','all_inclusive','room_images','room_description']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images=HotelImageSerializer(many=True, read_only=True)
    get_avg_rating=serializers.SerializerMethodField()
    country=CountryListSerializer(read_only=True)
    class Meta:
        model=Hotel
        fields = ['id', 'hotel_name', 'hotel_images','country', 'address', 'hotel_stars','get_avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

class ReviewSerializer(serializers.ModelSerializer):
    user_name=UserProfileSimpleSerializer()
    class Meta:
        model = Review
        fields = ['user_name','text', 'stars','parent',]


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images=HotelImageSerializer(many=True, read_only=True)
    owner=UserProfileSimpleSerializer()
    created_date=serializers.DateField(format='%d-%m-%Y')
    rooms=RoomListSerializer(many=True, read_only=True)
    reviews=ReviewSerializer(many=True, read_only=True)
    country=CountryListSerializer(read_only=True)
    get_count_people=serializers.SerializerMethodField()
    class Meta:
        model=Hotel
        fields=['hotel_name', 'hotel_description','hotel_images','country','rooms',
                'city','address', 'hotel_stars','hotel_video','created_date', 'owner','get_count_people', 'reviews',]

    def get_count_people(self, obj):
        return obj.get_count_people


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields='__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    hotel_country = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name','hotel_country']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'