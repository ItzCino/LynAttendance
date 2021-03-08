#######################################################################
#####VALID COOKIES MUST BE USED OTHER WISE WILL ERROR OUT OR CRASH#####
###########IF THE PROGRAM ERRORS THEN A NEW KEY IS NEEDED##############
#######################################################################

#CURL BASH TO PYTHON COOKIES
# https://curl.trillworks.com/

import ConvertCurlBashToPythonCookie
import attendance
import requests
from bs4 import BeautifulSoup

#Insert cookie header below;

# =============================================================
# =============================================================

cookie = """
#Insert cookie header below;



#Insert Cookie header above
"""

# =============================================================
# =============================================================

#Insert Cookie header above

#Value for up for STARTING WEEK (default = 1)
startingWeek = 1
#Value for up for FINISHING WEEK (default value should be the last week)
finishingWeek = 5

headers = ConvertCurlBashToPythonCookie.CurlBashToPythonCookie(cookie)

#headers = {'csrf_kamar_cn': 'bd2a714b48693186332fd8b67372a776', 'kamar_session': '9n50i4hu17vs8bqb4di0al63o8u6pmvq'}

#Initalises and sets values to 0
#total FINAL values for FORM periods and TOTAL Periods
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

#temporory values which are constantly updated and refreshed in function
formPresent = 0
formAbsent = 0
formJustified = 0
formLate = 0
totalFormPeriod = 0
totalPeriods = 0
totalPresents = 0
totalAbsents = 0
totalJustified = 0
totalLates = 0

#Sets default attendance URL
parentPortalURL = 'https://lynfield.mystudent.school.nz/attendance/'
parentPortalURLList = list(parentPortalURL)

#Requests for attendance data for each URL page by 1 integer increments (by 1 week increments)
for number in range(startingWeek, (finishingWeek + 1)):
    parentPortalURLList = list(parentPortalURL)
    #print(parentPortalURLList)
    parentPortalURLList.append(str(number))
    URL = (''.join(parentPortalURLList))
    #print(URL)
    response = requests.get(URL, headers=headers)
    try:
        formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = attendance.attendances(response)
        
    except TypeError:
        print("Invalid Cookies or URLS")
        print("\nStopped on week {}".format(number))
    #Adds attendance data to the SUM of that variable
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
    
    print("""
    Week:   FormPresents    FormAbsents     FormAttendanceRate:    AllPresents:    AllAbsents:   AttendanceRate:
    {}{:8}{:16}{:15}{:4.2f}%{:19}{:15}{:13}{:4.2f}% """ 
    .format(number, formPresent, formAbsent, "", (((formPresent + formLate + formJustified) / totalFormPeriod) * 100), 
    totalPresents, totalAbsents, "", (((totalPresents +  totalLates + totalJustified) / totalPeriods) * 100) )
    )



#soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

#Calculates the attendance rate for both FORM periods and ALL periods 
formPeriodAttendanceRate = ((sumFormPresent + sumFormJustified + sumFormLate) / sumTotalFormPeriod) * 100
allPeriodAttendanceRate = ((sumTotalPresents + sumTotalJustified + sumTotalLates) / sumTotalPeriods) * 100

#Prints out final attendance data formatted.

print("\n\nTotal Form Periods: \n")
print("Total form periods: %s" % sumTotalFormPeriod)
print("Total form periods present (including late periods) : %s" % (sumFormPresent + sumFormLate))
print("Total periods late: %s" % sumFormLate)
print("Total form periods absent: %s" % sumFormAbsent)
print("Total form justified absents: %s" % sumFormJustified)
print("Form period Attendance Rate (includes late and justified form periods) : {:4.2f}%".format(formPeriodAttendanceRate)) 

print("\n\nTotal Period Attendance:\n ")
print("Total periods: %s" % sumTotalPeriods)
print("Total periods present (including late periods) : %s" % (sumTotalPresents+ sumTotalLates))
print("Total periods late: %s" % sumTotalLates)
print("Total periods absent: %s" % sumTotalAbsents)
print("Total justified absents: %s" % sumTotalJustified)
print("All period Attendance Rate (includes late and justified periods) : {:4.2f}%".format(allPeriodAttendanceRate) )
