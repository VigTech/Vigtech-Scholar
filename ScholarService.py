#!flask/bin/python
from flask import Flask, jsonify, request
from ScholarAPI import scholarAPI
from arxiv import Arxiv
app = Flask(__name__)

@app.route('/consultaScholar/', methods=['GET'])
def get_taski():
	if request.method == 'GET':
		#Parametros de consulta
		consulta = request.args.get('consulta')
		proyecto = request.args.get('proyecto')
		user = request.args.get('user')
		#Creacion de ScholarAPI
		sch = scholarAPI()
		#Proceso de Descarga
		sch.buscadorSimple(consulta)
		sch.move_files(user, proyecto)
		sch.escribir_docs(user,proyecto)
		return jsonify({'titulos':sch.lista_articulos})

@app.route('/consultaArxiv/', methods=['GET'])
def get_tasko():
	if request.method == 'GET':
		#Parametros de consulta
		consulta = request.args.get('consulta')
		proyecto = request.args.get('proyecto')
		user = request.args.get('user')
		limite = request.args.get('limite')
		#Creacion de ScholarAPI
		#arx = Arxiv()
		#Proceso de Descarga
		arxiv = Arxiv(user, proyecto, limite)
		arxiv.get_arxiv(consulta)
		arxiv.leer_xml()
		#arxiv.move_files("camicasi", "1")
		arxiv.escribir_docs()	
		return jsonify({'titulos':arxiv.lista_articulos})
	
	
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
