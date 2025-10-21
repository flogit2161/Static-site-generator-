from textnode import TextNode, TextNodeType

def main():
    dummynode = TextNode("This is some anchor text", TextNodeType.LINK_TEXT, url="http://example.com")
    print(dummynode)

if __name__ == "__main__":
    main()  