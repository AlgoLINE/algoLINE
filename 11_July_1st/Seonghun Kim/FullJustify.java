public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        
        List<Integer> rowsAndWords = new LinkedList<Integer>();
        
        // count rows and number of words at each row
        int length = 0;
        List<String> rowWords = new ArrayList<String>();
        List<String> justified = new ArrayList<String>();
        
        for (int i = 0 ; i < words.length ; i++) {
            String word = words[i];
            int wordLength = word.length();
            if (length + wordLength <= maxWidth) {
                rowWords.add(word);
                length += (wordLength + 1);
            } else {
                justified.add(addExtraSpace(rowWords, length, maxWidth));
                rowWords.clear();
                rowWords.add(word);
                length = (wordLength + 1);
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < rowWords.size() - 1 ; i++) {
            sb.append(rowWords.get(i) + " ");
        }
        sb.append(rowWords.get(rowWords.size()-1));
        int remained = maxWidth - sb.length();
        while (remained > 0) {
            sb.append(" ");
            remained -= 1;
        }
        
        justified.add(sb.toString());
        return justified;
    }
    
    private String addExtraSpace(List<String> rowWords, int length, int maxWidth) {
        
        if (rowWords.size() == 1) {
            StringBuilder sb = new StringBuilder();
            sb.append(rowWords.get(0));
            int remained = maxWidth - sb.length();
            while (remained > 0) {
                sb.append(" ");
                remained -= 1;
            }
            
            return sb.toString();
        }
        
        int remainSpace = maxWidth - length + 1; // +1 means last extra space
        int quotient = remainSpace / (rowWords.size() - 1);
        int remainder = remainSpace % (rowWords.size() - 1);
        
        StringBuilder extraSpace = new StringBuilder();
        int cnt = 0;
        while (cnt < quotient) {
            extraSpace.append(" ");
            cnt += 1;
        }
        String extraString = extraSpace.toString();
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < rowWords.size()-1 ; i++) {
            String word = rowWords.get(i);
            sb.append(word + " ");
            sb.append(extraString);
            if (remainder > 0) {
                sb.append(" ");
                remainder -= 1;
            }
        }
        sb.append(rowWords.get(rowWords.size()-1));
        
        return sb.toString();
    }
}