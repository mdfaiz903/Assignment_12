from django . urls import path
from . views import userinfo
urlpatterns = [
    path('std/',userinfo,name='userinfo')
]
