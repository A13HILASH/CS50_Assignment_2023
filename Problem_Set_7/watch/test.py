import re
import sys
s=input("HTML: ")

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"
#allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
url = re.search('.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)"',s)
print(url)

if url:
    link= "https://youtu.be/" + url.group(1)
    print(link)