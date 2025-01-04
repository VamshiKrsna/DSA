# 1930. Unique Length-3 Palindromic Subsequences

def uniquePalindromesBF(s:str)->int:
    fin = 0
    n = len(s)
    M: dict[str,tuple] = {} # Store first and last occurence of each character
    for i in range(n):
        if s[i] not in M:
            M[s[i]] = (i,i) # if substr (char) not in map, add it with index
        else:
            M[s[i]] = (M[s[i]][0],i) #otherwise, update the occurence
    for ch, pos in M.items():
        l,r = pos # l, r = first and last occrence of char
        if r - l <= 1: # if l,r are besides, leave it.
            continue
        unique_chars: set[str] = set(s[l + 1 : r])
        fin += len(unique_chars)
    return fin

def uniquePalindromeOpt(s:str)->int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    total_count, unique_char_count = 0,0
    for char in alphabet:
        leftmost_occurence = s.find(char)
        if leftmost_occurence == -1:
            continue
        rightmost_occurence = s.rfind(char)
        if leftmost_occurence >= rightmost_occurence:
            continue

        visited_chars = [False] * 128
        unique_char_count = 0
        for index in range(leftmost_occurence + 1, rightmost_occurence):
            if not visited_chars[ord(s[index])]:
                visited_chars[ord(s[index])] = True
                unique_char_count += 1
                if unique_char_count == 26:
                    break
        total_count += unique_char_count
    return total_count



if __name__ == '__main__':
    input_str = "aabca"
    res = uniquePalindromesBF(input_str)
    print(res)
    res1 = uniquePalindromeOpt(input_str)
    print(res1)
    # input_string = "aabca"
    # substrings = []
    # length = len(input_string)
    # for start in range(length):
    #     # Iterate over all possible end indices
    #     for end in range(start + 1, length + 1):
    #         # Generate substring by taking characters from start to end
    #         substring = input_string[start:end]
    #
    #         # Generate all possible substrings by skipping characters
    #         for mask in range(1 << (end - start - 1)):
    #             skipped_substring = ""
    #             for i in range(end - start):
    #                 if i == 0 or not (mask & (1 << (i - 1))):
    #                     skipped_substring += substring[i]
    #             if skipped_substring:  # Ensure substring is not empty
    #                 substrings.append(skipped_substring)
    #
    #     # Remove duplicates by converting the list to a set and then back to a list
    # substrings = list(set(substrings))
    # print(substrings)
    # counter = 0
    # for string in substrings:
    #     if string == string[::-1]:
    #         counter += 1
    # print(counter)