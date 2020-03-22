import uuid
from datetime import datetime, date

from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

MATRICULAS_1 = [
    {
        'matricula': '23-53-UI',
        'hora_entrada': '23:10',
        'hora_saida': ''
    },  
    {
        'matricula': '43-49-TE',
        'hora_entrada': '23:10',
        'hora_saida': ''
    },
    {
        'matricula': 'BE-29-BE',
        'hora_entrada': '23:10',
        'hora_saida': '23:10'
    }
]
MATRICULAS = [
    
]
SENSORS = [

]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def removeSensor(sensor_id):
    for sensor in SENSORS:
        if sensor['id'] == sensor_id:
            SENSORS.remove(sensor)
            return True
    return False   

def removeMatricula(matricula_id):
    for matricula in MATRICULAS:
        if matricula['matricula'] == matricula_id:
            MATRICULAS.remove(matricula)
            return True
    return False   

@app.route('/matriculas', methods=['GET'])
def all_matriculas():
    response_object={'status':'success'}
    response_object['matriculas']=MATRICULAS
    return jsonify(response_object)

@app.route('/sensors', methods=['GET'])
def all_sensors():
    response_object={'status': 'success'}
    response_object['sensors']=SENSORS
    return jsonify(response_object)


@app.route('/sensors/<sensor_id>', methods =['DELETE'])
def singleSensor(sensor_id):
    response_object = {'status':'success'}
    if request.method == 'DELETE':
        removeSensor(sensor_id)
        response_object['message'] = 'Sensor removed'

    return jsonify(response_object)

@app.route('/matriculas/<matricula>', methods =['DELETE'])
def singleMatricula(matricula):
    response_object = {'status':'success'}
    if request.method == 'DELETE':
        removeMatricula(matricula)
        response_object['message'] = 'Matricula removed'

    return jsonify(response_object)

def currentTime():
    day = date.today()
    hours = datetime.now()
    current_time = hours.strftime("%H:%M:%S")
    current_day = day.strftime("%d/%m/%Y")
    return current_time


@app.route('/postMatricula', methods = ['POST'])
def postJsonMatricula():
    response_object={'status': 'success'}
    post_data =request.get_json()
    time = currentTime()

    retorno = checkMatriculaStatus(post_data.get('matricula'))
    if retorno == 0:
        MATRICULAS.append({
            'matricula': post_data.get('matricula'),
            'hora_entrada': time,
            'hora_saida': ''
        })

    return jsonify(response_object)

def checkMatriculaStatus(matricula):
    # print("matricula a ser  analisada é " + matricula)
    time = currentTime()
    for m in MATRICULAS:
        if m['matricula']==matricula and m['hora_saida'] == "":
            m.update({'hora_saida': time})
            return 1
    
    return 0
        

def checkID_Status(id, estado):
    # iterar sobre a lista
    for s in SENSORS:
        #Se o ID recebido for igual ao id existente, iremos analisar o estado
        if str(s['id'])==str(id):
    
            #Se o estado for o mesmo, não temos de fazer nada -> retorna 0
            if s['estado']=='LIVRE' and estado=='0':
                return 0
            elif s['estado']=='OCUPADO' and estado=='1':
                return 0
            elif s['estado'] =='LIVRE' and estado=='1':       #Se o estado for diferente, temos de fazer alteração -> retorna 1
                s.update({'estado':'OCUPADO'})
                return 1
            elif s['estado'] =='OCUPADO' and estado=='0': 
                s.update({'estado':'LIVRE'})
                return 1
            else:            # Em caso de erro retorna -2
                return -2
            
    return -1


@app.route('/postSensor', methods = ['POST'])
def postJsonSensors():
    response_object={'status': 'success'}
    post_data =request.get_json()

    response = checkID_Status(post_data.get('id'), post_data.get('estado'))

    if response == -1:
        if post_data.get('estado') == '0':
            SENSORS.append({
                'id': post_data.get('id'),
                'estado': 'LIVRE'
            })
        elif post_data.get('estado') == '1':
            SENSORS.append({
                'id': post_data.get('id'),
                'estado': 'OCUPADO'
            })  
        else:
            SENSORS.append({
                'estado': post_data.get('id')
            })  

    return jsonify(response_object)



if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)
