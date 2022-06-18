FF,FS,SF,SS = map(int,input().split())
if FF + FS == 0:
    print(SS + (SF > 0))
else:
    print(FF if not FS else FF + SS + min(SF, FS) * 2 + (FS > SF))
