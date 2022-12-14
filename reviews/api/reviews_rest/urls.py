from django.urls import path
from .views import (
    api_list_reviews,
    api_show_review,
    api_list_movies,
    api_list_reviews_by_imdb_id,
    api_list_accountVOs,
)

urlpatterns = [
    path(
        "users/",
        api_list_accountVOs,
        name="list_users",
    ),
    path(
        "movies/",
        api_list_movies,
        name="create_movie",
    ),
    path(
        "movies/<str:imdb_id>/",
        api_list_movies,
        name="list_movies",
    ),
    path(
        "reviews/<str:imdb_id>/",
        api_list_reviews_by_imdb_id,
        name="list_reviews",
    ),
    path(
        "create/review/",
        api_list_reviews,
        name="create_review",
    ),
    path(
        "reviews/edit/<int:pk>/",
        api_show_review,
        name="edit_review",
    ),
    path(
        "reviews/delete/<int:pk>/",
        api_show_review,
        name="delete_review",
    ),
]
