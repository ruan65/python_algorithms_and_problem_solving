from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for item in attrs:
            print(f'-> {item[0]} > {item[1]}')

    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag.lower()}')
        for item in attrs:
            print(f'-> {item[0]} > {item[1]}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')


parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())