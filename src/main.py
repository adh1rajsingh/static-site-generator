from textnode import TextType, TextNode


def main():
    node = TextNode("This is bold text", TextType.BOLD, "https://www.example.com")
    print(node)

if __name__ == "__main__":
    main()