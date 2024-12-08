from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import telebot
import requests


TOKEN = '7791370194:AAGDI47pe5gC_YZNuqAGak1jUwSRl-TfW1U'
bot = telebot.TeleBot(TOKEN)


class BitcoinPriceView(View):

     def get(self,request):
         response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
         data = response.json()
         price_btc = data['bpi']['USD']['rate']
         return JsonResponse({'price_Bit':price_btc})


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! برای دریافت قیمت بیت کوین به تتر، دستور/price را وارد کنید.")


@bot.message_handler(commands=['price'])
def send_price(message):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    price_btc = data['bpi']['USD']['rate']

    bot.reply_to(message, f"   قیمت بیت کوین به تتر :  {price_btc} USD")


def main():
     bot.polling(none_stop=True)


if __name__ == '__main__':
     main()
