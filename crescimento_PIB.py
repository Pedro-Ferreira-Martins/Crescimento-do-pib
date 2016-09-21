#crescimento PIB trienio


def Maior_Crescimento(a):
        #Função que toma uma lista como argumento
		num=range(len(a))
		#isso devolve uma lista com o mesmo numero de itens que o argumento principal
		#essa variavel serve pra usar no for loop ali em baixo. Em vez de len(a), podia usar
		#o int que vem no input, mas achei isso confuso e deixei assim. 
        x=[]
		#Essa lista serve pra armazenar o crescimento de cada ano. Eu tinha feito com um dicionário
		#antes, mas percebi que o dicionário não guarda a ordem dos itens  então não dava pra identificar
		#o ano pra devolver a resposta
        for i in num:
		#esse loop armazena em x as porcentagens de crescimento anuais
                if i==0:
				#como não posso comparar o primeiro ano com o ano anterior, só pus o valor como 0
                        x.append(0)
						#esse metodo acrescenta um valor na ultima posição da lista
                else:
				#é aqui que a magica acontece
                        x.append((a[i]-a[i-1])/a[i-1]*100)
						#ano1 - ano0 dividido pelo ano0 e multiplicado por 100
						#isso insere a porcentagem do ano na lista x
        trienios=[]
		#variavel pra armazenar a media trienal de crescimento
        num=range(len(a)-2)
		#essa é a mesma variavel que eu criei na linha 6. Mudei o valor dela aqui pra excluir os dois ultimos
		#anos pq eles não começam nenhum trienio. E se eu usasse a[i+2] no penultimo item daria um erro de index out of range
        for i in num:
		#aqui eu calculo a media de cada trienio e armazeno em 'trienios'
                trienios.append((x[i]+x[i+1]+x[i+2])/3)
				#soma todas as porcentagens e divide por 3
        maior=max(trienios)
		#A função max() devolve o maior valor em uma lista. armazenei esse valor em 'maior'
        n_ano=trienios.index(maior)
		#As posições dos valores em 'maior'são iguais as dos anos onde começa o respectivo trienio, então eu usei o metodo index()
		#pra dizer qual é a posição do maior valor
        print('A maior media de crescimento foi entre os anos %d e %d: %.1f'%(n_ano,n_ano+2,maior))

casa=[1.89,7.91,1.24,7.92,8.79]
Maior_Crescimento(casa)
