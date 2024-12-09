# Preface:
The Project's goal was to create UML diagrams based off of a mock scenario interview given to us in class (Findings and Requirements Analysis Included) and create some sample automation scripts using Python.
The main purpose of this read me file is to give context and instructions for the python scripts.
The Results Folder contains sample outputs from the python scripts.


# Script Purpose and Usage:

## Task 1
The purpose of the script is to analyze a log file easily using Python instead of manually parsing it. We took one of our own Windows security logs and parsed through the log files, looking for event IDs from this list: https://www.xplg.com/windows-server-security-events-list/. The Pandas library was used to open and read the log file (CSV format). We then parsed through the file, searching for the specific event IDs, and wrote them to a file. The output file categorizes the specific events, tallies them up, and holds the details of the event. The output file (summary_report.txt) is attached in the results folder.

To run the code yourself make sure you change line 3 to have the correct file path to the log file (in CSV form) that you want to use. The code works only for windows security logs. Change the file path on the output file on line 139 to get it to run as well. For some reason the code would not work without specifying an absolute path.

## Task 2 and 3
The purpose of this script is to monitor the performance of a system. The script is looking at CPU usage, memory usage, and disk usage. If the usage on the device ever reaches a certain threshold (currently 60%), it prints out a message to the terminal, creates a log file, and attempts to send an alert message via email. The script then sleeps for 30 seconds before continuing to run. Psutil library is used to pull system data, while smtplib is used to send the alert through email. Currently, smtplib is not sending emails with either Gmail or Yahoo emails, but the code should be correct in theory. We were able to verify that the system monitoring worked through terminal print commands.  

The email alert function is currently broken. Despite following the proper syntax provided by the professor and researching the issue on google we were unable to login to an email and send a message. Other students in the discord were also unsuccessful with getting the email alert to work, so we just left a comment above the function. The Log file when created writes to the user's folder (e.g. "C:\Users\name\system_performance.log"). Because the email function is broken the script will exit/crash when trying to send the email, if you want to persitently run the logging function delete or comment out the content of the send_alert function.

## Task 4
There are two separate scripts in task 4 so it was saved as a Jupyter notebook. The first script runs an Nmap scan on the host every hour and sends the results to a new output file. The schedule library is used to help schedule the task, and the DateTime library is used to generate a timestamp for the scan (It also helps name the output file as something unique). Subprocess is used to run Nmap. Nmap was run with the -sV to find a version of the service on a given port. We ran Nmap at intensity five as anything higher would cause the scan not to complete on Windows (Linux, regardless of intensity). The -v argument was used to troubleshoot scanning issues.
The second script was a simple script to sniff ten packets at a time and write them to a Pcap file. Scapy is imported as our packer sniffer, and it sniffs the first ten packets. The packets are then checked to see if they are TCP/IP, then the source and destination addresses are printed in the terminal. The capture as a whole is written to a pcap file (Test.pcap).

# Team Members:
 Peter Turnbull: Completed Tasks 1 and 4 for the Python automation assignment and created the Github Repository

Christian Jackson: Completed Tasks 2 and 3 for the Python automation assignment.

Yusif Nasirov: Assisted in the creation of the diagrams and final report.

Masen Nguyen: Assisted in the creation of the Analysis Document and diagrams.

Zaid AlShayji: Assisted in the creation of the final report, agreement forms, and Gannt Chart.

Yukki Vu: Assisted in the creation of the Analysis Document and diagrams.
