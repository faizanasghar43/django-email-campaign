from django.urls import path
from .views import CampaignView, CampaignDetailView, CampaignSchedulerView

urlpatterns = [
    path('create/', CampaignView.as_view(), name='add-items'),
    path('all/', CampaignView.as_view(), name='view-items'),
    path('single/<int:pk>/', CampaignDetailView.as_view(), name='view-one'),
    path('update/<int:pk>/', CampaignDetailView.as_view(), name='update-items'),
    path('delete/<int:pk>/', CampaignDetailView.as_view(), name='delete-items'),
    path('schedule-campaigns/<int:campaign_id>/', CampaignSchedulerView.as_view()),
]
