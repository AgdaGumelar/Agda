#print(range(3)
#range(0,3) 

# program perulangan
for i in (range(3)):
	print(i)
	
#perulangan 1 data = 0, i = 0, kemudian cetak 0
#perulangan 2 data = 1, i = 1, kemudian cetak 1
#perulangan 3 data = 2, i = 2, kemudian cetak 2
#begitu seterusnya sampai proses mencapai stop 6, 6

#for i in (range(3,6)):
#	print(i)

#for i in (range(1,9,+3):
#	print(i)

for i in range (10,3,-2):
	print(i)
	
#range (10,3,-2) = [10,8,6,4]

#perulangan 1, data =10, i =10, cetak 10
#perulangan 2, data =10-2, i = 8, cetak 8
#perulangan 3, data = 8-2, i = 6, cetak 6
#perulangan 4, data = 6-2, i = 4, cetak 4

#perulangan 5 tidak ada karena 
#	data sudah mencapai batas maksimal dari stop

for i in range(0,5):
	for j in range (0, i+1):
		print("i : ",i,"j : ",j)
		#print("*", end=" ")
	print()
	
#perulangan 1, i = 0,
#	for j range (0,1)

#perulangan 2, i = 1
#	for j range (0,2)

