#Attendance WOO!

from bs4 import BeautifulSoup

def world():
    print("Hello World!")

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
            print("present {}".format(formPresentCounter))
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

def attendances(response):
    soup = BeautifulSoup(response.content, "html.parser")

    #for formPeriodAttendance(), returns the form period attendances
    findsAllTr = soup.find_all('tr')
    formPresent, formAbsent, formJustified, formLate, totalFormPeriod = formPeriodAttendance(findsAllTr)

    #for allPeriodAttendance, returns the all period attendances
    allPeriods = soup.find_all("td")
    totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates = allPeriodAttendance(allPeriods)

    return formPresent, formAbsent, formJustified, formLate, totalFormPeriod, totalPeriods, totalPresents, totalAbsents, totalJustified, totalLates

