import PIL
import jieba
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class WordCloudPlot():
    def __init__(self):
        self.word_path = "word.txt"
        self.image_path = "img.jpg"
        self.result_path = "result.jpg"
        self.image_text = ""

    def get_words(self):
        image_words = []
        f = open(self.word_path, 'r').read()
        words = list(jieba.cut(f))
        for word in words:
            if len(word) <= 1:
                continue
            image_words.append(word)
        self.image_text = r' '.join(image_words)

    def wc_plot(self):
        path = 'd:/jieba/msyh.ttf'
        alice_mask = np.array(PIL.Image.open(self.image_path))
        wordcloud = WordCloud(font_path=path,
                              background_color="white",
                              margin=5,
                              width=1800,
                              height=800,
                              mask=alice_mask,
                              max_words=2000,
                              max_font_size=60,
                              random_state=42)
        wordcloud = wordcloud.generate(self.image_text)
        wordcloud.to_file(self.result_path)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()

def main():
    wcp = WordCloudPlot()
    wcp.get_words()
    wcp.wc_plot()

if __name__ == '__main__':
    main()