//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.math.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int a[][] = new int[n][2];
            for (int i = 0; i < n; i++) {
                a[i][0] = sc.nextInt();
                a[i][1] = sc.nextInt();
            }
            Solution obj = new Solution();
            int ans = obj.minRemoval(a);
            System.out.println(ans);

            System.out.println("~");
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    static int minRemoval(int intervals[][]) {
        // code here
        int n=intervals.length;
        
        Arrays.sort(intervals , (a,b)->Integer.compare(a[1],b[1]));
        
        int e=0;
        int ans=0;
        
        for(int i=0;i<n;i++){
            if(e>intervals[i][0])
                ans++;
            else
                e=intervals[i][1];
        }
        
        return ans;
        
    }
}
