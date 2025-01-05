# 2381. Shifiting Letters II (PoTD 05/01/2025)

def shiftBF(s:str,shifts:list)->str:
    slist = list(s)
    for shift in shifts:
        start, end, direction = shift
        substring = slist[start:end + 1]
        if direction == 0:  # Backwards
            for i in range(len(substring)):
                if ord(substring[i]) == 97:  # Shifting backwards from 'a'
                    slist[start + i] = chr(ord(substring[i]) + 25)  # Shift to 'z'
                else:
                    slist[start + i] = chr(ord(substring[i]) - 1)  # Shift 1 pos backwards
        else:  # Forwards
            for i in range(len(substring)):
                if ord(substring[i]) == 122:  # Shifting forwards for 'z'
                    slist[start + i] = chr(ord(substring[i]) - 25)
                else:
                    slist[start + i] = chr(ord(substring[i]) + 1)
    return ("".join(slist))

def shiftOptimal(s:str,shifts:list)->str:
    pass


if __name__ == '__main__':
    # print("Hello")
    # print(ord("b"))
    # print(chr(97)) # Backwards : 97->122
    s = "abc"
    shifts = [[0,1,0],[1,2,1],[0,2,1]]
    print(shiftBF(s,shifts))
    # for shift in shifts:
    #     start = shift[0]
    #     end = shift[1]
    #     dir = shift[2]
    #     if dir == 0: # For Backward Direction
    #         temp = s[start:end + 1]
    #         print(temp)
    #         for i in range(len(temp)):
    #             if ord(temp[i]) == 97:
    #                 temp = temp.replace(temp[i],chr(ord(temp[i])+25))
    #             temp = temp.replace(temp[i],chr(ord(temp[i])-1))
    #         print(temp)
    #     else:
    #         temp = s[start:end+1]
    #         print(temp)
    #         for i in range(len(temp)):
    #             if ord(temp[i]) == 122:
    #                 temp = temp.replace(temp[i],chr(ord(temp[i])-25))
    #             temp = temp.replace(temp[i],chr(ord(temp[i])+1))
    #         print(temp)
    # BETTER APPROACH WITH SAME IDEA :
