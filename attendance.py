#Attendance WOO!

from bs4 import BeautifulSoup


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
        if trElemCounter < 4:
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
            totalFormPeriodCounter = (len(present_elem) + len(absent_elem) + len(justified_elem) + len(late_elem))
            return (formPresentCounter, formAbsentCounter, formJustifiedCounter, formLateCounter, totalFormPeriodCounter)
            break

    


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


page = open("htmls/attendance_4.html","r")
page = page.read()
soup = BeautifulSoup(page, "html.parser")

#for formPeriodAttendance(), returns the form period attendances
findsAllTr = soup.find_all('tr')
formPresent, formAbsent, formJustified, formLate, totalFormPeriod = formPeriodAttendance(findsAllTr)

#for allPeriodAttendance, returns the all period attendances
allPeriods = soup.find_all("td")
totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = allPeriodAttendance(allPeriods)

formPeriodAttendanceRate = ((formPresent + formJustified + formLate) / totalFormPeriod) * 100
allPeriodAttendanceRate = ((totalPresents + totalJustified + totalLates) / totalPeriods) * 100

print("\nTotal Form Periods: \n")
print("Total form periods: %s" % totalFormPeriod)
print("Total form periods present (including late periods) : %s" % (formPresent + formLate))
print("Total periods late: %s" % formLate)
print("Total form periods absent: %s" % formAbsent)
print("Total form justified absents: %s" % formJustified)
print("Form period Attendance Rate (includes late and justified form periods) : {:4.2f}%".format(formPeriodAttendanceRate)) 
print("\n" *2)
print("Total Period Attendance:\n ")
print("Total periods: %s" % totalPeriods)
print("Total periods present (including late periods) : %s" % (totalPresents+ totalLates))
print("Total periods late: %s" % totalLates)
print("Total periods absent: %s" % totalAbsents)
print("Total justified absents: %s" % totalJustified)
print("All period Attendance Rate (includes late and justified periods) : {:4.2f}%".format(allPeriodAttendanceRate) )

