from isOdd import isOdd
from progress.bar import Bar
import time
import emoji

print(emoji.emojize('Python is :thumbs_up:'))
print()
print(isOdd(1))
print(isOdd(2))
print()


bar = Bar('Processing', max=20)
for i in range(20):
    i+=1
    bar.next()
    time.sleep(0.25)
bar.finish()