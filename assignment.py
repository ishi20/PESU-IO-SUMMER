def create_list():
	s = input("Enter your list of numbers: ")
	l = s.split(",")
	t = tuple(l)
	print('List : ',l)
	print('Tuple : ',t)

def even():
	numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958,743, 527 ]
	for i in range(len(numbers)):
		if numbers[i] == 237:
			break
		if numbers[i] %2 ==0:
			print(numbers[i])

def binary_search(start,end,key,l2):
	if start <= end:
		mid = int((start +  end)/2)
		if l2[mid] > key:
			return binary_search(start,mid-1,key,l2)
		elif l2[mid] < key:
			return binary_search(mid+1, end, key ,l2)
		elif l2[mid] == key:
			return mid

	else:
		return -1

def sum():
	n = int(input("Enter a number: "))
	sum =0
	while n!= 0:
		sum += n%10
		n = int (n/10)
	print (sum)
def check_num():
	st = input("Enter a string: ")
	print (st.isdigit())
'''
create_list()
even()
st = input("Enter a list of numbers seperated by space: ")
l2 = st.split()
l2 = [ int(i) for i in l2]
key = int(input("Enter number to be searched: "))
pos=binary_search(0,len(l2),key,l2)
if pos == -1:
	print("The number isn't in the list")
else:
	print(pos,"\n")
sum()
check_num()
'''
