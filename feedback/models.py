from django.db import models


class People(models.Model):
    name = models.CharField(max_length=300)
    alias = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    class Meta:
        db_table = 'people'


class PeopleRatingFeedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    feedback = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'people_rating_feedback'
