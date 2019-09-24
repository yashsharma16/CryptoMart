from django.shortcuts import render

# Create your views here.

def home(request):
	import requests
	import json

	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,EOS,BCH,LINK,TRX,ETC,BNB,OKB,ADA,XLM,SALT,MOF,BSV,BTT,HT,HBAR,KCS,NEO,USDT,XMR,ONT,MSDT,USDC,TRUE,PAX,AROM,SNM,YOU,STC,LAMB,ZRX,ZEC,WAVES,RCN,DASHXTZ,TUSD,WINT,IOST,MANA,QTUM,MANTIC,ALGO,MTL,CTXC,OGSP,CELR&tsyms=USD,EUR")
	price = json.loads(price_request.content)

	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request,'home.html',{'api':api,'price':price})

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request,'prices.html',{'quote':quote,'crypto':crypto})
	
	else:
		empty = "Enter Any Crypto Currency" 
		return render(request,'prices.html',{'empty':empty})