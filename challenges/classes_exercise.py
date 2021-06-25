""" 
Exercício

Dada a class Leitor:

- Implemente um método de busca. Esse método de busca deverá receber 
obrigatoriamente uma 'string' e outros argumentos que você achar necessário 
e deverá retornar as linhas que possuem essa 'string'

- Chamar o método criado

- Exibir o retorno

DICA: Ao iterar o retorno do método `open_file`, 
cada iteração irá retornar a próxima linha do arquivo aberto

"""
class Leitor:

    def open_file(self, file_path):
        return open(file_path, 'r')
    
    def show_content(self, file_path):
        with self.open_file(file_path) as file_ref:
            
            for row in file_ref:
                print(row, end="")
