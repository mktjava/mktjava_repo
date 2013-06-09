import sys

fs = []
argc = len(sys.argv) 
if argc == 1:
    fs.append(sys.stdin)
elif argc >= 2:
    try:
        for f in sys.argv[1:]:
            fs.append(open(f,"rU"))
    except IOError:
        print >>sys.stderr,"nl: %s:No such file or directory"%(sys.argv[1])
	sys.exit()
else:
    print >>sys.stderr,"usage: nl [file]"
    sys.exit()

d = {}
for f in fs:
    for l in f:
        words = l.lower().split()
        for w in words:
            if d.has_key(w):
                d[w]+=1
            else:
                d[w]=1
    f.close()

sorted_keys=sorted(d.keys(),key=lambda x:d[x],reverse=True)
print "all: %d"%len(d)

i=0
for k in sorted_keys:
    if i==20:
        break
    print k,": ",d[k]
    i+=1
