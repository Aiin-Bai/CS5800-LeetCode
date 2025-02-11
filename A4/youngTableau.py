class YoungTableau:
    def __init__(self, m, n):
       
      
        self.M = [[float('inf')] * n for _ in range(m)]
    
    def Print(self):
       
        print("\n".join([str(_) for _ in self.M]))
    
    def ExtractMin(self):
        if self.M[0][0] == float('inf'):
            return None
        min_val = self.M[0][0]
        i, j = 0, 0
        m, n = len(self.M), len(self.M[0])
        while True:
            min_i, min_j = i, j
            if j + 1 < n and self.M[i][j + 1] < self.M[min_i][min_j]:
                min_i, min_j = i, j + 1
            if i + 1 < m and self.M[i + 1][j] < self.M[min_i][min_j]:
                min_i, min_j = i + 1, j
            if (min_i, min_j) == (i, j) or self.M[min_i][min_j] == float('inf'):
                self.M[i][j] = float('inf')
                break
            self.M[i][j] = self.M[min_i][min_j]
            i, j = min_i, min_j
        return min_val
    
    def Insert(self, v):
        m, n = len(self.M), len(self.M[0])
    
        if self.M[m-1][n-1] != float('inf'):
            return False
        
   
        i, j = m-1, n-1
        self.M[i][j] = v
    
   
        while (i > 0 and self.M[i-1][j] > v) or (j > 0 and self.M[i][j-1] > v):
            if i > 0 and self.M[i-1][j] > v and (j == 0 or self.M[i-1][j] > self.M[i][j-1]):
           
                self.M[i][j], self.M[i-1][j] = self.M[i-1][j], self.M[i][j]
                i -= 1
            else:
            
                self.M[i][j], self.M[i][j-1] = self.M[i][j-1], self.M[i][j]
                j -= 1
            
        return True
    
    def Search(self, v):
        m, n = len(self.M), len(self.M[0])
        i, j = 0, n-1 
    
        while i < m and j >= 0:
            if self.M[i][j] == v:
                return (i, j)
            elif self.M[i][j] > v:
                j -= 1  
            else:
                i += 1  
            
        return None


# Test code
if __name__ == "__main__":
    # Create an empty 2x3 Young tableau
    yt = YoungTableau(2, 3)
    
    # Test insertions
    yt.Insert(7)
    yt.Insert(6)
    yt.Insert(9)
    yt.Insert(1)
    yt.Insert(3)
    yt.Insert(5)
    yt.Insert(2)  
    
    print("Initial Young tableau:")
    yt.Print()
   
    # Test searches
    print("\nSearch results:")
    print(yt.Search(1))   # should output (0, 0)
    print(yt.Search(2))   # should output None
    print(yt.Search(3))   # should output (0, 1)
    print(yt.Search(4))   # should output None
    print(yt.Search(5))   # should output (0, 2)
    print(yt.Search(6))   # should output (1, 0)
    print(yt.Search(7))   # should output (1, 1)
    print(yt.Search(8))   # should output None
    print(yt.Search(9))   # should output (1, 2)
    print(yt.Search(10))  # should output None
    
    # Test extractions
    print("\nExtracting minimum elements:")
    print(yt.ExtractMin())  # should output 1
    yt.Print()
    # Expected output example:
    # [3, 5, 9]
    # [6, 7, inf]
    
    print("\nExtracting next minimum:")
    print(yt.ExtractMin())  # should output 3
    yt.Print()
    # Expected output example:
    # [5, 7, 9]
    # [6, inf, inf]

    # Test 1: Operations on empty tableau
    yt = YoungTableau(2, 2)
    print(yt.ExtractMin())  # Should output None, because tableau is empty
    print(yt.Search(1))     # Should output None, because tableau is empty
    yt.Print()              # Should show all inf values

    # Test 2: Operations on full tableau and boundary values
    yt = YoungTableau(2, 2)
    print(yt.Insert(1))  # Should return True
    print(yt.Insert(2))  # Should return True
    print(yt.Insert(3))  # Should return True
    print(yt.Insert(4))  # Should return True
    print(yt.Insert(5))  # Should return False, because tableau is full
    print(yt.Search(0))  # Should return None
    print(yt.Search(5))  # Should return None
    yt.Print()          # Should show filled 2x2 matrix

    