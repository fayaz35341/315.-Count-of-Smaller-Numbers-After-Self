/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function(nums) {
    let arr = Array.from(new Set(nums)).sort((a, b) => a - b);
    let idx = new Map();

    for (let i = 0; i < arr.length; i++) {
        idx.set(arr[i], i + 1);
    }

    let m = arr.length;
    let bit = new Array(m + 1).fill(0);
    let res = [];
    let n = nums.length;

    for (let i = 0; i < n; i++) {
        let j = n - 1 - i;   // iterate backwards

        // 🔍 Query: count of smaller elements
        let count = 0;
        let k = idx.get(nums[j]) - 1; // strictly smaller

        while (k > 0) {
            count += bit[k];
            k -= k & -k;
        }

        // ⬆ Update BIT
        let val = idx.get(nums[j]);
        while (val <= m) {
            bit[val] += 1;
            val += val & -val;
        }

        res.push(count);
    }

    return res.reverse();
};
