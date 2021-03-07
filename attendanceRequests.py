import attendance
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'lynfield.mystudent.school.nz',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d5dcfa8d93de801286bbc0d54d36c48371614990148; csrf_kamar_cn=b9b41c03c5cf61e3d78e50036e3898d6; kamar_session=d36nsgqk2v2tu6gkr0p7o8hlppjlojhg',
}

dataLoad = {'cookie': '__cfduid=d5dcfa8d93de801286bbc0d54d36c48371614990148; csrf_kamar_cn=b9b41c03c5cf61e3d78e50036e3898d6; kamar_session=d36nsgqk2v2tu6gkr0p7o8hlppjlojhg'}

parentPortalURL = 'https://lynfield.mystudent.school.nz/attendance/'
parentPortalURLList = list(parentPortalURL)
for number in range(1, 6):
    parentPortalURLList = list(parentPortalURL)
    #print(parentPortalURLList)
    parentPortalURLList.append(str(number))
    URL = (''.join(parentPortalURLList))
filename = "htmls/attendance_3.html"
attendance.attendances(filename)

#response = requests.get('https://lynfield.mystudent.school.nz/attendance/1', headers=headers)

#soup = BeautifulSoup(response.content, "html.parser")
#print(soup)
