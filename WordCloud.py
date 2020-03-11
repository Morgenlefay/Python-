# WordCloud.py
import jieba
import imageio
import wordcloud

# 读取文件
file = open('WordCloud/红楼梦.txt','rt', encoding = 'utf-8')
text = file.read()
file.close()

ls = jieba.lcut(text)
txt = " ".join(ls)

stopwords = {'我们':0, '你们':0, '他们':0, '那里':0, '这里':0, '一个':0} # 噪声词
color_mask =imageio.imread("WordCloud/love.jpeg")

w = wordcloud.WordCloud(font_path = 'WordCloud/msyh.ttf',
                        width = 1000,
                        height = 700,
                        stopwords = stopwords,
                        background_color = 'white',
                        mask = color_mask,
                        max_words = 500)
w.generate(txt)
w.to_file("txt.eps")
