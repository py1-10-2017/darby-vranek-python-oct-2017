from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.form_app.urls'))
]
