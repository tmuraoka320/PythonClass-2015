def Ordinal(i):
	try:
		if i%1==0:
			if str(i)[-2:-1]=="1": return "%dth" % i
			elif str(i)[-1]=="1": return "%dst" % i
			elif str(i)[-1]=="2": return "%dnd" % i
			elif str(i)[-1]=="3": return "%drd" % i
			else: return "%dth" % i
		else:
			raise Exception
	except:
		return "Type Integers!"

print Ordinal("a")
print Ordinal(12.2)
print Ordinal(1)
print Ordinal(2)
print Ordinal(3)
print Ordinal(11)
print Ordinal(16)
print Ordinal(111)