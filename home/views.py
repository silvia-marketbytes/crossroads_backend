from rest_framework import viewsets
from .models import *
from .serializers import *

class HomeBannerViewSet(viewsets.ModelViewSet):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class PopularCoursesViewSet(viewsets.ModelViewSet):
    queryset = PopularCourses.objects.all()
    serializer_class = PopularCoursesSerializer

class CourseListingViewSet(viewsets.ModelViewSet):
    queryset = CourseListing.objects.all()
    serializer_class = CourseListingSerializer

class FreeEducationViewSet(viewsets.ModelViewSet):
    queryset = FreeEducation.objects.all()
    serializer_class = FreeEducationSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class NewsAndEventsOverviewViewSet(viewsets.ModelViewSet):
    queryset = NewsAndEventsOverview.objects.all()
    serializer_class = NewsAndEventsOverviewSerializer

class NewsAndEventsDetailViewSet(viewsets.ModelViewSet):
    queryset = NewsAndEventsDetail.objects.all()
    serializer_class = NewsAndEventsDetailSerializer

class TestimonialOverviewViewSet(viewsets.ModelViewSet):
    queryset = TestimonialOverview.objects.all()
    serializer_class = TestimonialOverviewSerializer

class TestimonialDetailViewSet(viewsets.ModelViewSet):
    queryset = TestimonialDetail.objects.all()
    serializer_class = TestimonialDetailSerializer

class FormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer