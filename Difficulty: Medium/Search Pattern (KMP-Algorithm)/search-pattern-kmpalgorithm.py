#User function Template for python3
class Solution:
    def search(self, pat, txt):
        def rabin_karp(pat, txt, prime=101):
            m, n = len(pat), len(txt)
            pat_hash, txt_hash = 0, 0
            h = 1
            result = []
            d = 256  # Number of characters in the input alphabet
            
            # Precompute h = (d^(m-1)) % prime
            for i in range(m - 1):
                h = (h * d) % prime

            # Compute initial hash values for the pattern and first window of text
            for i in range(m):
                pat_hash = (d * pat_hash + ord(pat[i])) % prime
                txt_hash = (d * txt_hash + ord(txt[i])) % prime

            for i in range(n - m + 1):
                # Check if current window hash matches pattern hash
                if pat_hash == txt_hash:
                    # If hash matches, check characters one by one
                    if txt[i:i + m] == pat:
                        result.append(i)

                # Calculate hash for next window (if not the last one)
                if i < n - m:
                    txt_hash = (d * (txt_hash - ord(txt[i]) * h) + ord(txt[i + m])) % prime
                    if txt_hash < 0:
                        txt_hash += prime

            return result

        return rabin_karp(pat, txt)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends