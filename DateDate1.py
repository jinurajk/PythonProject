import calendar

cal = calendar.month(2016,7)
print ("Calendar of 2016 July ", cal)

print ("First week day ",calendar.firstweekday( ))

print (" 2016 Is Leapyear",  calendar.isleap(2016))
print (" 2015 Is Leapyear",  calendar.isleap(2015))

print ("Leap years b/w 1950 and 2017",  calendar.leapdays(1950,2017))

print ("Month Apr 2016", calendar.month(2016,4,w=4,l=1))

print ("Month Apr 2016",calendar.monthrange(2016,7))