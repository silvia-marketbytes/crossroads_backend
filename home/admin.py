from django.contrib import admin
from .models import *

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'apply_now_url', 'contact_us_url', 'order')
    list_editable = ('order',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'order')
    list_editable = ('order',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'description', 'read_more', 'order')
    list_editable = ('order',)

class CourseListingInline(admin.TabularInline):
    model = CourseListing
    extra = 1

@admin.register(PopularCourses)
class PopularCoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'tab_name', 'order')
    list_editable = ('order',)
    inlines = [CourseListingInline]

@admin.register(CourseListing)
class CourseListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'popular_course', 'title', 'subtitle', 'link_button', 'order')
    list_editable = ('order',)

@admin.register(FreeEducation)
class FreeEducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'country_image', 'country_name', 'order')
    list_editable = ('order',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'read_more', 'order')
    list_editable = ('order',)

class NewsAndEventsDetailInline(admin.TabularInline):
    model = NewsAndEventsDetail
    extra = 1

@admin.register(NewsAndEventsOverview)
class NewsAndEventsOverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    inlines = [NewsAndEventsDetailInline]

@admin.register(NewsAndEventsDetail)
class NewsAndEventsDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_and_events_overview', 'image', 'title', 'description', 'link', 'order')
    list_editable = ('order',)

class TestimonialDetailInline(admin.TabularInline):
    model = TestimonialDetail
    extra = 1

@admin.register(TestimonialOverview)
class TestimonialOverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')
    inlines = [TestimonialDetailInline]

@admin.register(TestimonialDetail)
class TestimonialDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'testimonial_overview', 'image', 'title', 'rating', 'description', 'video', 'order')
    list_editable = ('order',)

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'location', 'help_type', 'order')
    list_editable = ('order',)
    list_filter = ('help_type',)