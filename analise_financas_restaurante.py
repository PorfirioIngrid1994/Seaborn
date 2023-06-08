import seaborn as sns
import matplotlib.pyplot as plt

# Definição de tema do gráfico (interface):
sns.set_theme(style='darkgrid')

# Base de dados:
# É utilizada uma base dados do próprio seaborn
base_dados = sns.load_dataset('tips')  # base de dados de um restaurante
base_dados.head()

base_dados.rename(columns={
    'total_bill': 'TotalConta',
    'tip': 'Gorgeta',
    'sex': 'Sexo',
    'smoker': 'Fumante',
    'day': 'DiaSemana',
    'size': 'PessoasMesa'
}, inplace=True)

print(base_dados)

# Gráfico1 Relplot
# sns.regplot(x='TotalConta', y='Gorgeta', data=base_dados)

# # Gráfico2 lmplot
# sns.lmplot(x='TotalConta', y='Gorgeta', data=base_dados, hue='Sexo')

# Gráfico3 lineplot
# sns.lineplot(x='TotalConta', y='Gorgeta', data=base_dados)

# # Gráfico3.1 lineplot - Passando outro parâmetro
# sns.lineplot(x='TotalConta', y='Gorgeta', data=base_dados, hue='Fumante')

#Gráfico 4 - Histplot 

# sns.histplot(data=base_dados, x = 'TotalConta')

#Gráfico 4.1 - Histplot mais um parâmetro 

# sns.histplot(data=base_dados, x = 'TotalConta', hue='Fumante')

#Gráfico 5- Barplot

# sns.barplot(data=base_dados, x='Sexo', y='TotalConta', hue='Fumante')

#Gráfico 6 - pairplot

# sns.pairplot(base_dados)

#Gráfico 6.1 - Mais um parâmetro 

# sns.pairplot(base_dados, hue='Sexo')

#Gráfico 7 - Boxplot

# sns.boxplot(data=base_dados, x= 'DiaSemana', y='TotalConta')

#Gráfico 7.1 - Boxplot

sns.boxplot(data=base_dados, x= 'DiaSemana', y='TotalConta', hue='Sexo')

# Exibir o gráfico
plt.show()
