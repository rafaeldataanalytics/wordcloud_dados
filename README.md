# ☁️ Nuvem de Palavras com Python

Este projeto demonstra a criação de uma **WordCloud (nuvem de palavras)** utilizando **Python**, com foco em representar visualmente tecnologias, ferramentas e conceitos relacionados a **back-end e análise de dados**.

A nuvem foi gerada de forma programática, reforçando o uso de Python para **automação**, **tratamento de dados** e **geração de artefatos visuais**.

---

## 🧠 WordCloud de Tecnologias

![WordCloud](Assets/wordcloud_1.png)

---

## 🔍 Tecnologias e Conceitos Representados

A WordCloud destaca conhecimentos como:

- **Python e SQL** aplicados ao desenvolvimento back-end e dados  
- **Análise de dados** com Pandas e NumPy  
- **ETL e automação de processos**  
- **APIs e integração de sistemas**  
- **Web Scraping** para coleta de dados  
- **Excel e Power BI** como apoio à análise e BI  
- **Git e GitHub** para versionamento e organização de projetos  

---

## 🚀 Objetivo do Projeto

O objetivo deste repositório é demonstrar:
- uso prático de bibliotecas Python
- organização de projeto
- geração de imagens a partir de código
- publicação profissional no GitHub

Este projeto faz parte do meu processo de evolução como **desenvolvedor back-end com foco em dados**.

---

## 🛠️ Como foi gerado

A WordCloud foi criada utilizando:
- Python
- Biblioteca `wordcloud`
- Biblioteca `matplotlib`

O script está disponível neste repositório para reprodução e estudo.


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Abre o arquivo de texto e lê todo o conteúdo
# encoding="utf-8" evita problemas com acentos
with open("tecnologias.txt", encoding="utf-8") as arquivo:
    texto = arquivo.read()


# Cria a nuvem de palavras com configurações visuais
wc = WordCloud(
    width=1000,
    height=500,
    background_color="black",
    colormap="viridis"
).generate(texto)


# Exibe a nuvem de palavras
plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()


# Salva a imagem gerada em arquivo PNG
wc.to_file("wordcloud.png")

