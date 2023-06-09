from django.db import models



class Teachers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='teacher-image',null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    telegram_link = models.CharField(max_length=255,null=True,blank=True)
    instagram_link = models.CharField(max_length=255,null=True,blank=True)
    facebook_link = models.CharField(max_length=255,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = 'Teacher'


class About(models.Model):
    image = models.ImageField(upload_to='about-image',null=True,blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='news-image',null=True,blank=True)
    video = models.FileField(upload_to='news-video',null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'News'



class Gallary(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    maktab = models.BooleanField(default=False)
    dars = models.BooleanField(default=False)
    bayram = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Gallary'
