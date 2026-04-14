public class Solution {
    public int TitleToNumber(string columnTitle) {
        
        int result = 0;

        foreach (int ch in columnTitle)
        {
            result *= 26;
            result += ch - (int)'A' + 1;
        }

        return result;
            
    }
}