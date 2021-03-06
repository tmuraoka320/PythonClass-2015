class Clock(object):
	def __init__(self, hour, minutes):
		self.minutes = minutes
		self.hour = hour
	
	@classmethod
	def at(cls, hour, minutes=0): 
		return cls(hour, minutes)
	
	def __str__(self):
		if self.hour < 10: hour2 = "0%d" % self.hour
		else: hour2 = self.hour
		if self.minutes < 10: minutes2 = "0%d" % self.minutes
		else: minutes2 = self.minutes
		return "%s:%s" %(hour2, minutes2)
	
	def __add__(self,added_minutes):
		sum_minutes=self.minutes+added_minutes
		updated_minutes=sum_minutes%60
		updated_hours=self.hour+sum_minutes/60
		if updated_hours >= 24: updated_hours -= 24
		else: updated_hours = updated_hours
		return Clock(updated_hours,updated_minutes)

	def __sub__(self,subtract_minutes):
		sub_minutes = self.minutes - substract_minutes%60
		down_hour = self.hour - subtract_minutes/60
		if sub_minutes < 0:
			down_minutes = 60 + sub_minutes
		else: down_minutes = sub_minutes
		return Clock(down_hour, down_minutes)

	def __eq__(self, other):
		return self.hour == other.hour and self.minutes == other.minutes

	def __ne__(self, other):
		return self.hour != other.hour or self.minutes != other.minutes

clock = Clock(23,9)
print clock
print clock + 130
print clock + - 130
print clock
clock1 = Clock(11,11)
clock2 = Clock(11,11)
print clock1 == clock2
clock3 = Clock(12,12)
clock4 = Clock(12,13)
clock5 = Clock(13,12)
print clock3 != clock4
print clock3 != clock5