import logparser
file = open('access.log','r')
frequency = {}
for line in file:
 part = parser.parser(line)
 date = part['time'][0:11]
 time = part['time'][12:14]
 status = part['status']
 if date not in frequency:
   frequency[date] = {time:{status:1}}
 else:
   if time not in frequency[date]:
     frequency[date][time] = {status:1}
   else:
     if status not in frequency[date][time]:
       frequency[date][time][status] = 1
     else:
       frequency[date][time][status] = frequency[date][time][status]+ 1
file.close()
#print(frequency)
for date in frequency:
 print("\nDate::", date)
 for hour in frequency[date]:
   print(" Hour::", hour)
   for status in frequency[date][hour]:
     print(" Status::", status , "Count::", frequency[date][hour][status])
