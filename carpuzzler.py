import math


"""con_1 last 4 letters palindrome
con_2 last 5 letters palindrome
con_3 middle 4 letters palindrome
con_4 all palindrome

"""
def pal(n):
	x = n[::-1]

	if (x==n): 
		return 'ok'
	
print 'miles, con_1, con_2, con_3, con_4'

for miles in range(1000000):
	i=str(miles)
	con_1 = i[2:]
	i=str(miles+1)
	con_2 = i[1:]
	i=str(miles+2)
	con_3 = i[1:5]
	i=str(miles+3)
	con_4 = i
	if pal(con_1) == 'ok' and pal(con_2) == 'ok' and pal(con_3) == 'ok' and pal(con_4) == 'ok':
		if len(str(miles))==6:
			print miles,con_1,con_2,con_3,con_4
