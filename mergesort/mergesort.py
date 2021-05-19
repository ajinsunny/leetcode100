
'''

Given this input array. Can you sort this using merge sort? 


arr = [32,27, 43, 3, 9, 82, 10]


Step 1. 

Find the middle point 

Step 2. 

call merge sort on left chunk of arr

Step 3. 
Call merge sort on right chunk of arr

Step 4. 
Use two pointer to iterate through the left and right chunk 

-    if the ith value on the left chunk is less than the right chunk 
-     assign the lower value to the kth value of the main array 
      if the other way round
        assign lower value to the main array. 
        
Step 5. 
Ensure there is no remaining elements in the left and right chunk: 
    if there is any then append it to the main array 
    
  
'''

def merge_sort(arr):
  if len(arr)>1:
      
    
    
    mid = len(arr)//2
    
    left_chunk = arr[:mid]
    right_chunk = arr[mid:]
    
    merge_sort(left_chunk)
    merge_sort(right_chunk)
    
    
    i,j,k = 0,0,0
    
    while i<len(left_chunk) and j<len(right_chunk):
      
      if left_chunk[i]<right_chunk[j]:
        arr[k] = left_chunk[i]
        i+=1
      else:
        arr[k] = right_chunk[j]
        j+=1
      k+=1
      
    while i <len(left_chunk):
      arr[k]=left_chunk[i]
      i+=1
      k+=1
    
    while j <len(right_chunk):
      arr[k]=right_chunk[j]
      j+=1
      k+=1

  return arr 

array = [32,27, 43, 3, 9, 82, 10]
print(merge_sort(array))