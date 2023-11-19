from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    class Meta:
        abstract=True

class Service (BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="Service", null=True, blank=True)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.discount is not None:
          
            discounted_price = self.price - (self.price * (self.discount / 100))
            self.price = discounted_price  
        # self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)




class CarouselItem(BaseModel):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    buuton_text = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title
    

class Category(BaseModel):
    title=models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

class contact (BaseModel):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    message=models.TextField()

    class Meta:
        verbose_name=("contact")
        verbose_name_plural=("contacts")

    def __str__(self):
        return self.name
    

class Setting (BaseModel):
    logo=models.ImageField(upload_to="logo",null=True,blank=True)
    phone1=models.CharField(max_length=255)
    phone2=models.CharField(max_length=255)
    email=models.EmailField()
    facebook=models.URLField()
    instagram=models.URLField(null=True,blank=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    bgimg=models.ImageField(upload_to="bgimg",null=True,blank=True)
    location = models.CharField(max_length=200)

class Testimonial(BaseModel):
    name=models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField(upload_to="Testimonial",null=True,blank=True)
    position=models.CharField(max_length=255,null=True,blank=True)
   
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=("Testimonial")
        verbose_name_plural=("Testimonials")

class About(BaseModel):
    title=models.CharField(max_length=255)
    buuton_text = models.CharField(max_length=100)
    link = models.URLField()
    content=models.TextField()
    video = models.URLField()

class Subscriber(BaseModel):
    email=models.EmailField()

    def __str__(self):
        return self.email   