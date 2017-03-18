from django.conf.urls import url
from .views import BankAccountDataRetrieveAPIView
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^ab/(?P<account_id>\d+)/$', BankAccountDataRetrieveAPIView.as_view(), name='ABankRet'),
]
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]