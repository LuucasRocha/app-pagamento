from filaConfirmação import filaConfirmação
import json

def confirmarPagamento():
    '''
    Remove e retorna o próximo pagamento da fila de confirmações.
    '''
    pagamento = filaConfirmação.get()
    arq = open("./schema/baseDadosRecebedores.json", "r")
    dadosRecebedores = json.loads(arq.read())
    arq.close()
    for recebedor in dadosRecebedores:
        try:
            if (recebedor["agencia"] == pagamento["agencia"] and 
                recebedor["conta"] == pagamento["conta"] and 
                recebedor["tipo_conta"] == pagamento["tipo_conta"]):
                return {"status": 200, 
                        "mensagem": "Pagamento confirmado com sucesso!"}
        except KeyError:
                return {"status": 500, 
                        "mensagem": "Preencha todos os campos!"}