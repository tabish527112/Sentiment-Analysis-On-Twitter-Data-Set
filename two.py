def cleaning():
    a=open('twitterout.txt')
    lines= a.readlines()
    a.close()
    wr=open('twitterclean.txt','a')
    for line in lines:
	strt=line.find('"text":"')
	end=line.find('"',strt+9)
	tweet=line[strt+8:end]
	wr.write(tweet+'\n\n')
    wr.close()

def processing():
    a=open('afin.txt')
    b=a.readlines()
    n=len(b)
    a.seek(0)
    d={}
    for i in range(0,n):
        b=a.readline()
        b=b.replace('\t',' ')
        b=b.replace('\n','')
        b=b.split(' ')
        l=len(b)
        p=b[0]
        if(l>2):
            p=p+' '+b[1]
        q=b[l-1]
        if p in d.keys():
            d[p]=d[p]+q
        else:
            d[p]=q
    x=open('twit_Reac_0.txt','w')
    for i in d:
        x.write(i)
        x.write('                    ')
        x.write(d[i])
        x.write('\n')
    x.close()
    a.close()
    a=open('twitterclean.txt')
    b=a.readlines()
    n=len(b)
    a.seek(0)
    z=open('reaction_0.txt','w')
    for i in range(0,n):
        c=0
        b=a.readline()
        b=b.split(' ')
        for j in b:
            if j in d.keys():
                p=int(d[j])
                c=c+p
        if(c>0):
            z.write('Positive')
        if(c<0):
            z.write('Negative')
        if(c==0):
            z.write('Neutral')
        z.write('\t')
        z.write(str(c))
        z.write('\n')
    z.close()
    a.close()
            
        
    
def SATD():
    cleaning()
    processing()
    y=open("reaction_0.txt",'r')
    a=y.readlines()
    n=len(a)
    y.seek(0)
    sp=0
    sn=0
    s0=0
    for i in  range(0,n):
        a=y.readline()
        a=a.replace("\t"," ")
        a=a.replace("\n","")
        a=a.split()
        if(a[0]=="Positive"):
            sp=sp+1
        if(a[0]=="Negative"):
            sn=sn+1
        if(a[0]=="Neutral"):
            s0=s0+1;
    x=open("result.txt",'w')
    x.write("Neutral tweets are ")
    x.write(str(s0))
    x.write("\n")
    x.write("Positive tweets are ")
    x.write(str(sp))
    x.write("\n")
    x.write("Negative tweets are ")
    x.write(str(sn))
    x.write("\n")
    x.close()
    y.close()
    import matplotlib.pyplot as plt
 
# Data to plot
    labels = 'Neutral', 'Positive', 'Negative'
    sizes = [s0, sp, sn]
    colors = ['white', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # explode 1st slice
 
# Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
    plt.axis('equal')
    plt.show()

SATD()
