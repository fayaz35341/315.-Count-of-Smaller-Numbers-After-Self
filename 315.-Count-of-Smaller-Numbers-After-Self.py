class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # count frequency from left to right
        arr = sorted(set(nums))
        idx = {v: i+1 for i, v in enumerate(arr)}

        m = len(idx)
        bit = [0] * (m+1)
        res = []
        n = len(nums)
        for i in range(n):
            j = n - 1 - i # backwards

            # query
            count = 0
            k = idx[nums[j]] - 1 # strictly lower
            while k > 0:
                count += bit[k]
                k -= k & -k

            # update
            val = idx[nums[j]]
            while val <= m:
                bit[val] += 1
                val += val & -val            

            res.append(count)

        return res[::-1]

        # n = len(nums)
        # result = [0] * n
        # for i in range(n):
        #     count = 0
        #     for j in range(i + 1, n):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     result[i] = count
        # return result 

        # c=[0]*len(nums)
        # enum=list(enumerate(nums))

        # def mergeS(nums):
        #     if len(nums)<=1:
        #         return nums
        #     mid=len(nums)//2
        #     left=mergeS(nums[:mid])
        #     right=mergeS(nums[mid:])
        #     return m_s(left,right)

        # def m_s(left,right):
        #     result=[]
        #     i=j=0
        #     while i<len(left) and j<len(right):
        #         if left[i][1] <= right[j][1]:
        #             result.append(left[i])
        #             c[left[i][0]]+=j
        #             i+=1
        #         else:
        #             result.append(right[j])
        #             j+=1
        #     while i < len(left):
        #         result.append(left[i])
        #         c[left[i][0]] += j
        #         i += 1
            
        #     result.extend(right[j:])
        #     return result
        # mergeS(enum)
        # return c
