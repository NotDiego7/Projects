import requests

PRODUCT_URL = 'https://www.amazon.com/Sceptre-34-Inch-Ultrawide-DisplayPort-C345B-QUT168/dp/B0BTK1C533/ref=sr_1_5?crid=MVJZ89BZT71W&keywords=sceptre%2Bmonitor&qid=1699907466&sprefix=sceipr%2Caps%2C200&sr=8-5&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": "PHPSESSID=242a10656e1779cac246145de54684aa",
}

response = requests.get(url= PRODUCT_URL, headers= headers)

print(response.content)

# Bot detection issues