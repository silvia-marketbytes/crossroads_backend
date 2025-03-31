from rest_framework import serializers
from .models import *

class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class CourseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseListing
        fields = '__all__'

class PopularCoursesSerializer(serializers.ModelSerializer):
    listings = CourseListingSerializer(many=True, read_only=True)
    class Meta:
        model = PopularCourses
        fields = '__all__'

class FreeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeEducation
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class NewsAndEventsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndEventsDetail
        fields = '__all__'

class NewsAndEventsOverviewSerializer(serializers.ModelSerializer):
    details = NewsAndEventsDetailSerializer(many=True, read_only=True)
    class Meta:
        model = NewsAndEventsOverview
        fields = '__all__'

class TestimonialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialDetail
        fields = '__all__'

class TestimonialOverviewSerializer(serializers.ModelSerializer):
    details = TestimonialDetailSerializer(many=True, read_only=True)
    class Meta:
        model = TestimonialOverview
        fields = '__all__'

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = '__all__'