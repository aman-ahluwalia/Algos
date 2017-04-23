def insertionSort(A):
	for i in range(1,len(A)):
		key = A[i]
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key

def main():
	n = int(raw_input('Number of inputs to be sorted (in one line please): '))
	A = map(int, raw_input().split())
	insertionSort(A)
	print A

if __name__ == "__main__": main()