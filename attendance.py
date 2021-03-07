#Attendance WOO!

from bs4 import BeautifulSoup

page = open("htmls/attendance_4.html","r")
page = page.read()

soup = BeautifulSoup(page, "html.parser")

#print(soup)

#days = soup.find_all("table", class_="table table-bordered")
days = soup.find_all("td")
#print(days)
findsAllTr = soup.find_all('tr')
#print(len(findsAllTR))


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
    print(trElemCounter)
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
        break

print("Total form periods: %s" % totalFormPeriodCounter)
print("Total form periods present (including late periods) : %s" % (formPresentCounter + formLateCounter))
print("Total form periods absent: %s" % formAbsentCounter)
print("Total form justified absents: %s" % formJustifiedCounter)


#Initalises and Sets all period counters to 0
totalPeriodCounter = 0
presentCounter = 0
absentCounter = 0
justifiedCounter = 0
dayOff = 0

attenList = []


#Checks for presents, absents, and justified absents.
for chunck in days:
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
        presentCounter +=1

    elif absent_elem != None:
        absentCounter += 1
        #continue
    
    elif justified_elem != None:
        justifiedCounter += 1
        #continue
    
    else:
        continue

    #attenList.append(present_elem)
    

    totalPeriodCounter+=1


print(*attenList)
print("Total periods: %s" % totalPeriodCounter)
print("Total periods present (including late periods) : %s" % presentCounter)
print("Total periods absent: %s" % absentCounter)
print("Total justified absents: %s" % justifiedCounter)
print("Total Periods Off: %s" % dayOff)


#:return totalPeriodcounter, presentCounter, absentCounter, justifiedCounter, daysOff



