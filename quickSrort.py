#sorting method
def quickSort(aList):
	quickSortHelper(aList, 0, len(aList)-1)

def quickSortHelper(aList, start, end):
	if start < end:
		pivot = partition(aList, start, end)
		quickSortHelper(aList, start, pivot-1)
		quickSortHelper(aList, pivot+1, end)

def partition(aList, start, end):

	pivot = aList[end]

	while start < end:
		while aList[start] < pivot:
			start += 1
		while aList[end] > pivot:
			end -= 1
		swap(aList, start, end)

		if(aList[start] == aList[end]):
			start += 1
	return end    

def swap(aList, start, end):

	temp = aList[start]
	aList[start] = aList[end]
	aList[end] = temp


aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(aList)
print aList