strs = ["flower", "flow", "flight","flow1","flow2","flow3"]
strs1 = ["flower", "flow"]
strs2 = ["abddfd","ab", "abc", "abdddd","abeeeee","abwqwqwq12","ab23"]






def find_prefix (strs):
    res = ""
    strs.sort(key=len)
    WORD_TO_COMPARE = strs[0]

    for char in range (len(WORD_TO_COMPARE)):
        to_compare = WORD_TO_COMPARE[char]
        res = res +to_compare

        for str in strs:
            if (to_compare != str [char] ) :
                break

    return res

prefix  = find_prefix(strs2)
print(prefix)







