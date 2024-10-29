from django.core.validators import MinLengthValidator
from django.db import models

from furryFunnies.authors.models import Author


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=(
            MinLengthValidator(5),
        ),
        unique=True,
    )

    image_url = models.URLField(
        help_text="Share your funniest furry photo URL!"
    )

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

