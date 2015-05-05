#!flask/bin/python
from flask import Flask, jsonify, request
from ScholarAPI import scholarAPI

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
	
	
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
