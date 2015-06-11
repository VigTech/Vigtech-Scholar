from urllib2 import urlopen, quote
import urllib
from xml.dom import minidom
from xml.etree import ElementTree as ET
import os

"""
url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
data = urllib.urlopen(url).read()
print data
"""
REPOSITORY_DIR="/home/vigtech/shared/repository/"
class Arxiv:
	lista_articulos=[]
	lista_docs=[]
	dirp= ""
	limite = 0
	def __init__(self, user, proyecto, limite):
		
		self.lista_articulos=[]
		self.lista_docs=[]
		self.dirp= str(user)+"." + str(proyecto)
		self.limite = limite
	
		
	def get_arxiv(self,query):
		consulta = quote(query)
		url = 'http://export.arxiv.org/api/query?search_query=all:'+ consulta + '&start=0&max_results=' + str(self.limite)
		print url
		data = urllib.urlopen(url).read()
		salida = open(REPOSITORY_DIR + self.dirp +"/salida.xml", "w")
		salida.write(data)
		salida.close()
		print data

	def leer_xml(self):
		#dirp= str(user) + "." + str(proyecto)
		f=open(REPOSITORY_DIR + self.dirp +"/salida.xml","r")
		tree = ET.parse(f)
		root = tree.getroot()
		print root.tag
		
		for child in root:
			for link,title in zip(child.findall("{http://www.w3.org/2005/Atom}link"), child.findall("{http://www.w3.org/2005/Atom}title")):
				tipo = link.get("type")
				print tipo
				titulo =  title.text.strip().replace("\n", " ")+ ".pdf"
				print titulo
				if tipo == "text/html":
					url = link.get("href").replace("abs","pdf") + ".pdf"
					
					try:
						#print("Descargando: " + nameFile)
						testFile=urllib.URLopener()
						testFile.retrieve(url, REPOSITORY_DIR+ self.dirp + "/"+ titulo)
						print("Descarga Exitosa!")
						self.lista_articulos.append(titulo)
						#art.setitem('state', 'DESCARGADO')
					except Exception as error:
						print "Error Descargando"
	
	def escribir_docs(self):
		pdfs = open(REPOSITORY_DIR + self.dirp + "/" + "docs.txt", "a")
		for pdf in self.lista_articulos:
			if pdf is not None:
				pdfs.write(pdf + '\n')
		pdfs.close()
		
	"""	
	count = 0
	for node in tree.iter():
		titulo = ""
		if node.tag =="{http://www.w3.org/2005/Atom}title":
			titulo = node.text.strip() + ".pdf" 
			#print titulo
		if node.tag =="{http://www.w3.org/2005/Atom}link":
			print titulo
			if node.get("type") == "application/pdf":
				print node.tag
				print node.get("href")
				
				
				try:
					#print("Descargando: " + nameFile)
					#testFile=urllib.URLopener()
					#testFile.retrieve(node.get("href") + ".pdf",titulo)
					#testFile.retrieve(node.get("href") + ".pdf", titulo)
					print("Descarga Exitosa!")
					#art.setitem('state', 'DESCARGADO')
					count +=1
				except Exception as error:
					print "Error Descargando"


	"""
		
#arxiv = Arxiv("camicasi", "1")
#arxiv.get_arxiv("Software Engineering")
#arxiv.leer_xml()
#arxiv.move_files("camicasi", "1")
#arxiv.escribir_docs()	
#get_arxiv("Heart")
#leer_xml()
#testFile=urllib.URLopener()
#testFile.retrieve("http://arxiv.org/pdf/1303.0445v1.pdf","prueba.pdf")
#get_arxiv("Artificial Intelligence")
