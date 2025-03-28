from django.db import models

class HomeBanner(models.Model):
    image = models.ImageField(upload_to='home-banner/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    apply_now_url = models.URLField(max_length=200, null=True, blank=True) 
    contact_us_url = models.URLField(max_length=200, null=True, blank=True)  
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title or "Untitled Banner"

    class Meta:
        ordering = ['order']

class Service(models.Model):
    image =  models.ImageField(upload_to='service-banner/', null=True,blank=True)
    title=models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    order = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class About(models.Model):
    title=models.CharField(max_length=255, null=True, blank=True)
    subtitle=models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    read_more = models.URLField(null=True, blank=True, verbose_name="Read More Link")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class PopularCourses(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    tab_name = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['order']

class CourseListing(models.Model):
    popular_course = models.ForeignKey(PopularCourses, related_name='listings', on_delete=models.CASCADE )
    title = models.CharField(max_length=255,null=True, blank=True )
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    link_button = models.URLField(null=True, blank=True, verbose_name="More Details Link") 
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['order']

class FreeEducation(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    country_image = models.ImageField(upload_to='free_education/', null=True, blank=True)
    country_name = models.CharField(max_length=255,null=True, blank=True)
    order = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.title} - {self.country_name}"
    class Meta:
        ordering = ['order']


class Slider(models.Model):
    image =  models.ImageField(upload_to='service-banner/', null=True,blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    read_more = models.URLField(null=True, blank=True, verbose_name="Read More Link")
    order = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.title} - {self.country_name}"
    class Meta:
        ordering = ['order']

class NewsAndEventsOverview(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title

class NewsAndEventsDetail(models.Model):
    news_and_events_overview = models.ForeignKey(NewsAndEventsOverview, related_name='details', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_events/', null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    link = models.URLField(null=True, blank=True, verbose_name="Details Link")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class TestimonialOverview(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class TestimonialDetail(models.Model):
    testimonial_overview = models.ForeignKey(TestimonialOverview, related_name='details', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    rating = models.PositiveIntegerField(default=0,null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    video = models.URLField(null=True, blank=True, verbose_name="Video URL")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class FormSubmission(models.Model):
    HELP_CHOICES = (
        ('education', 'Education'),
        ('job_assistance', 'Job Assistance'),
        ('migration', 'Migration'),
    )
    name = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    help_type = models.CharField(max_length=20, choices=HELP_CHOICES,null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['order']


