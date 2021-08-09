from django.urls import include, path

from restapi import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.GetListPosts.as_view()),
    path('<str:q>', views.SearchPost.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]