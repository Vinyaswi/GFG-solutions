class Solution {
    public int largest(List<int> arr) {
        // code here.
        int max=int.MinValue;
        foreach(int a in arr){
            if(a>max){
                max=a;
            }
        }
        return max;
    }
}
