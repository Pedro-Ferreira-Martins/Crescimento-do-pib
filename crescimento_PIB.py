#crescimento PIB trienio


def Maior_Crescimento(a):
	num=range(len(a)-2)
	x={}#{porcentagem de a[i]:a[i]}
	for i in num:
		dif_=a[i]-a[i+2]
		porcentagem=dif_/(a[i]/100)
		x[-porcentagem]=a[i]
	print(x)
	b=max(x)
	ano1=a.index(x[b])+1
	ano2=ano1+2
	print('A maior media de crescimento foi entre os anos %d e %d: %d'%(ano1,ano2,b))

casa=[4.0,1.72,3.67,9.66,3.05]
Maior_Crescimento(casa)
