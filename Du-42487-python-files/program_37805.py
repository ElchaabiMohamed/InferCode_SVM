def minimum(l):
    if len(l)==1:
        return l[0]
    else:
        mnum = minimum(l[1:])
        minn = mnum
        if mnum < minn:
            minn = mnum
        return minn