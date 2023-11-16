# make rimes
def rimes(arg):
    separation_index=[]
    arg=arg.split(" ")
    i=0
    l=[]
    while i != len(arg):
        l.append(arg[i][-2:])
        i=i+1
    i=0
    word=l[9]
    x=10
    while i != len(l):
        if i > x:
            if l[i]==l[x-1]:
                print("rimme trouvée")
                separation_index.append(i)
                x=1
        i=i+1
    #with usage of separation index find index of rimes dand make \n
    i=0
    while i != len (separation_index):
        arg.insert (separation_index[i],"\n")
        i=i+1
    arga=" ".join(arg)
    return arga
wordss="mon nom est bizarre mais la kales haha bahba nicolas as loli popi how to do you cant have it and"
translate=rimes(wordss)
print(translate)