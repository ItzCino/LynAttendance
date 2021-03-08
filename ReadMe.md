V1.0

WARNING: PYTHON NEEDS TO BE INSTALLED FOR PROGRAM TO RUN
THIS PROGRAM WAS DESIGNED ON PYTHON VERSION 3.8.0 AND SHOULD WORK WITH NEWER VERSIONS


For this set of program to run pip needs to be installed.
Pip isn't installed, click the link below and follow instructions for installation
https://www.liquidweb.com/kb/install-pip-windows/
If the required packages / libraries are installed feel free to move onto the "How To Use" section of this ReadMe.

Required Libraries / Packages:

Request
BeautifulSoup4

if either library isn't installed then follow the intructions below for installing these packages:
(Keep in mind that pip needs to be installed in order for these libraries to be install so if pip isn't installed follow this link: 
https://www.liquidweb.com/kb/install-pip-windows/ )

Installation for REQUEST package / library:

Simpler Route:

1. Navigate to the Packages folder supplied with this repository.
2. Run the files to install your missing packages / libraries.
3. Close all terminals and restart all IDE's.
4. Done!


==============================================================

Through CMD / Terminal (More difficult) :

1. launch terminal / cmd.
2. Type: "python -m pip install requests".
3. Close out of terminal / cmd and restart any running IDE's.
4. Done!

Installation for BeautifulSoup package / library:

1. launch terminal / cmd.
2. Type: "pip install beautifulsoup4".
3. Close out of terminal / cmd and restart any running IDE's.
4. Done!


HOW TO USE:

1. Launch the "AttendanceMain.py" file as this is the main program with python.
2. prompted with the "Insert Cookie" screen.
3. Now head over to "https://lynfield.mystudent.school.nz/" (parent portal).
4. Once on the website press and hold Ctrl + Shift + I this will open up the inspect element page.
5. Now head over to the "Networks" Tab which is located on the top of the Element inspector. (Sometimes it's hidden and collasped under two right arrows).
6. Click on the "Networks" Tab.
7. Leave this Network log open and login to parent portal
8. On the Network log, a number of files will now appear.
9. Find the file named attendance and right click on it.
10. Find the option called "copy".
11. Once the option "copy" is found hover your mouse over it.
12. From here find the option called "Copy as cURL (bash)"
13. Now paste the "cookie" into the python terminal and hit enter.
14. If there is error, try getting a new cookie by freshing the page and repeating steps 8 - 13.
15. And... Voilà there is your attendance!


V1.0

- Cino
