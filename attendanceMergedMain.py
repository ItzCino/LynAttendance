#######################################################################
#####VALID COOKIES MUST BE USED OTHER WISE WILL ERROR OUT OR CRASH#####
###########IF THE PROGRAM ERRORS THEN A NEW KEY IS NEEDED##############
#######################################################################

#CURL BASH TO PYTHON COOKIES
# https://curl.trillworks.com/

import requests
from bs4 import BeautifulSoup

#Value for up for STARTING WEEK (default = 1)
startingWeek = 1
#Value for up for FINISHING WEEK (default value should be the last week)
finishingWeek = 40

#Manual Cookie Inserter for overiding; cookie loop @ line 
#Insert cookie header below;

# =============================================================
# =============================================================

#cookie = """
#Insert cookie header below;



#Insert Cookie header above
#"""

# =============================================================
# =============================================================

#Insert Cookie header above

#Finds all TR elements for FORM PERIOD
def formPeriodAttendance(findsAllTr):
    #Initalises and sets counters for form period attendances to 0
    totalFormPeriodCounter = 0
    formPresentCounter = 0
    formAbsentCounter = 0
    formJustifiedCounter = 0
    formLateCounter = 0

    #Element find for TR element for form period
    trElemCounter = 0
    #print(findsAllTr)
    for trElem in findsAllTr: 
        #print(trElemCounter)
        if trElemCounter < 3:
            trElemCounter += 1
            continue

        present_elem = trElem.find_all("strong", class_="btn btn-sm btn-success print-hide")
        absent_elem = trElem.find_all("strong", class_="btn btn-sm btn-danger print-hide")
        justified_elem = trElem.find_all("strong", class_="btn btn-sm btn-warning print-hide")
        late_elem = trElem.find_all("strong", class_="btn btn-sm btn-info print-hide")
        
        #Used for debugging purposes for no. of groups of tr elements
        #print("="*160)
        #print(trElem)

        if (present_elem or absent_elem or justified_elem or late_elem) is None:
            continue
        else:     
            #print(present_elem, absent_elem, justified_elem, late_elem)        
            #print(trElem)
            formPresentCounter = len(present_elem)
            formAbsentCounter = len(absent_elem)
            formJustifiedCounter = len(justified_elem)
            formLateCounter = len(late_elem)
            #print("present {}".format(formPresentCounter))
            totalFormPeriodCounter = (len(present_elem) + len(absent_elem) + len(justified_elem) + len(late_elem))
            return (formPresentCounter, formAbsentCounter, formJustifiedCounter, formLateCounter, totalFormPeriodCounter)
    

#Finds all periods which have values of period; PRESENT, ABSENT, JUSTIFIED, LATE
def allPeriodAttendance(allPeriods):
    #Initalises and Sets all period counters to 0
    totalPeriodCounter = 0
    presentCounter = 0
    absentCounter = 0
    justifiedCounter = 0
    lateCounter = 0
    attenList = []


    #Checks for presents, absents, and justified absents.
    for chunck in allPeriods:
        present_elem = chunck.find("strong", class_="btn btn-sm btn-success print-hide")
        absent_elem = chunck.find("strong", class_="btn btn-sm btn-danger print-hide")
        justified_elem = chunck.find("strong", class_="btn btn-sm btn-warning print-hide")
        late_elem = chunck.find("strong", class_="btn btn-sm btn-info print-hide")

        if (present_elem or absent_elem or justified_elem or late_elem) is None:
            #dayOff += 1
            continue    

        elif present_elem != None:
            presentCounter += 1
            #continue

        elif late_elem !=None:
            lateCounter += 1

        elif absent_elem != None:
            absentCounter += 1
            #continue
        
        elif justified_elem != None:
            justifiedCounter += 1
            #continue
        
        else:
            continue

        totalPeriodCounter+=1
    
    return (totalPeriodCounter, presentCounter, absentCounter, justifiedCounter, lateCounter)

