# Python program for KmP Algorithm 
# KmP algorithm is used to search if a particular string pattern is a substring in given txt string.
def kmp_search(pat, txt): 
    m = len(pat) 
    n = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*m 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    compute_lps_array(pat, m, lps) 
  
    i = 0 # index for txt[] 
    while i < n: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == m: 
            print (str(i-j)) 
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < n and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def compute_lps_array(pat, m, lps): 
    len = 0 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
   
    while i < m: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1