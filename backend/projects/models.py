"""
Project model module
"""
import os
import hashlib
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.db.models.functions import Coalesce
from django.db.models import OuterRef, QuerySet, Subquery, Value
from library.models import BaseModel
from configuration.models import (
    Category,
    Currency,
    Level,
    Skill as BaseSkill,
    Status,
)
from location.models import City, Country, Place, State
from user.user_models import Party

class ProjectManager(models.Manager):
    def get_queryset(self):
        #preload user data to reduce db call
        return super().get_queryset().select_related("party__user")

    def with_owner_stats(self):
        return self.annotate(
            owner_projects=Coalesce(
                Subquery(
                    Project.objects.filter(party=OuterRef("party"))
                    .values("party")
                    .annotate(count=models.Count("party"))
                    .values("count"),
                ),
                Value(0)
            )
        )

class Project(BaseModel):
    """
    Project model
    """
    objects = ProjectManager()

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE, related_name="project_category"
    )
    sub_category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE,
        related_name="project_sub_category",
    )
    work = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    skill = models.ManyToManyField(BaseSkill, related_name="project_skill")
    duration = models.DurationField(default=timedelta)
    description = models.TextField(null=True, blank=True)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_currency",
    )
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    tag = models.TextField(null=True, blank=True)
    cre_price = models.IntegerField(null=True, blank=True)
    budget_total = models.IntegerField(null=True, blank=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    #status = models.ForeignKey(
    #    Status,
    #    on_delete=models.CASCADE,
    #    null=True,
    #    blank=True,
    #    related_name="project_status",
    #)
    STATUS_CHOICES = [
        ("n", "New"),
        ("i", "In Progress"),
        ("c", "Closed"),
    ]
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="n", null=True, blank=True
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_status",
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_place",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_country",
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_city",
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="project_state",
    )
    deleted_date = models.DateTimeField(null=True, blank=True)

    def InProgress(self):
        self.status = 'p'
        self.save()
        return True

    def Close(self):
        self.status = 'c'
        self.save()
        return True

    def __str__(self):
        return self.title



class File(BaseModel):
    """
    Project file model
    """

    def hash_upload(instance, filename):
        """
        Project file model
        """
        fname, ext = os.path.splitext(filename)
        return "project/{0}{1}".format(
            hashlib.md5(fname.encode("utf-8")).hexdigest(), ext
        )

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_file = models.FileField(upload_to=hash_upload, null=True, blank=True)


class Cost(BaseModel):
    """
    Project cost model
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    calculate_cost = models.IntegerField()
    pay_cost = models.IntegerField()
    pay_date = models.DateTimeField()


class Offer(BaseModel):
    """
    Project offer model
    """

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="offers"
    )
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=200)
    duration = models.DurationField(default=timedelta)
    cost = models.IntegerField(default=0)
    description = models.TextField(default="")
    STATE_CHOICES = [
        ("a", "Accept"),
        ("r", "Reject"),
        ("n", "Not Set"),
        ("p", "Paid"),
    ]
    state = models.CharField(
        max_length=1, choices=STATE_CHOICES, default="n", null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            "project",
            "party",
        )

    def __str__(self):
        return self.title


class OfferStep(BaseModel):
    """
    Project offer step model
    """

    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="offersteps",
    )
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200)
    duration = models.DurationField(default=timedelta)
    optional = models.BooleanField(default=False, blank=True, null=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.title


class Budget(BaseModel):
    """
    Project budget model
    """

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="budgets"
    )
    currency = models.ForeignKey(Currency, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.IntegerField()
    optional = models.BooleanField()
    cost = models.IntegerField()

    def __str__(self):
        return self.title
