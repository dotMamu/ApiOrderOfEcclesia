from django.urls import path
from .views import *

urlpatterns = [
    path('weapons/', WeaponView.as_view(), name='weapons-list'),
    path('glyph_union/', GlyphUnionView.as_view(), name='glyph_union-list'),
    path('weapons/<str:name>', WeaponDetailView.as_view(), name='weapons-detail'),
    path('glyph_union/<str:name>', GlyphUnionDetailView.as_view(), name='glyph_union-detail'),
    
]