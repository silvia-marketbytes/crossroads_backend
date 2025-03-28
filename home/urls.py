from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'home-banners', views.HomeBannerViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'about', views.AboutViewSet)
router.register(r'popular-courses', views.PopularCoursesViewSet)
router.register(r'course-listings', views.CourseListingViewSet)
router.register(r'free-education', views.FreeEducationViewSet)
router.register(r'sliders', views.SliderViewSet)
router.register(r'news-events-overview', views.NewsAndEventsOverviewViewSet)
router.register(r'news-events-details', views.NewsAndEventsDetailViewSet)
router.register(r'testimonial-overview', views.TestimonialOverviewViewSet)
router.register(r'testimonial-details', views.TestimonialDetailViewSet)
router.register(r'form-submissions', views.FormSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]