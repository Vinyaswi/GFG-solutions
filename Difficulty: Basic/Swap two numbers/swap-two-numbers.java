class Solution {
    static List<Integer> get(int a, int b) {
        // code here
        List<Integer> temp=new ArrayList<>();
        
        a=a+b;
        b=a-b;
        a=a-b;
        temp.add(a);
        temp.add(b);
        return temp;
    }
}