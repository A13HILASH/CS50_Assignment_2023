import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search('(.+)src="https?://(?:www\.)?youtube\.com/embed/(.+?)"',s)
    if url:
        return "https://youtu.be/" + url.group(2)
    
if __name__ == "__main__":
    main()