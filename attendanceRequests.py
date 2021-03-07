import attendance
import requests
from bs4 import BeautifulSoup

sumFormPresent = 0
sumFormAbsent = 0
sumFormJustified = 0
sumFormLate = 0
sumTotalFormPeriod = 0

sumTotalPeriods = 0
sumTotalPresents = 0
sumTotalAbsents = 0
sumTotalJustified = 0
sumTotalLates = 0


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
for number in range(1, 2):
    parentPortalURLList = list(parentPortalURL)
    #print(parentPortalURLList)
    parentPortalURLList.append(str(number))
    URL = (''.join(parentPortalURLList))
    filename = "htmls/attendance_3.html"
    formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = attendance.attendances(filename)
    sumFormPresent += formPresent
    sumFormAbsent += formAbsent
    sumFormJustified += formJustified
    sumFormLate =+ formLate
    sumTotalFormPeriod += totalFormPeriod

    sumTotalPeriods += totalPeriods
    sumTotalPresents += totalPresents
    sumTotalAbsents += totalAbsents
    sumTotalJustified += totalJustified
    sumTotalLates += totalLates

#response = requests.get('https://lynfield.mystudent.school.nz/attendance/1', headers=headers)

#soup = BeautifulSoup(response.content, "html.parser")
#print(soup)
formPeriodAttendanceRate = ((sumFormPresent + sumFormJustified + sumFormLate) / sumTotalFormPeriod) * 100
allPeriodAttendanceRate = ((sumTotalPresents + sumTotalJustified + sumTotalLates) / sumTotalPeriods) * 100

print("\nTotal Form Periods: \n")
print("Total form periods: %s" % sumTotalFormPeriod)
print("Total form periods present (including late periods) : %s" % (sumFormPresent + sumFormLate))
print("Total periods late: %s" % sumFormLate)
print("Total form periods absent: %s" % sumFormAbsent)
print("Total form justified absents: %s" % sumFormJustified)
print("Form period Attendance Rate (includes late and justified form periods) : {:4.2f}%".format(formPeriodAttendanceRate)) 
print("\n" *2)
print("Total Period Attendance:\n ")
print("Total periods: %s" % sumTotalPeriods)
print("Total periods present (including late periods) : %s" % (sumTotalPresents+ sumTotalLates))
print("Total periods late: %s" % sumTotalLates)
print("Total periods absent: %s" % sumTotalAbsents)
print("Total justified absents: %s" % sumTotalJustified)
print("All period Attendance Rate (includes late and justified periods) : {:4.2f}%".format(allPeriodAttendanceRate) )
