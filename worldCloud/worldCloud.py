import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pdftotext
import numpy as np
from PIL import Image # converting images into arrays
import random

# Load your PDF
with open("D:/School/ACM 476/DataBI.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open('DataBI.txt', 'w') as f:
    f.write("\n\n".join(pdf))
    
textFile = open('DataBI.txt', 'r').read()

#mask = np.array(Image.open('beyaz.png'))

stopwords = set(STOPWORDS)

# instantiate a word cloud object
wordcloud = WordCloud(
    background_color='white',
    width = 1920,
    height = 1080,
    max_words=500,
#    mask = zatanna_mask,
    stopwords=stopwords
)

'''
# A function to create grey colours.
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
'''
# generate the word cloud
wordcloud.generate(textFile)

# To generate colors like in the mask's.
#image_colors = ImageColorGenerator(mask) 

# display the word cloud
plt.figure(figsize=(25, 15))
#plt.imshow(wordcloud.recolor(color_func = image_colors), interpolation='bilinear')
#plt.imshow(wordcloud.recolor(color_func = grey_color_func), interpolation='bilinear')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.savefig('dataminingWordCloud.png')
plt.show()