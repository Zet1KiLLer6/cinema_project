from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User  = get_user_model()


class Movie(models.Model):
    """
        Это модель фильмов
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movies", verbose_name="Владелец фильмв"
    )
    title = models.CharField("Название", max_length=70)
    description = models.TextField("Описание", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="likes")
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} liked - {self.movie.title}"

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")

    rating = models.SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], blank=True, null=True)

    def __str__(self):
        return f"{self.owner} --> {self.movie.title}"