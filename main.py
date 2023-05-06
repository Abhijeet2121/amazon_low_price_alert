from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "kabhi30@gmail.com"
MY_PASSWORD = "nxvdwyrbpdlukqkv"

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8"
}
response = requests.get(url, headers=header)
amazon_web = response.text

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify)
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < 100:
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:New Low Price! \n\n Product price is less than 100. please go and check out the product \n click on below link {url}"
        )