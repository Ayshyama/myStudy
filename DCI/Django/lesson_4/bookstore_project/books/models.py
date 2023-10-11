from django.db import models


class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=100, null=True)


    class Meta:
        abstract = True


class Author(CommonInfo, models.Model):
    zip_code = models.IntegerField(null=True)
    join_date = models.DateField()
    popularity_score = models.IntegerField()

    # Create a `followers` field in the `Author` model that is a Many to Many Relationship with `User`
    followers = models.ManyToManyField('User', related_name='authors')


class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    published_date = models.DateField()

    # Create a `author` field in the `Books` model that is a One to Many Relationship with `Author`
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    # Create a `publisher` field in the `Books` model that is a One to Many Relationship with `Publisher`
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    # Create a `genre` field in the `Books` model that is a One to Many Relationship with `Genre`
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date', 'price']


class Publisher(CommonInfo, models.Model):
    publisher_name = models.CharField(max_length=200)
    join_date = models.DateField()
    popularity_score = models.IntegerField()


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=150)
