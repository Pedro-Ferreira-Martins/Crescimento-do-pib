#crescimento PIB trienio


def Maior_Crescimento(a):
        num=range(len(a))
        x=[]#{ano:% de cresc}
        for i in num:
                if i==0:
                        x.append(0)
                else:
                        x.append((a[i]-a[i-1])/a[i-1]*100)
        trienios=[]
        num=range(len(a)-2)
        for i in num:
                trienios.append((x[i]+x[i+1]+x[i+2])/3)
        maior=max(trienios)
        n_ano=trienios.index(maior)
        print('A maior media de crescimento foi entre os anos %d e %d: %.1f'%(n_ano,n_ano+2,maior))

casa=[1.89,7.91,1.24,7.92,8.79]
Maior_Crescimento(casa)
