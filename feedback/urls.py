from django.urls import path
from django.views.generic import TemplateView

from .views import FeedbackView

urlpatterns = [
    path(
        'success/',
        TemplateView.as_view(template_name='feedback_success.html'),
        name='feedback_success',
    ),
    path('<str:alias>/', FeedbackView.as_view(), name='feedback'),
]
