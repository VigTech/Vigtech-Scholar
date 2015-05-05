import scholar
import os
import json
import urllib
REPOSITORY_DIR = "/home/vigtech/shared/repository/"
class scholarAPI:
	lista_articulos=[]
	lista_docs=[]
	def __init__(self):
		self.lista_articulos=[]
		self.lista_docs=[]
		print REPOSITORY_DIR
	def buscadorSimple(self,frase):
		#nombre_directorio=str(id_user)+ "."+ str(id_proyecto)
		querier=scholar.ScholarQuerier()
		
		settings=scholar.ScholarSettings()
		
		query=scholar.SearchScholarQuery()

		query.set_phrase(frase)
		query.set_num_page_results(40)

		querier.send_query(query)
		scholar.getArticles(querier)

		articles=querier.articles
		articulos=self.getArticlesDict(articles)
		#MOVER ARTICULOS A CARPETA TMP
		#if articulos is not None:
		#	moveFiles()
		#	indexarArchivos()
		return articulos
	
	def buscadorAvanzado(self,frase,words, autor, after, before):
		#nombre_directorio= str(id_user)+ "."+ str(id_proyecto)
		querier=scholar.ScholarQuerier()
		settings=scholar.ScholarSettings()
		query=scholar.SearchScholarQuery()
		if frase != "":
			query.set_phrase(frase)
		if words != "":
			query.set_words(words)
		if autor != "":
			query.set_author(autor)
		if after !="" or before != "":
			query.set_timeframe(after, before)

		query.set_num_page_results(40)
		querier.send_query(query)
		scholar.getArticles(querier)
		articles=querier.articles
		

		articulos=self.getArticlesDict(articles)

		return articulos
		
	def getArticlesDict(self,articles):
		articulos=[]
		for art in articles:

			titulo=art.attrs["title"][0]
			#print(titulo)
			url=art.attrs["url"][0]
			url_pdf=art.attrs["url_pdf"][0]
			#state =art.attrs['state'][0]
			#testFile=urllib.URLopener()
			if url_pdf is not None:
				
				newArt={'titulo': titulo, 'url':url, 'url_pdf':url_pdf}
				articulos.append(newArt)
				if titulo != "NO ACCESIBLE":
					self.lista_articulos.append(titulo)
				print (newArt['titulo']+ '\n')
					
				
		return articulos
	
	def move_files(self,user, nombreProyecto):
		rutaProyecto = str(user) + "." + str(nombreProyecto)
		
		for art in self.lista_articulos:
			if art != "NO ACCESIBLE":
				self.lista_docs.append(art + ".pdf")
				
		for art in self.lista_docs:
			nombre = art.replace(" ", "\\ ")
			os.system("mv -f " + nombre + " " +REPOSITORY_DIR + rutaProyecto + "/")
	
	def escribir_docs(self, user, proyecto):
		pdfs = open(REPOSITORY_DIR + str(user) + "." + str(proyecto) + "/" + "docs.txt", "a")
		for pdf in self.lista_docs:
			if pdf is not None:
				pdfs.write(pdf + '\n')
		pdfs.close()
		
#sch = scholarAPI()
#sch.buscadorSimple("Named Entity Recognition")
