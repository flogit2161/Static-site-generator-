from textnode import TextNode, TextType

def main():
    dummynode = TextNode("This is some anchor text", TextType.LINK, "http://example.com")
    print(dummynode)

if __name__ == "__main__":
    main()  