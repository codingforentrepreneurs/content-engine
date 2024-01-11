import random
import string
from django.utils.text import slugify


def generate_random_string(size=10):
    chars = string.ascii_lowercase + string.digits
    random_chars = [random.choice(chars) for _ in range(0, size)]
    return "".join(random_chars)


def unique_slugify(instance, _slug=None, size=5, slug_field="slug", title_field='title', invalid_slug='create'):
    '''
    celery tasks
    '''

    to_slug_field = getattr(instance, title_field)
    slug = slugify(to_slug_field)
    if _slug is not None:
        slug = slugify(_slug)
    if slug == invalid_slug:
        random_str = generate_random_string(size=size)
        slug = f"{invalid_slug}-{random_str}"
    lookup = {}
    lookup[f"{slug_field}__iexact"] =  slug
    ModelClass = instance.__class__
    qs_exists = ModelClass.objects.filter(**lookup).exists()
    if qs_exists:
        """
        Not unique slug
        generate one
        """
        random_str = generate_random_string(size=size)
        new_slug = slugify(f"{to_slug_field} {random_str}")
        return unique_slugify(instance, _slug=new_slug, size=size, slug_field=slug_field, title_field=title_field)
    return slug