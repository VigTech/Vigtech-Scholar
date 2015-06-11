#!flask/bin/python
from flask import Flask, jsonify, request
from arxiv import Arxiv

app = Flask(__name__)

@app.route('/consultaArxiv/', methods=['GET'])
def get_taski():
	if request.method == 'GET':
		#Parametros de consulta
		consulta = request.args.get('consulta')
		proyecto = request.args.get('proyecto')
		user = request.args.get('user')
		#Creacion de ScholarAPI
		#arx = Arxiv()
		#Proceso de Descarga
		arxiv = Arxiv(user, proyecto)
		arxiv.get_arxiv(consulta)
		arxiv.leer_xml()
		#arxiv.move_files("camicasi", "1")
		arxiv.escribir_docs()	
		return jsonify({'titulos':arxiv.lista_articulos})
	
	
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
