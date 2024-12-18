from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name','hotel_description','city', 'address',)


@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = ('room_description',)

