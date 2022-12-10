idx1 = -1
def forEach(arr, do):
    global idx1
    idx1+=1
    if idx1!=len(arr):
        try:
            do(arr[idx1], idx1, arr)
        except:
            try:
                do(arr[idx1], idx1)
            except:
                do(arr[idx1])
        forEach(arr, do)
    else:
        idx1 = -1
