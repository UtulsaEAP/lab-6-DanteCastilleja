"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def in_order(nums):
   for num in range(len(nums) - 1) :
       if nums[num] > nums[num + 1] :
           return False
   return True
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else: 
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
