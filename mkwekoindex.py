# coding: utf-8

import xml.etree.ElementTree as ET
import html
import sys

class paperInfo:
    def __init__(self, title):
        self.title = title
        self.authors = []
        self.affils = []

    def addAuthor(self, name):
        self.authors.append(name)

    def addAffil(self, affil):
        self.affils.append(affil)

    def setFile(self, filen):
        self.filen = filen

    def setAbst(self, abst):
        self.abst = abst

    def setPages(self, pages):
        self.pages = pages

    def output(self):
        print('<div class="paper">')
        print('<a target="_blank" href="'+self.filen+'">'+html.escape(self.title)+'</a> ')
        print(' <span class="pages"> pp. ' + self.pages + '</span><br>')
        
        for i in range( len(self.authors) ):
            print('<span class="author">', end="")
            print(self.authors[i]+" ", end="")
            try:
                print("（"+self.affils[i]+"）")
            except:
                None
            print("</span> ")
        
        print('<div class="abst">'+html.escape(self.abst)+'</div>')
        print('</div>')
        print('')

        
args = sys.argv

tree = ET.parse(args[1])
root = tree.getroot()

papers = [] # paper list
pinfo = None
booktitle = None
typestr = None
copyrightstr = None

for child in root:
    if (child.tag == "repository_item"):
        pinfo = paperInfo( child.attrib['title'] )
        papers.append( pinfo )
    if (child.tag == "repository_file"):
        pinfo.setFile(child.attrib['file_name'])
    if (child.tag == "repository_personal_name"):
        pinfo.addAuthor(child.attrib['family'] + " " + child.attrib['name'])
# 著者所属モードと、論文抄録モードを、きりかえる
    if (child.tag == "repository_item_attr_type"):
        typestr = child.attrib['attribute_name'] 
        
    if (child.tag == "repository_item_attr"):
        if (typestr == "著者所属"):
            pinfo.addAffil(child.attrib['attribute_value'])
        elif (typestr == "論文抄録"):
            pinfo.setAbst(child.attrib['attribute_value'])
            
    if (child.tag == "repository_biblio_info"):
        pinfo.setPages(child.attrib['start_page']+" - "+child.attrib['end_page'])
        booktitle = child.attrib['biblio_name']

    if (child.tag == "repository_license_master"):
        copyrightstr = child.attrib['license_notation']

html0 = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>
'''[1:-1]

html1 = '''
</title>
<style>
.paper {
  margin-top: 20px;
  margin-left: 5px;
}
.pages {
  font-size: x-small;
}
.author {
  margin-left: 12px;
  margin-right: 0px;
  font-size: small;
}
.abst {
  margin-top: 5px;
  margin-left: 14px;
  font-size: x-small;
}
footer {
  color: #777;
  text-align: center;
  font-size: small;
}
</style>
</head>
<body>
'''[1:-1]

print(html0)
print(booktitle)
print(html1)

print("<h1>"+booktitle+"</h1>")

# ファイル名で並び替える
sorted_papers = sorted(papers, key=lambda pi: pi.filen)

for p in sorted_papers:
    p.output()

print('<hr><footer>'+copyrightstr+'<br>')
print('This index file is generated by <a href="https://github.com/miuramo/weko_index">WEKO_INDEX</a>')
print('</footer>')
html2 = '''
</body>
</html>
'''[1:-1]

print(html2)

    

        
        

        

    

