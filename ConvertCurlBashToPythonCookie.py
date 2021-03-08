#CONVERTS CURL BASH TO PYTHON COOKIE
#Program returns dictionary from CURL BASH commands

def CurlBashToPythonCookie(curlBash): 
    completedList = []
    completedCookieHeader = {}
    curlBashRemoveH = curlBash.split(" \
  -H ")
    #print(len(curlBash))
    #for line in curlBash:
    #    print(line)
    curlBashRemoveH.remove(curlBashRemoveH[0])
    lastElem = curlBashRemoveH[-1]
    curlBashRemoveH.remove(curlBashRemoveH[-1])
    lastElem = lastElem.split("   ")
    lastElem = lastElem[0]
    curlBashRemoveH.append(lastElem)
    for line in curlBashRemoveH:
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
    return ( completedCookieHeader)
    
#Testing purposes: uncomment the function caller at the end of program 
#And replace RETURN with PRINT within the end of the function 
myCurl = """
curl 'https://lynfield.mystudent.school.nz/attendance' \
  -H 'authority: lynfield.mystudent.school.nz' \
  -H 'cache-control: max-age=0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'referer: https://lynfield.mystudent.school.nz/' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: __cfduid=d4d0ce098945690961541902c11403a881614837836; kamar_session=a1gvgjm662bvaber3o17hojccuodjjml; csrf_kamar_cn=f58ac3257f267b34d874a47901c9604a' \
  --compressed
""" 

"""
import requests

headers = {
    'authority': 'lynfield.mystudent.school.nz',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://lynfield.mystudent.school.nz/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d4d0ce098945690961541902c11403a881614837836; kamar_session=a1gvgjm662bvaber3o17hojccuodjjml; csrf_kamar_cn=f58ac3257f267b34d874a47901c9604a',
}

response = requests.get('https://lynfield.mystudent.school.nz/attendance', headers=headers)
"""

#CurlBashToPythonCookie(curlBash)


