from django.urls import path
from .views import (
    StudentRegisterView,
    CheckResultsView
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# The configuration for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title = "RESULTS CHECKER API",
        default_version = '2022',
        description = "API FOR CHECKING YOUR RESULTS",
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    path('api/signup/', StudentRegisterView.as_view(), name='student_signup'),
    path('api/checkresults/',CheckResultsView.as_view(),name = "check_results")

]