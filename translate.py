from googletrans import Translator
from bs4 import BeautifulSoup, Tag,NavigableString

html = open('index2.html', 'rb')
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all(["p","ul","ol","h1","h2","h3","h4","h5","h6","td","button","label","div","a", "span", "i", "strong"])
translator=Translator()
def callcon(t, tag):
    for i in range(0, len(t)):
        
        if type(t[i])== NavigableString:
            # import ipdb; ipdb.set_trace()
            if len(t[i])>1:
                translation=translator.translate(t[i],dest="hi").text
                new_text = tag.find(string=str(t[i])).replace_with(translation)
                print(new_text)
                print(translation)
                print()
                #og=og.replace(str(t[i]),"suneri")
                #return og
        else:
            #print(t[i].contents)
            #print(og)
            # print("Estamos no else: ", t[i])
            # callcon(t[i].contents,tag)
            pass
for tag in tags:
    #constr="".join(str(e) for e in tag.contents)
    #print(constr)
    callcon(tag.contents, tag)
with open("output2.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))
