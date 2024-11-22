

class Solution:
    def maximumProfit(self, prices):
        
        profit,min_price=0,prices[0]
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends