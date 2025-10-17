from filaConfirmação import filaConfirmação

def submeterPagamento(pagamento):
    '''
    Adiciona um pagamento à fila de confirmações.
    Exemplo de pagamento:
    {"valor": 100, 
    "moeda": "BRL", 
    "metodo": "transferencia",
    "agencia": "1234",
    "conta": "56789-0",
    "tipo_conta": "corrente"
    }
    '''
    filaConfirmação.put(pagamento)