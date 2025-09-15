
class Solution {
    public int countOfElements(int x, List<Integer> arr) {
        // Code here
        int count=0;
        for(int i : arr){
            if(i<=x) count++;
        }
        return count;
    }
}