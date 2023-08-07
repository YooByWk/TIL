pattern = ['ZRO', 'ONE', 'TWO']
original = list('ZRO ZRO  ONE ONE TWO ZRO'.split())


result = []
# for n in original: 
    # # 1 
    # for i in rnage(3):
    #     if pattern[i] == n:
    #         result.append(i)
            # break
#pattn = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2}

for n in original: 
    result.append(pattern[n])
