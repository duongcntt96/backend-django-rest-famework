from django.urls import include, path

from restapi import views

from rest_framework.routers import DefaultRouter

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = DefaultRouter()

router.register("listpost",views.ListPostSet)


urlpatterns = [
    path('', views.GetListPosts.as_view()),
    path('d', include(router.urls)),
    path('<str:q>', views.SearchPost.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]