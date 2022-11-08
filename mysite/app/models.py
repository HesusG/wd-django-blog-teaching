from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def blogDetail(request, pk):
    context = {}
    context['article'] = Blog.objects.get(id=pk)
    return render(request, 'blog-detail.html', context)

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    message = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

class Portfolio(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/portfolio/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name