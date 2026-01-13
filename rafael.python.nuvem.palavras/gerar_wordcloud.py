from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Abre o arquivo de texto e lê todo o conteúdo
# encoding="utf-8" evita problemas com acentos
with open("tecnologias.txt", encoding="utf-8") as arquivo:
    texto = arquivo.read()


# Cria a nuvem de palavras com configurações visuais
wc = WordCloud(
    width=1000, height=500, background_color="black", colormap="viridis"
).generate(texto)


# Exibe a nuvem de palavras
plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()


# Salva a imagem gerada em arquivo PNG
wc.to_file("wordcloud.png")
