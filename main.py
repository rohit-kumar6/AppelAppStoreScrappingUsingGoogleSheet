import gspread
import rpa as r
from urllib.parse import urlparse
import requests
import re

gc = gspread.service_account(filename="cred.json")
sh = gc.open_by_key("1Y3uWi0aCC88tIB-MoQ9oR3xTPsPZl3ZGWHrL5ya2R4U")
worksheet = sh.sheet1
r.init()

rowCount = worksheet.row_count
for row in range(2, rowCount + 1):
    r.url(worksheet.cell(row, 2).value)
    if r.exist("//span[contains(text(),'App Store')]"):
        if r.exist("(//a[text()='Developer Website'])[1]/@href"):
            devWebsite = r.read("(//a[text()='Developer Website'])[1]/@href")
            worksheet.update_cell(row, 3, urlparse(devWebsite).netloc)

        if r.exist("(//a[text()='Privacy Policy'])[1]/@href"):
            privacyPolicyWebsite = r.read("(//a[text()='Privacy Policy'])[1]/@href")
            worksheet.update_cell(row, 4, urlparse(privacyPolicyWebsite).netloc)
            emails = set()
            r.url(privacyPolicyWebsite)
            innerText = r.dom("return document.body.innerText")
            new_emails = set(re.findall(r"([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)",
                                        innerText, re.I))  # re.I: (ignore case)
            emails.update(new_emails)
            worksheet.update_cell(row, 5, ",".join(emails))

            # try:
            #
            #
            #     response = requests.get(privacyPolicyWebsite, timeout=60)
            #     new_emails = set(re.findall(r"([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)",
            #                                 response.text, re.I))  # re.I: (ignore case)
            #     emails.update(new_emails)
            #     worksheet.update_cell(row, 5, ",".join(emails))
            # except Exception as e:
            #     # ignore pages with errors and continue with next url
            #     continue

    if row == 500:
        break

r.close()
