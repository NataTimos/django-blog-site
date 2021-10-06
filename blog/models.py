from django.urls import reverse
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-published_date',)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.published_date.year,
                              self.published_date.strftime('%m'),
                              self.published_date.strftime('%d'),
                              self.slug])
    
    def __str__(self):
        return self.title
