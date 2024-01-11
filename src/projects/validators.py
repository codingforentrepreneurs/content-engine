from django.core.exceptions import ValidationError


def validate_project_handle(handle):
    if handle == "create":
        raise ValidationError(f"\"create\" is an invalid handle")