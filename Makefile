## WEKO_INDEX Makefile 
##
## usage:
##
## (1) Put zip files (ex. export.zip, export (1).zip ,... )
##     on the same directory.
##
## (2) Just make.
## 
## $ make          create index.html and extract pdf files from zip files.
## 
## $ make pdf      extract pdf files from zip files.

all: index.html pdf clean

index.html: tmp2.xml
	python3 mkwekoindex.py tmp2.xml > index.html

tmp2.xml : tmp1.xml
	echo "<export>" > tmp2.xml && \
	cat tmp1.xml >> tmp2.xml && \
	echo "</export>" >> tmp2.xml
# wrap by <export> and </export> for further parsing

tmp1.xml: tmp0.xml
	grep -v "xml version=" tmp0.xml | grep -v "export>" > tmp1.xml
# remove declaration and <export> / </export> 

tmp0.xml:
	@for i in *.zip ; do echo $$i ; unzip -p "$$i" import.xml >> tmp0.xml ; done;
# extract all import.xml of the zip files, and concatenate.

clean:
	rm tmp*.xml

pdf:
	@for i in *.zip ; do echo $$i ; yes | unzip "$$i" ; done; \
	rm import.xml
# extract all pdf files

cleanpdf:
	rm *.pdf

### cleanzip:
### 		rm *.zip
### (if you want to delete zip files, uncomment this part.)


