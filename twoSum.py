from typing import List

class solution:

	def binarySearch (arr, l, r, x): 
	  
		# Check base case 
		if r >= l: 

			mid = l + (r - l)//2
	        
			# If element is present at the middle itself 
			if arr[mid] == x: 
				return mid 
			
			# If element is smaller than mid, then it 
			# can only be present in left subarray 
			elif arr[mid] > x: 
				return binarySearch(arr, l, mid-1, x) 

			# Else the element can only be present 
			# in right subarray 
			else: 
				return binarySearch(arr, mid + 1, r, x) 

		else: 
			# Element is not present in the array 
			return -1

	
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		
		index1 = 0
		index2 = 0

		while index1 < len(nums)-1:
			diff = nums[index1] + target
			index2 = binarySearch(nums, index1+1, len(nums)-1, diff)

			#print (index1)
			
			if index2 == -1:
				index1 += 1

			else:
				return [index1, index2]

			

		#return [index1, index2]



	

n = [2, 7, 11, 29]
t = 8

test1 = solution()

test1.twoSum(n, t)