def attendances(response):
    soup = BeautifulSoup(response.content, "html.parser")

    #for formPeriodAttendance(), returns the form period attendances
    findsAllTr = soup.find_all('tr')
    formPresent, formAbsent, formJustified, formLate, totalFormPeriod = formPeriodAttendance(findsAllTr)

    #for allPeriodAttendance, returns the all period attendances
    allPeriods = soup.find_all("td")
    totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = allPeriodAttendance(allPeriods)
    #print( formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates)

    return formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates


def CurlBashToPythonCookie(curlBash): 
    completedList = []
    completedCookieHeader = {}
    curlBashRemoveH = curlBash.split(r" \
  -H ")
    #print(curlBashRemoveH)
    #curlBashRemoveH = ''.join('curlBashSplit')
    #print(curlBashRemoveH)
    #print(len(curlBashRemoveH))
    #for line in curlBashRemoveH:
    #    print(line)
    curlBashRemoveH.remove(curlBashRemoveH[0])
    lastElem = curlBashRemoveH[-1]
    curlBashRemoveH.remove(curlBashRemoveH[-1])
    lastElem = lastElem.split(r" \
  ")
    lastElem = lastElem[0]
    curlBashRemoveH.append(lastElem)
    for line in curlBashRemoveH:
       # print(line)
        splitLine = line.split(": ")
        splitKey = list(splitLine[0])
        splitKey.remove(splitKey[0])
        splitKey = ("".join(splitKey))
        splitValue = list(splitLine[1])
        splitValue.remove(splitValue[-1])
        splitValue = ("".join(splitValue))
        #print(splitKey,":", splitValue)
        
        completedCookieHeader[splitKey] = splitValue
        
    #print(completedCookieHeader)
    return completedCookieHeader


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

#Session Cookie Loop
print("\nEnter session cookie (instructions on how is in ReadMe.md): ")
print()

cookieList = []
cookieInput = ' '

while cookieInput != "":
    cookieInput = str(input(""))
    if "--compressed" in cookieInput:
        cookieList.append(cookieInput)
        break
    cookieList.append(cookieInput)

cookieStr = ('\n'.join(cookieList))
cookie = str(cookieStr)

#Calls CurlBashToPythonCookie from ConvertCurlBashToPythonCookie.py to convert
#cURL to python dictionary
headers = CurlBashToPythonCookie(cookie)


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
        formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = attendances(response)
        
    except TypeError:
        print()
        print("Invalid Cookies or URLS")
        print("Stopped on week {}".format(number))
        print("Please try again with new cookie!!")
        exit()
    #Adds attendance data to the SUM of that variable
    sumFormPresent += formPresent
    sumFormAbsent += formAbsent
    sumFormJustified += formJustified
    sumFormLate += formLate
    sumTotalFormPeriod += totalFormPeriod

    sumTotalPeriods += totalPeriods
    sumTotalPresents += totalPresents
    sumTotalAbsents += totalAbsents
    sumTotalJustified += totalJustified
    sumTotalLates += totalLates
    
    try:
        formAttendanceRate = (((formPresent + formLate + formJustified) / totalFormPeriod) * 100)
        allAttendanceRate = (((totalPresents +  totalLates + totalJustified) / totalPeriods) * 100)
    except:
        
        #Calculates the attendance rate for both FORM periods and ALL periods 
        formPeriodAttendanceRate = ((sumFormPresent + sumFormJustified + sumFormLate) / sumTotalFormPeriod) * 100
        allPeriodAttendanceRate = ((sumTotalPresents + sumTotalJustified + sumTotalLates) / sumTotalPeriods) * 100
        
        #Prints out final attendance data formatted.
        print()
        print("=======================================================================================================================")
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
        
        print("END")
        exit()
        
    print("=======================================================================================================================")
    print("""Week:   FormPresents    FormAbsents     FormAttendanceRate:    AllPresents:    AllAbsents:   AttendanceRate:
    {}{:8}{:16}{:15}{:4.2f}%{:19}{:15}{:13}{:4.2f}% """ 
    .format(number, formPresent, formAbsent, "", formAttendanceRate, totalPresents, totalAbsents, "", allAttendanceRate ))
