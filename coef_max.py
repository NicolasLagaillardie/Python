def coef_max(t):
	max=0
	for i in range(len(t)):
		if abs(t[i])>max:
			max=t[i]
	return max
