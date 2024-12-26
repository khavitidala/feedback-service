from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from ipware import get_client_ip

from .models import People, PeopleRatingFeedback


class FeedbackView(View):
    template_name = 'feedback.html'

    def get(self, request, alias):
        people = get_object_or_404(People, alias=alias)
        return render(request, self.template_name, {'people': people})

    def post(self, request, alias):
        ip, _ = get_client_ip(request)
        people = get_object_or_404(People, alias=alias)

        # Create feedback
        PeopleRatingFeedback.objects.create(
            people=people,
            amount=request.POST.get('rating'),
            feedback=request.POST.get('feedback'),
            ip_address=ip,
            user_agent=request.META.get('HTTP_USER_AGENT'),
        )

        return redirect('feedback_success')
