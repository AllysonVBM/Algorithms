# 🧩 Estrutura da Classe `Node`

## 🏗️ 1. Criação da Classe

Primeiro, criamos a classe `Node`:

```python
class Node:
    ...
⚙️ 2. Método __init__
Em seguida, criamos o método construtor __init__, responsável por inicializar o nó:

python
Copy code
def __init__(self, initial_data):
    self.data = initial_data
    self.next = None
Explicação
self.data → Armazena o valor do nó.

self.next → Guarda a referência (endereço) do próximo nó.
Inicialmente, é definido como None.

📤 3. Método get_data()
Responsável por retornar o valor armazenado no nó.

python
Copy code
def get_data(self):
    return self.data
📝 4. Método set_data()
Responsável por atribuir um novo valor ao nó.

python
Copy code
def set_data(self, new_data):
    self.data = new_data
🔗 5. Método get_next()
Retorna a referência (endereço) do próximo nó na lista.

python
Copy code
def get_next(self):
    return self.next
🔄 6. Método set_next()
Define o endereço do próximo nó da lista.

python
Copy code
def set_next(self, new_next):
    self.next = new_next
🚀 Execução do Código
Durante a execução, fizemos o seguinte:

1️⃣ Criamos dois nós:
python
Copy code
node1 = Node(10)
node2 = Node(20)
Neste momento:

ini
Copy code
node1 = (10, None)
node2 = (20, None)
2️⃣ Alteramos o valor do primeiro nó:
python
Copy code
node1.set_data(30)
Agora node1 possui o valor (30, None).

3️⃣ Ligamos o primeiro nó ao segundo:
python
Copy code
node1.set_next(node2)
Assim, node1 passa a referenciar node2:

ini
Copy code
node1 = (30, address(node2))
🧠 Resultado Final
Criamos uma Linked List simples, onde:

css
Copy code
node1 → node2 → None
Ou representando apenas os valores:

scss
Copy code
(30) → (20)
🔍 Resumo
Etapa	Função	Responsabilidade
1	__init__	Inicializa o nó
2	get_data	Retorna o valor do nó
3	set_data	Atualiza o valor do nó
4	get_next	Retorna o próximo nó
5	set_next	Define o próximo nó