def Ordinal(i):
	last = str(i)[-1]
	try:
		if str(i)[-2]=='1':
			raise Exception
		elif last=='1': return "%dst" % i
		elif last=='2': return "%dnd" % i
		elif last=='3': return "%drd" % i
		else: return "%dth" %i
	except TypeError: return "Enter integer!"
	except:
		return "%dth" %i
		
print Ordinal(1)