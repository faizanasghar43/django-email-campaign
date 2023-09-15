from django.urls import path
from email_scrapping.views import ScrappyAPIView


urlpatterns = [
    path('scrape/', ScrappyAPIView.as_view(), name='scrappy-list'),
    path('scrappy/<int:pk>/', ScrappyAPIView.as_view(), name='scrappy-detail'),
]
