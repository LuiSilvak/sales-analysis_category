# Análise de Vendas por Categoria

## Descrição

Este projeto tem como objetivo analisar as vendas de um conjunto de dados e categorizar os produtos para identificar padrões de desempenho. A análise foca em examinar o total de vendas por categoria, visualizar a contribuição de cada uma para as vendas totais e destacar as categorias que apresentam melhor desempenho.

## Funcionalidades

1. Importação de dados de vendas em formato CSV.
2. Cálculo do total de vendas por categoria.
3. Visualização gráfica das categorias com maior e menor contribuição para as vendas.
4. Geração de insights sobre o desempenho das categorias de produtos.
5. Possibilidade de exportar os resultados em formato CSV.

## Pré-requisitos

1. Certifique-se de ter os seguintes requisitos instalados no seu ambiente:

    - Python 3.7 ou superior.
    - Bibliotecas necessárias:
        - pandas
        - matplotlib
        - seaborn

2. Você pode instalar as dependências utilizando o comando:

```bash
    pip install pandas matplotlib seaborn
```

## Como Usar

1. Clone este repositório:

```bash
    git clone https://github.com/LuiSilvak/sales-analysis_category.git
    cd sales-analysis_category
```
2. Certifique-se de ter um arquivo CSV contendo os dados de vendas. O arquivo deve conter, no mínimo, as seguintes colunas:

    Categoria
    Produto
    Vendas

3. Exemplo de formato do arquivo:

```bash
    Categoria,Produto,Vendas
    Eletrônicos,Smartphone,1200
    Roupas,Camiseta,300
    Alimentos,Arroz,500
    Eletrônicos,Laptop,800
```
4. Execute o script principal:

```bash
    python sales-analysis_category.py
```

5. Visualize as saídas no console e nos gráficos gerados.

## Exemplo de Saída

1. Estatísticas Sumarizadas:

```bash
    Total de Vendas por Categoria:
    Eletrônicos: 2000
    Roupas: 300
    Alimentos: 500
```

2. Gráficos Gerados:
    - Gráfico de barras mostrando as vendas por categoria.
    - Gráfico de pizza representando a contribuição percentual de cada categoria.

## Estrutura do Projeto

```bash
    analise-vendas-por-categoria/
    │
    ├── analise_vendas.py            # Script principal
    ├── exemplos/
    │   └── exemplo_vendas.csv       # Exemplo de arquivo de dados
    ├── README.md                    # Documentação do projeto
    └── requirements.txt             # Dependências do projeto
```
## Expansões Futuras

1. Análise temporal das vendas por categoria (ex.: vendas por mês).
2. Inclusão de previsão de vendas futuras com base em dados históricos.
3. Integração com bancos de dados para análise em tempo real.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
