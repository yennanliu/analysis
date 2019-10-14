def json_reformat(j):
    """
    : input  : { "a": 1, "b": { "c": 2, "d": [3,4] } }
    : output : {"a": 1, "b.c": 2, "b.d": [3,4] }
    """
    def get_flat(pre,j):
        for i in j:
            print (j[i], type(j[i]))
            if type(j[i]) != dict:
                if pre == "":
                    res[i] = j[i]
                else:
                    res[pre + "." + str(i)] = j[i]
            else:
                pre = str(i) 
                get_flat(pre, j[i])
        return res 
    res = {}
    pre = ""
    res = get_flat(pre, j)
    print (res)
    return res 