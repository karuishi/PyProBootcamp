from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Practice Cooking pot
# url = "https://appbrewery.github.io/instant_pot/"
# Live Site Cooking pot
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# RAM Memory
url = "https://www.amazon.com.br/Kingston-KF432C16BBK2-16-mem%C3%B3rias-aplic%C3%A1vel/dp/B097K2WBL3/ref=sr_1_4?crid=2ILSOXTE5BANN&dib=eyJ2IjoiMSJ9.7s6nudIBJJn6QQSKm81H0VqbdAxaUc44Al2HrZBbQPPm9KDsiZGE0HYtO6RF6sPY2jLzNoXwSCAmp6ggMaP97beyUxtc7bU7uqvHQ5Nl6FhpF2v7mtE6r59gw85PkhH-D0BiDbZaRfAasvMxlk6szKI6AQSI4Yg0MWSJkTcXHJRLoMEcuGgv50EYZkjdnELZNJ17pP-selQ5pjsZft4rPvU__XQBfqo6RqAFWpJM9fMXcRZO5pIUThNDIxsUyTqZ62ztLRBLMkYVL24P9nSdzKsGA19imMz0aXleWxCiTa8.5Udml5NQFogQKF4rio2ve9mGdU23ORoqY0-z83UWhzw&dib_tag=se&keywords=memoria%2Bram%2Bddr4%2B8gb&qid=1773957568&sprefix=mem%2Caps%2C257&sr=8-4&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751&th=1"

# ====================== Add Headers to the Request ===========================

# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

BUY_PRICE = 1500
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
try:
    # Obter o elemento do preço
    # price_element = soup.find(class_="a-offscreen")
    price_element = soup.find(id="apex-pricetopay-accessibility-label")
    
    if price_element is None:
        raise ValueError("Não foi possível encontrar o preço. A Amazon pode ter pedido um CAPTCHA ou alterado a estrutura da página.")      
    price = price_element.get_text()
    
    price_without_currency = price.replace("R$", "").replace("\xa0", "").strip()
    price_without_currency = price_without_currency.replace(".", "").replace(",", ".")
    price_as_float = float(price_without_currency)
    print(f"Preço convertido: {price_as_float}")

    title_element = soup.find(id="productTitle")
    if title_element is None:
        raise ValueError("Não foi possível encontrar o título do produto.")
        
    title = title_element.get_text().strip()
    print(f"Produto: {title}")

    if price_as_float < BUY_PRICE:
        message = f"{title} is on sale for {price}!"
        with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
            connection.starttls()
            result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
            connection.sendmail(
                from_addr=os.environ["EMAIL_ADDRESS"],
                to_addrs=os.environ["EMAIL_ADDRESS"],
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
            
except AttributeError as e:
    print(f"Erro de atributo ao analisar o HTML: {e}")
except ValueError as e:
    print(f"Erro na conversão dos dados: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

