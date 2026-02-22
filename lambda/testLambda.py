import json

def lambda_handler(event, context):
    # O 'event' contém os dados que dispararam a função (ex: dados da API)
    nome = event.get('nome', 'Estranho')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Olá {nome}, executado via Serverless!')
    }
