from confirmarPagamento import confirmarPagamento
from submeterPagamento import submeterPagamento
from filaConfirmação import filaConfirmação

def test_confirmarPagamento_success():
    payload = {
        "agencia": "1234",
        "conta": "56789-0",
        "tipo_conta": "corrente",
        "valor": 150.00
    }
    filaConfirmação.put(payload)
    assert confirmarPagamento() == {"status": 200, 
                    "mensagem": "Pagamento confirmado com sucesso!"}

def test_confirmarPagamento_fail():
    payload = {
        #"agencia": "1234",
        "conta": "56789-0",
        "tipo_conta": "corrente",
        "valor": 150.00
    }
    filaConfirmação.put(payload)
    assert confirmarPagamento() ==  {"status": 500, 
                        "mensagem": "Preencha todos os campos!"}
    
def test_submeterPagamento_success():
    payload = {
        "valor": 100,
        "moeda": "BRL",
        "metodo": "transferencia",
        "agencia": "1234",
        "conta": "56789-0",
        "tipo_conta": "corrente"
    }
    submeterPagamento(payload)
    assert filaConfirmação.qsize() == 1

def test_submeterPagamento_multiple():
    payload1 = {
        "valor": 200,
        "moeda": "BRL",
        "metodo": "transferencia",
        "agencia": "4321",
        "conta": "09876-5",
        "tipo_conta": "poupança"
    }
    payload2 = {
        "valor": 300,
        "moeda": "BRL",
        "metodo": "pix",
        "agencia": "1234",
        "conta": "56789-0",
        "tipo_conta": "corrente"
    }
    submeterPagamento(payload1)
    submeterPagamento(payload2)
    assert filaConfirmação.qsize() == 2

test_confirmarPagamento_success()
test_confirmarPagamento_fail()
test_submeterPagamento_success()
test_submeterPagamento_multiple()

print("Todos os testes passaram com sucesso!")