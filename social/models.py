from django.db import models

class Users(models.Model):  # TODO slash logdata and personal data
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=399)
    registerTime = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    old = models.IntegerField(null=True)
    city = models.CharField(max_length=20, null=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.email} {self.password}'


class Post(models.Model):
    posttext = models.TextField()
    image = models.FileField(null=True)
    post_id = models.IntegerField()
    owner_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.post_id = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.posttext} {self.post_id} {self.owner_id} {self.date}'


class Comments(models.Model):
    commenttext = models.TextField()
    image = models.FileField(null=True)
    comment_id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner_id = models.IntegerField()
    owner_name = models.TextField(null=True)

    def __str__(self):
        return f'{self.commenttext} {self.comment_id} {self.post} {self.owner_id}'
