from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Don't create table in DB


class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]  # Category.objects.all() => order_by("name")
        verbose_name = "category"
        verbose_name_plural = "Categories"  # Add this line


class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the Tag, which is its name.
        """
        return self.name


# post.tag.all
# post.
class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)
    is_breaking_news = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Advertisement(TimeStampModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advertisements/%Y/%m/%d", blank=False)

    def __str__(self):
        return self.title


class OurTeam(TimeStampModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="our_teams/%Y/%m/%d", blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]  #Contact.objects.all() => order_by("created_at")
# Post - User
# 1 user can add M posts => M
# 1 post is associated to only 1 => 1
# ForeignKey => M => Post


# Post - Category
# 1 category can have M posts => M
# 1 post is associated to only 1 category => 1
# ForeignKey => M => Post

# Post - Tag
# 1 tag can have M posts => M
# 1 post can have M tags => M
# ManyToManyField => M => Any => Post