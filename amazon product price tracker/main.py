import os

import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv()
email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")



response=requests.get(url="https://www.amazon.in/Lenovo-ThinkBook-21MW00ETIN-Fingerprint-Warranty/dp/B0H6XQLM17/?_encoding=UTF8&pd_rd_w=7W8Yv&content-id=amzn1.sym.269451f3-e80e-420c-94ec-ee592d610294%3Aamzn1.symc.9c2bf194-2fbd-4cc2-90ac-eadc11371901&pf_rd_p=269451f3-e80e-420c-94ec-ee592d610294&pf_rd_r=23VRT759J5V2CW7HBPZ6&pd_rd_wg=fpbZl&pd_rd_r=9b5f262d-9cd7-40d3-aa6c-34087beabb43&ref_=pd_hp_d_r_btf_ci_mcx_mr_",headers={"Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 Edg/154.0.0.0", }
)
soup=BeautifulSoup(response.text,"html.parser")
price=soup.find(class_="a-price-whole").get_text()
price=price.replace(".","")
price=price.replace(",","")
price_without_currency=float(price)


with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(email,password)
    if price_without_currency<80000:
        connection.sendmail(from_addr=email,to_addrs="edgeuser194@gmail.com",msg=f"Subject: the product price has been reduced  to{price_without_currency} ")
print("done")