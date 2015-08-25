#insert sort

def insertSort(aList):
	for index in range(1, len(aList)):
		key = aList[index]
		position = index -1

		while position >= 0 and aList[position]>key:
			aList[position+1] = aList[position]
			position = position -1

		aList[position+1] = key

def mergeSort(aList):
	if len(aList)>1:
		midpoint = len(aList)//2
		left = aList[:midpoint]
		right = aList[midpoint:]
		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0
		while i<len(left) and j<len(right):
			if left[i] < right[j]:
				aList[k] = left[i]
				i = i+1
			else:
				aList[k] = right[j]
				j = j+1
			k= k+1
		while i < len(left):
			aList[k] = left[i]
			i = i+1
			k = k+1
		while j < len(right):
			aList[k] = right[j]
			j = j+1
			k = k+1

aList1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
aList2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertSort(aList1)
mergeSort(aList2)
print "insertSort ", aList1
print "mergeSort ", aList2