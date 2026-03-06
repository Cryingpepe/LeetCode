class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int temp = 0;
        int result = 0;

        for (int i : nums){
            if (i == 1){
                temp++;
            }
            else{
                result = Math.max(temp, result);
                temp = 0;
            }
        }

        result = Math.max(temp, result);

        return result;

    }
}