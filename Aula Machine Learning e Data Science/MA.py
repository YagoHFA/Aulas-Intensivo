import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score



# Importanto base de dados
tabela = pd.read_csv('advertising.csv')

#Exibindo base de dados
print(tabela)

#Exibindoa a correlação dos dados
print(tabela.corr())

#Criando um gráfico 
sns.heatmap(tabela.corr(), cmap="Blues", annot= True)

#Exibindo o gráfico
plt.show()


#Definindo a função dos dados da tabela para previsão
y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]

#Estabelecendo os dados de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)


#Criando as Inteligencia Artificiais
modelo_regressaLinear = LinearRegression()
modelo_arvoredecicao = RandomForestRegressor()


#Treinando as Inteligencias Artificiais
modelo_arvoredecicao.fit(x_treino, y_treino)
modelo_regressaLinear.fit(x_treino, y_treino)


#Testando as Inteligencias Artificiais
previcao_linear = modelo_regressaLinear.predict(x_teste)
previcao_arvore = modelo_arvoredecicao.predict(x_teste)

#Exibindo os resultado dos testes
print(r2_score(y_teste, previcao_linear))
print(r2_score(y_teste, previcao_arvore))

#Criando uma tabela auxiliar 
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previcao Arvore de Decicao'] = previcao_arvore
tabela_auxiliar['Previcao RegressivaLinear'] = previcao_linear


#Criando um gráfico para comparar resultados
sns.lineplot(data = tabela_auxiliar)
plt.show()

#Nova tabela com novos dados para teste
novaTabela = pd.read_csv('novos.csv')
print(novaTabela)


#Testando os novos testes
previcao = modelo_arvoredecicao.predict(novaTabela)

#Resultado dos testes
print(previcao)
