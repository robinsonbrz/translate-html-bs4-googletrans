
from googletrans import Translator
from bs4 import BeautifulSoup, Tag, NavigableString
import os


def find_html_files(root_dir, file_to_search):
    root_dir = './'
    file_to_search = '.html'
    html_files_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_to_search):
                html_files_list.append(os.path.join(root, file))
    return html_files_list


def translate_text(html_file, language_to):
    print("\nTranslating: ", html_file)
    html = open(html_file, 'rb')
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(["p","ul","ol","h1","h2","h3","h4","h5","h6","td", \
                        "button","label","div","a", "span", "i", "strong", \
                        "title", "li"])
    translator=Translator()

    for tag in tags:
        for i in range(0, len(tag.contents)):
            if type(tag.contents[i])== NavigableString and len(tag.contents[i]) > 1:
                translation=translator.translate(tag.contents[i],dest=language_to).text
                tag.find(string=str(tag.contents[i])).replace_with(translation)
    
    with open(html_file, "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))
    
    html.close()
    f_output.close()


if __name__ == "__main__":
    language_to = 'hi'
    print("Starting script")
    list_html_to_translate = find_html_files(root_dir = './', file_to_search = '.html')
    [translate_text(i, language_to) for i in list_html_to_translate ]
    print(len(list_html_to_translate))
