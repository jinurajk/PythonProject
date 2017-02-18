str = "this is string example....wow!!!";

suffix = "wow!!!";
suffix1 = "wow!!!!";
print (str.endswith(suffix))
print (str.endswith(suffix,20))
print (str.endswith(suffix1,20))

print ("Double exapanded tab: " +str.expandtabs(12))
print ("Double exapanded tab: " +str.expandtabs())

str1 = "exam";

print (str.find(str1))
print (str.find("jnjjj", 10))
print (str.index("jnjjj", 10))

