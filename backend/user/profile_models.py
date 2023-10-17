"""
Profile model module
"""
import os
import hashlib
from django.db import models
from library.models import BaseModel
from location.models import City, State, Country
from configuration.models import Level, Degree, Language as BaseLanguage
from configuration.models import Skill as BaseSkill, Category
from .user_models import Party


# pylint: disable=too-many-ancestors
class Profile(models.Model):
    """
    Profile endpoint Model
    """

    def hash_upload(instance, filename):
        """
        HashUpload
        delete old avatar if exists
        """
        this = Profile.objects.get(party=instance.party)
        try:
            this.avatar.delete()
        except:
            pass
        fname, ext = os.path.splitext(filename)
        return f"avatar/{0}{1}".format(
            hashlib.md5(fname.encode("utf-8")).hexdigest(), ext
        )

    party = models.OneToOneField(
        Party,
        primary_key=True,
        related_name="party_profile",
        unique=True,
        on_delete=models.CASCADE,
    )
    date_birth = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False
    )
    avatar = models.ImageField(upload_to=hash_upload, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    about_me = models.TextField(default="", null=True, blank=True)
    GENDER_CHOICES = [
        ("f", "Female"),
        ("m", "Male"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="m", null=True, blank=True
    )
    MARITAL_CHOICES = [
        ("y", "Yes"),
        ("n", "No"),
    ]
    marital = models.CharField(
        max_length=1, choices=MARITAL_CHOICES, default="m", null=True, blank=True
    )
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    panel = models.IntegerField(default=0, null=True, blank=True)
    panel_timeout = models.DateTimeField(
        null=True, blank=True, auto_now=False, auto_now_add=False
    )
    active = models.BooleanField(default=False)
    news = models.BooleanField(default=False)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    is_employer = models.BooleanField(default=False)
    company_name = models.CharField(default="", max_length=250, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (
            self.party.user.first_name
            + " "
            + self.party.user.last_name
            + "-"
            + self.party.user.mobile
            + " "
        )


class Contact(BaseModel):
    """
    Contacte endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_contact"
    )
    CONTACT_TYPE_CHOICES = [
        ("p", "Phone"),
        ("m", "Mobile"),
        ("a", "Address"),
    ]
    contact_type = models.CharField(
        max_length=1, choices=CONTACT_TYPE_CHOICES, default="a", null=True, blank=True
    )
    contact = models.TextField()


class Skill(BaseModel):
    """
    Skill endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_skill"
    )
    skill = models.ForeignKey(BaseSkill, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "party",
            "skill",
        )


class Job(BaseModel):
    """
    Jobs endpoint Model
    """

    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="party_job")
    title = models.TextField()
    company = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Education(BaseModel):
    """
    Education endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_education"
    )
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    uni_name = models.TextField(default="")
    major = models.TextField(default="")
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )

    class Meta:
        unique_together = (
            "party",
            "degree",
        )


class Certificate(BaseModel):
    """
    Certificate endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_certificate"
    )
    name = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Specialty(BaseModel):
    """
    specialty endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_speciality"
    )
    name = models.TextField()
    level = models.TextField()
    description = models.TextField()
    Institution_name = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Achievement(BaseModel):
    """
    Achivment endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_achievement"
    )
    title = models.TextField()
    event = models.TextField()
    description = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Language(BaseModel):
    """
    Language endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_language"
    )
    language = models.ForeignKey(BaseLanguage, on_delete=models.CASCADE)
    talking = models.IntegerField(default=0, null=True, blank=True)
    writing = models.IntegerField(default=0, null=True, blank=True)
    comprehension = models.IntegerField(default=0, null=True, blank=True)


class WorkSample(BaseModel):
    """
    WorkSample endpoint Model
    """

    def hash_upload(self, instance, filename):
        """
        Upload Hash  endpoint Model
        """
        # delete old avatar if exists
        this = WorkSample.objects.get(party=instance.party)
        try:
            this.avatar.delete()  # type: ignore
        except:
            pass
        fname, ext = os.path.splitext(filename)
        return f"worksample/{0}{1}".format(
            hashlib.md5(fname.encode("utf-8")).hexdigest(), ext
        )

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_worksample"
    )
    title = models.TextField()
    skill = models.OneToOneField(BaseSkill, unique=True, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=hash_upload, null=True, blank=True)


class Experience(BaseModel):
    """
    Experience endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_experience"
    )
    title = models.TextField()
    description = models.TextField()
    place = models.CharField(default="", max_length=255)
    date_start = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    date_end = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )


class SocialMedia(BaseModel):
    """
    SocialMedia endpoint Model
    """

    party = models.ForeignKey(
        Party, on_delete=models.CASCADE, related_name="party_socialmedia"
    )
    name = models.TextField()
    userid = models.TextField()
    phone = models.TextField()
    link = models.TextField()
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)


class Vote(BaseModel):
    """
    Vote endpoint Model
    """

    party = models.OneToOneField(
        Party, related_name="vote_party", unique=True, on_delete=models.CASCADE
    )
    owner = models.OneToOneField(
        Party, related_name="vote_owner", unique=True, on_delete=models.CASCADE
    )
    vote = models.IntegerField(default=0, null=True, blank=True)
    opinion = models.TextField(default="", null=True, blank=True)


class ProfilePermissions(BaseModel):
    """
    User only allow this permission to add projects
    """

    party = models.ForeignKey(
        Party, related_name="party_permission", unique=False, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name="category_permission",
        unique=False,
        on_delete=models.CASCADE,
    )
