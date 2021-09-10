from flask import Flask, request
import json
import pandas as pd 

def cargar_datos(ruta):
    resultado=pd.read_json(ruta)
    print(resultado)
    return resultado

app=Flask(__name__,template_folder='Template')

@app.route('/',methods=['GET'])
def welcome():
    return 'Hola mundo'

@app.route('/pokemon/',methods=['GET'])
def obtener_todos_los_pokemones():
    pokemon=cargar_datos(ruta)
    return json.loads(pokemon[['#','Name','Type 1','Type 2','Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary']].to_json(orient='index'))

@app.route('/pokemon/<string:Name>',methods=['GET'])
def obtener_pokemon(Name):
    pokemon=cargar_datos(ruta)
    res=pokemon.loc[(pokemon['Name']==Name)]
    return json.loads(res.to_json(orient='index'))

@app.route('/pokemon/ingresa',methods=['GET','POST'])
def registrar_pokemon():
    pokemon=cargar_datos(ruta)
    n=pokemon.shape[0]
    identidad=int(request.args.get('#'))
    nombre=request.args.get('Name')
    tipos=list(request.args.get('Type 1').split(','))
    tipos2=list(request.args.get('Type 2').split(','))
    Total=list(request.args.get('Total').split(','))
    HP=list(request.args.get('HP').split(','))
    Ataque=list(request.args.get('Attack').split(','))
    Defensa=list(request.args.get('Defense').split(','))
    Spataque=list(request.args.get('Sp. Atk').split(','))
    Spdefensa=list(request.args.get('Sp. Def').split(','))
    Velocidad=list(request.args.get('Speed').split(','))
    Generacion=list(request.args.get('Generation').split(','))
    Legendario=list(request.args.get('Legendary').split(','))
    pokemon.loc[n]=[identidad,nombre,tipos,tipos2,Total,HP,Ataque,Defensa,Spataque,Spdefensa,Velocidad,Generacion,Legendario]
    pokemon.to_json(r'pkmon.json')
    return 'Se inserto pokemon exitosamente'


if __name__=='__main__':
    ruta='pkmon.json'
    app.run(host='0.0.0.0',port=9000,debug=True)