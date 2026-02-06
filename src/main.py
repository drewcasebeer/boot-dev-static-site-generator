from htmlnode import HTMLNode
from textnode import TextNode


def main():
    textNode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(textNode)

    htmlNode = HTMLNode(
        "a", None, None, {"href": "https://www.google.com", "target": "_blank"}
    )
    print(htmlNode)


if __name__ == "__main__":
    main()
