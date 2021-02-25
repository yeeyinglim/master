from django.db import models
from movies.models import Movie
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'