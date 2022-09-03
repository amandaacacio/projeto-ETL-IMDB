# Projeto de ETL com dados do IMDB

Para a elaboração e construção deste projeto, foram utilizados dados disponibilizados pelo site do IMDB referente à todos os títulos de filmes avaliados pelo site. Também utilizamos a página do IMDB que apresenta os 250 filmes mais bem avaliados do portal para a realização do web scraping. Optamos por utilizar os dados da raspagem dos 250 filmes mais bem avaliados e integrar com as informações de cada filme que a página não apresenta.

# Arquitetura

Para a criação da *Arquitetura de Dados* do projeto, utilizamos a ferramenta *Miro*. A Imagem abaixo representa a arquitetura do projeto:

![image](https://user-images.githubusercontent.com/66805067/188272078-89273fa3-d4e4-48f4-b1ec-0819e9cd1d81.png)

https://miro.com/welcome/dG8xa1hMNXJMY1FJYW5vT3N5NTJVSHBwOEd5UEdnelRmZWJNb3c1b3E4SGEzWERvV2NINFZhRTU1MFo4S0gzaXwzMDc0NDU3MzU5NDQxMDMzMzky?share_link_id=687587977900

# Web Scraping

> Atenção: O caminho do "path" deve ser alterado no código.

Para a coleta da primeira fonte de dados (relação dos Top 250 filmes do IMDB) primeiro baixamos a página https://www.imdb.com/chart/top/ utilizando a biblioteca *requests* do Python. 
A biblioteca *requests* fará uma solicitação GET ao servidor, que fará o download dos conteúdos HTML da página solicitada para nós. 
Com isso, utilizamos a biblioteca *BeautifulSoup* para analisar o conteúdo HTML e extraimos o conteúdo de cada nível de tag. Após isso, temos um dataframe com os dados raspados da página e exportamos como o csv "web_scraping_imdb.csv" na pasta Datasets.

# ETL

> Atenção: O caminho do "path" deve ser alterado no código.

Após a raspagem dos dados do site do IMDB com os 250 filmes mais bem avaliados, passamos para a extração da outra fonte de dados do projeto. Utilizamos a biblioteca *wget* do Python para realizar o download dos dados disponibilizados no site https://datasets.imdbws.com/.
Para esse projeto, apenas o arquivo title.basics é baixado, um conjunto de dados contido em um arquivo formatado de valores separados por guias (TSV) no conjunto de caracteres UTF-8.

![image](https://user-images.githubusercontent.com/66805067/188269886-5b219a12-099e-4616-8352-af5fd5dc38c3.png)

Após baixado o arquivo .tsv, o descompactamos na pasta Datasets utilizando as bibliotecas *gzip* e *shutil*. E seguimos com a realização da interseção das duas fontes e o ETL das mesmas até chegar no output "imdb_top250.csv".

# Business Intelligence

Consumimos no *Power Bi* o arquivo consolidado dos 250 Top Filmes avaliados do IMDB que já passou pelo processo de ETL, extraindo a informação de Score dos filmes por Gênero (Podendo ser utilizado a minutagem, ano de lançamento, etc).
