month = input("Input the month (e.g. January, February etc.): ")

if month in ('January', 'February', 'December'):
	season = 'winter'
elif month in ('April', 'May', 'March'):
	season = 'spring'
elif month in ('July', 'August', 'June'):
	season = 'summer'
else:
	season = 'autumn'

print("Season is",season)