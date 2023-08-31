# LynAttendance

LynAttendance is a terminal based tool to "scan" through the student portal to compile information about your total attendance which calculates your attendance rate.
This is done by sending requests to the student portal which only returns the your attendence one week at a time which is a limitation due to the layout of the site. 
This program then uses the structure of the site to extract and compile the attendence information.

>> 🔧 IMPORTANT! : My code here does not follow the best coding practices as it was one of the first projects I have worked on, but it does leave a point in time where I can look back at to see how far I have come.

# Installation
V1.1

> WARNING: USE THIS PROGRAM YOUR OWN RISK, THIS WAS JUST A SMALL SIDE PROJECT OF MINE AND ANY NEW UPDATES TO THE LYNFIELD STUDENT PORTAL
         MAY BREAK AND DEEM THIS PROGRAM TO NOT WORK. SO YOU THIS PROGRAM AT YOUR OWN RISK AND I AM NOT RESPONSIBLE FOR ANY DAMAGES AS
         YOU ARE CHOOSING TO RUN THIS PROGRAM

> WARNING2: PYTHON NEEDS TO BE INSTALLED FOR PROGRAM TO RUN
THIS PROGRAM WAS DESIGNED ON PYTHON VERSION 3.8.0 AND SHOULD WORK WITH PYTHON VERSIONS 3.7.X , 3.8.X  and NEWER PYTHON 3.X.X VERSIONS

For this program to run, Python3 must be installed.
If Python3 isn't installed, click the link below and follow instructions for installation 
https://www.python.org/downloads/

For this program to run, pip must be installed.
If pip isn't installed, click the link below and follow instructions for installation 
https://www.liquidweb.com/kb/install-pip-windows/


## REQUIRED LIBRARIES / PACKAGES:
- Request
- BeautifulSoup4

If the required packages / libraries are installed feel free to move onto the "How To Use" section of this ReadMe. If not continue reading.

If either or both libraries aren't installed, then follow the intructions below for installing these packages:
(Keep in mind that pip needs to be installed in order for these libraries to be install so if pip isn't installed follow this link: 
https://www.liquidweb.com/kb/install-pip-windows/ )

Installation for REQUEST package / library:

- Simple Route (BOTH python and pip must be install to work) :

1. Navigate to the Packages folder supplied with this repository.
2. Run the one or both .bat files to install your missing packages / libraries.
3. Close all terminals and restart all IDE's.
4. Done!


==============================================================

- Through CMD / Terminal (More difficult: BOTH python and pip must be install to work) :

1. launch terminal / cmd.
2. Type: "python -m pip install requests".
3. Close out of terminal / cmd and restart any running IDE's.
4. Done!

Installation for BeautifulSoup package / library:

1. launch terminal / cmd.
2. Type: "pip install beautifulsoup4".
3. Close out of terminal / cmd and restart any running IDE's.
4. Done!


- DOWNLOADING FILES:
These files can be downloaded in many ways:

Files can be cloned from this git repository by using:
"git clone https://github.com/ItzCino/LynAttendance.git"

The files can be downloaded directly:
1. Navigate to this repository: https://github.com/ItzCino/LynAttendance
2. Click on the green "Code" button and choose Download Zip as your option and you download should start automatically.


- HOW TO USE:

1. Launch the "attendanceMergedMain.py" file as this is the main program with python.
2. prompted with the "Insert Cookie" screen.
3. Now head over to "https://lynfield.mystudent.school.nz/" (Lynfield Parent Portal).
4. Once on the website press and hold Ctrl + Shift + I this will open up the inspect element page.
5. Now head over to the "Networks" Tab which is located on the top of the tabs of the Element inspector. 
   (Sometimes it's hidden and collasped in two right arrows).
   
7. Click on the "Networks" Tab.
8. Leave this Network log open and login to parent portal as per unsual.
9. On the Network log, a number of files will now appear.
10. Find the file named attendance and right click on it.
11. Find the option called "copy".
12. Once the option "copy" is found hover your mouse over it.
13. From here find the option called "Copy as cURL (bash)"
14. Now paste the "cookie" into the python terminal and hit enter.
15. If there is error, try getting a new cookie by freshing the page and repeating from steps 8 - 13.
16. And... Voilà there is your attendance!


NOTE: THIS PROGRAM ALSO WORKS ON https://repl.it/ (Soon to be Replit.com as time of writing.)
For it to work on repl, an repl account needs to be created and only the "attendanceMergedMain.py"

WARNING: USE THIS PROGRAM YOUR OWN RISK, THIS WAS JUST A SMALL SIDE PROJECT OF MINE AND ANY NEW UPDATES TO THE LYNFIELD PARENT PORTAL
         MAY BREAK AND DEEM THIS PROGRAM TO NOT WORK. SO YOU THIS PROGRAM AT YOUR OWN RISK AND I AM NOT RESPONSIBLE FOR ANY DAMAGES AS
         YOU ARE CHOOSING TO RUN THIS PROGRAM

V1.1

Cino
