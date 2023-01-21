"""
app py for project module
"""
from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    """
    project config
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "projects"
