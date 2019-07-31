from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^accounts/profile',views.home,name='home'),
    url(r'^profile/(\d+)$', views.profile, name='profile'),
    url(r'^profile/update/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^project/(\d+)$', views.single_project, name='project'),
    url(r'^rating/(\d+)$', views.review_rating, name="review"),
    url(r'^new/(\d+)$', views.new_project, name="new_project"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
