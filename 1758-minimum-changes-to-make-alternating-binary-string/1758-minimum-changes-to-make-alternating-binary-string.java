class Solution {
    public int minOperations(String s) {
        int count = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0 && s.charAt(i) != '0') {
                count++;
            } else if (i % 2 == 1 && s.charAt(i) != '1') {
                count++;
            }
        }

        return Math.min(count, n - count);
    }
}