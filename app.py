from flask import Flask, jsonify, request, render_template

app = Flask(__name__) #inicializa nossa aplicação

# criando listas de lojas
lojas = [
    {
        'name': 'Magazine Luiza',
        'items': [
            {
                'name': 'Notebook Acer',
                'price': 4999
            }
        ]
    }
]

#POST - Recebe dados
#GET - Envia dados de volta

#@app.route('/')
#def home():
#    return render_template('index.html')

#post /loja data: {name :}  - cria uma nova loja
@app.route('/loja', methods=['POST'])
def cria_loja():
    request_data = request.get_json() # dados para solicitar a request são os mesmos do get_json, feitas para o edpoint /loja
    new_loja = { #criando dicionário de dados que serão recebidos
        'name': request_data['name'],
        'items':[]
    }
    lojas.append(new_loja) #salvando a nova loja em lojas
    return jsonify(new_loja) #precisamos retornar uma String, para isso usamos o jsonify

#get /loja/<string:name> - retorna uma loja com determinado nome
#'http://127.0.0.1:5000/loja/name'
@app.route('/loja/<string:name>') #via percorrer as lojas cadastradas buscando por um "nome"
def get_loja(name):
    for loja in lojas:
        if loja['name'] == name: #compara o nome das busca pelo nome da loja
            return jsonify(loja) #se encontrado, retorna a loja
    return jsonify({'message': 'Loja não encontrada!'}) #mensagem de erro

#get /loja - retorna lista de lojas
@app.route('/loja')
def get_lojas():
    return jsonify({'lojas': lojas}) #string vs listas(python)

#post /loja/<name> data: {name :, price :} - cria um item dentro da loja específica
@app.route('/loja/<string:name>/item', methods=['POST'])
def cria_item_na_loja(name):
    request_data = request.get_json()
    for loja in lojas:
        if loja['name'] == name: #compara existencia do nome da loja
            new_item = { #gera o novo item
                'name': request_data['name'],
                'price': request_data['price']
            }
            loja['items'].append(new_item) #salva o item em items
            return jsonify(new_item) #retorna o item
    return jsonify({'message': 'Loja não encontrada!'}) #mensagem de erro



#get /loja/<name>/item data: {name :} - pega o item em uma loja específica
@app.route('/loja/<string:name>/item')
def get_item_na_loja(name):
    for loja in lojas:
        if loja['name']== name:
            return jsonify({'items': loja['items']}) 
    return jsonify({'message': 'Loja não encontrada!'}) #mensagem de erro

#app.run(port=5000)


# Processo padrão o brownser usa o POST para enviar dados e GET para receber dados