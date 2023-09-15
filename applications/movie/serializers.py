from rest_framework import serializers
from applications.movie.models import Movie, Rating, Like



class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Like
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)

        return post

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["like_count"] = instance.likes.filter(is_like=True).count()

        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += rating.rating

        if rating_result:
            rep["rating"] = rating_result / instance.ratings.all().count()
        else:
            rep["rating"] = 0

        return rep


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ("rating",)