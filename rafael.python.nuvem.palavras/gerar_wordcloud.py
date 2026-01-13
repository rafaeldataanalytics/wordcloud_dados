from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = """
Python Python SQL SQL
Backend APIs REST
Data Analysis Pandas NumPy
ETL Data Pipelines
Web Scraping Automation
Power BI BI Analytics
Excel Data Automation
Git GitHub Version Control
"""

wc = WordCloud(
    width=1000, height=500, background_color="black", colormap="viridis"
).generate(texto)

plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file("wordcloud.png")
