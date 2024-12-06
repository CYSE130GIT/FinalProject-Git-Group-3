import pandas as pd
#Open csv with cp1252 encoding to prevent read/write errors when creating output report change path to get it to run
logs = pd.read_csv('C:\\Users\\hi2ma\\Documents\\CYSE 130\\Lab.csv', encoding='cp1252')
suspicious_logs=[]
#42 Event IDs for windows server security events gotten from https://www.xplg.com/windows-server-security-events-list/
#Each Event has its own counter to see how many events occured
Security_event_ids = [4624, 4625, 4634, 4648, 4719, 4964, 1102, 4720, 4722, 4723, 4725, 4728, 4732, 4756, 4738, 4740, 4767, 4735, 4737, 4755, 4772, 4777, 4782, 4616, 4657, 4697, 4698, 4699, 4700, 4701, 4702, 4946, 4947, 4950, 4954, 5025, 5031, 5152, 5153, 5155, 5157, 5447]
Counter4624 = 0
Counter4625 = 0
Counter4634 = 0
Counter4648 = 0
Counter4719 = 0
Counter4964 = 0
Counter1102 = 0
Counter4720 = 0
Counter4722 = 0
Counter4723 = 0
Counter4725 = 0
Counter4728 = 0
Counter4732 = 0
Counter4756 = 0
Counter4738 = 0
Counter4740 = 0
Counter4767 = 0
Counter4735 = 0
Counter4737 = 0
Counter4755 = 0
Counter4772 = 0
Counter4777 = 0
Counter4782 = 0
Counter4616 = 0
Counter4657 = 0
Counter4697 = 0
Counter4698 = 0
Counter4699 = 0
Counter4700 = 0
Counter4701 = 0
Counter4702 = 0
Counter4946 = 0
Counter4947 = 0
Counter4950 = 0
Counter4954 = 0
Counter5025 = 0
Counter5031 = 0
Counter5152 = 0
Counter5153 = 0
Counter5155 = 0
Counter5157 = 0
Counter5447 = 0
for index, row in logs.iterrows():
   if row[2] in Security_event_ids:
      suspicious_logs.append(row)
      match row[2]:
         case 4624:
            Counter4624 += 1
         case 4625:
            Counter4625 += 1
         case 4634:
            Counter4634 += 1
         case 4648:
            Counter4648 += 1
         case 4719:
            Counter4719 += 1
         case 4964:
            Counter4964 += 1
         case 1102:
            Counter1102 += 1
         case 4720:
            Counter4720 += 1
         case 4722:
            Counter4722 += 1
         case 4723:
            Counter4723 += 1
         case 4725:
            Counter4725 += 1
         case 4728:
            Counter4728 += 1
         case 4732:
             Counter4732 += 1
         case 4756:
            Counter4756 += 1
         case 4738:
            Counter4738 += 1
         case 4740:
            Counter4740 += 1
         case 4767:
            Counter4767 += 1
         case 4735:
            Counter4735 += 1
         case 4737:
            Counter4737 += 1
         case 4755:
            Counter4755 += 1
         case 4772:
            Counter4772 += 1
         case 4777:
            Counter4777 += 1
         case 4782:
            Counter4782 += 1
         case 4616:
            Counter4616 += 1
         case 4657:
            Counter4657 += 1
         case 4697:
            Counter4697 += 1
         case 4698:
            Counter4698 += 1
         case 4699:
            Counter4699 += 1
         case 4700:
            Counter4700 += 1
         case 4701:
            Counter4701 += 1
         case 4702:
            Counter4702 += 1
         case 4946:
            Counter4946 += 1
         case 4947:
            Counter4947 += 1
         case 4950:
            Counter4950 += 1
         case 4954:
            Counter4954 += 1
         case 5025:
            Counter5025 += 1
         case 5031:
            Counter5031 += 1
         case 5152:
            Counter5152 += 1
         case 5153:
            Counter5153 += 1
         case 5155:
            Counter5155 += 1
         case 5157:
            Counter5157 += 1
         case 5447:
            Counter5447 += 1
