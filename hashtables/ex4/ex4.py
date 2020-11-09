def has_negatives(a):
    nums = {}
    nums2 = []
    #loop through each number
    for num in a:
        #see if num has a corr "-" num
        if nums.get(
            abs(num)): #returns absolute num
            #see if it adds to zero
            if(nums.get(abs(num)) + num) == 0:
                #if it does equal zero
                nums2.append(abs(num))
        else:
            #if no value is found, pass num as new key as well as it's value
            nums[abs(num)] = num
    return nums2


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))