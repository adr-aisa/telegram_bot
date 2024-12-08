from django.urls import path
from .views import BitcoinPriceView

urlpatterns=[
    path('hi/',BitcoinPriceView.as_view(), name='bitcoinprice')

]