#Writes the findings to the file summary_report.txt change path to get it to run
with open('C:\\Users\\hi2ma\\Documents\\CYSE 130\\summary_report.txt', 'w') as f:
    f.write(f"Total suspicious logs found: {len(suspicious_logs)}\n")
    f.write('%s Successful account log on (Event ID: 4624)\n' %Counter4624) 
    f.write('%s Failed account log on (Event ID: 4625)\n' %Counter4625)
    f.write('%s An account logged off (Event ID: 4634)\n' %Counter4634)
    f.write('%s A logon attempt was made with explicit credentials (Event ID: 4648)\n' %Counter4648)
    f.write('%s System audit policy was changed (Event ID: 4719)\n' %Counter4719)
    f.write('%s A special group has been assigned to a new log on (Event ID: 4964)\n' %Counter4964)
    f.write('%s Audit log was cleared. This can relate to a potential attack (Event ID: 1102)\n' %Counter1102)
    f.write('%s A user account was created (Event ID: 4720)\n' %Counter4720)
    f.write('%s A user account was enabled (Event ID: 4722)\n' %Counter4722)
    f.write('%s An attempt was made to change the password of an account (Event ID: 4723)\n' %Counter4723)
    f.write('%s A user account was disabled (Event ID: 4725)\n' %Counter4725)
    f.write('%s A user was added to a privileged global group (Event ID: 4728)\n' %Counter4728)
    f.write('%s A user was added to a privileged local group (Event ID: 4732)\n' %Counter4732)
    f.write('%s A user was added to a privileged universal group (Event ID: 4756)\n' %Counter4756)
    f.write('%s A user account was changed (Event ID: 4738)\n' %Counter4738)
    f.write('%s A user account was locked out (Event ID: 4740)\n' %Counter4740)
    f.write('%s A user account was unlocked (Event ID: 4767)\n' %Counter4767)
    f.write('%s A privileged local group was modified (Event ID: 4735)\n' %Counter4735)
    f.write('%s A privileged global group was modified (Event ID: 4737)\n' %Counter4737)
    f.write('%s A privileged universal group was modified (Event ID: 4755)\n' %Counter4755)
    f.write('%s A Kerberos authentication ticket request failed (Event ID: 4772)\n' %Counter4772)
    f.write('%s The domain controller failed to validate the credentials of an account (Event ID: 4777)\n' %Counter4777)
    f.write('%s Password hash of an account was accessed (Event ID: 4782)\n' %Counter4782)
    f.write('%s System time was changed (Event ID: 4616)\n' %Counter4616)
    f.write('%s A registry value was changed (Event ID: 4657)\n' %Counter4657)
    f.write('%s An attempt was made to install a service (Event ID: 4697)\n' %Counter4697)
    f.write('%s Events related to Windows scheduled tasks being created, modified, deleted, enabled or disabled (Event ID: 4698)\n' %Counter4698)
    f.write('%s Events related to Windows scheduled tasks being created, modified, deleted, enabled or disabled (Event ID: 4699)\n' %Counter4699)
    f.write('%s Events related to Windows scheduled tasks being created, modified, deleted, enabled or disabled (Event ID: 4700)\n' %Counter4700)
    f.write('%s Events related to Windows scheduled tasks being created, modified, deleted, enabled or disabled (Event ID: 4701)\n' %Counter4701)
    f.write('%s Events related to Windows scheduled tasks being created, modified, deleted, enabled or disabled (Event ID: 4702)\n' %Counter4702)
    f.write('%s A rule was added to the Windows Firewall exception list (Event ID: 4946)\n' %Counter4946)
    f.write('%s A rule was modified in the Windows Firewall exception list (Event ID: 4947)\n' %Counter4947)
    f.write('%s A setting was changed in Windows Firewall (Event ID: 4950)\n' %Counter4950)
    f.write('%s Group Policy settings for Windows Firewall has changed (Event ID: 4954)\n' %Counter4954)
    f.write('%s The Windows Firewall service has been stopped (Event ID: 5025)\n' %Counter5025)
    f.write('%s Windows Firewall blocked an application from accepting incoming traffic (Event ID: 5031)\n' %Counter5031)
    f.write('%s A network packet was blocked by Windows Filtering Platform (Event ID: 5152)\n' %Counter5152)
    f.write('%s A network packet was blocked by Windows Filtering Platform (Event ID: 5153)\n' %Counter5153)
    f.write('%s Windows Filtering Platform blocked an application or service from listening on a port (Event ID: 5155)\n' %Counter5155)
    f.write('%s Windows Filtering Platform blocked a connection (Event ID: 5157)\n' %Counter5157)
    f.write('%s A Windows Filtering Platform filter was changed (Event ID: 5447)\n' %Counter5447)
    for log in suspicious_logs:
        f.write('%s\n' %log[0])
        f.write('%s\n' %log[1])
        f.write('%s\n' %log[2])   
        f.write('%s\n' %log[3])   
        f.write('%s\n' %log[4])
        f.write('------------------------------------------------------------------------------------------------------------------------------------\n\n\n\n')                      
x=input('Enter to Close')
