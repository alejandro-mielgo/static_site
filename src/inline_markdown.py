import re


from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    #if its a special type, append it directly
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":  #si el simbolo objetivo es el primer caracter, se crea una cadena vacía
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text:str) -> list[tuple[str,str]]:

    texts:tuple = tuple(re.findall(r"\!\[(.*?)\]",text))
    links:tuple = re.findall(r"\((.*?)\)",text)
    return list(zip(texts,links))


def extract_markdown_links(text:str) -> list[tuple[str,str]]:

    texts:tuple = tuple(re.findall(r"\[(.*?)\]",text))
    links:tuple = re.findall(r"\((.*?)\)",text)
    return list(zip(texts,links))


def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes:list=[]

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        else:
            original_text = old_node.text
            images = extract_markdown_images(original_text)
            if len(images) == 0:
                new_nodes.append(old_node)  # no hay imágenes en el texto analizado, lo añado a la solución
                continue
            else:
                for image in images :
                    sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                    if len(sections) !=2:
                        raise ValueError('Invalid markdown')
                    
                    if sections[0] != '':
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    
                    new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))

                    original_text = sections[1]
                
                if original_text != '':

                    new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



if __name__=="__main__":

   

    node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
