# Desafio Técnico - Sparta | API de Cálculo de Taxa

API REST que calcula o valor monetário da taxa de administração a ser cobrada de cada cotista de um fundo de investimento.

## 🚀 Tecnologias

* **Python 3.12+**
* **FastAPI** - Framework para API
* **Uvicorn** - Servidor ASGI
* **Pydantic** - Validação de dados
* **Pytest** - Testes unitários

## ⚙️ Como Rodar

**1. Clone e configure:**
```bash
git clone https://github.com/dib10/sparta_teste_backendJR
cd sparta_teste_backendJR
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate    # Linux/macOS
```

**2. Instale dependências:**
```bash
pip install -r requirements.txt
```

**3. Execute a API:**
```bash
uvicorn app.main:app --reload --port 8001
```

Acesse: `http://127.0.0.1:8001/docs` (Swagger UI)

## 🧪 Testes

```bash
pytest
```

## 🔧 Endpoints

### POST `/calcular`
Calcula a taxa de administração para cada cotista.

**Request:**
```json
{
  "taxa": 0.01,
  "cotas": [
    {"valor": 10.50, "quantidades": [100, 200]},
    {"valor": 11.00, "quantidades": [100, 250]}
  ]
}
```

**Response:**
```json
[0.08531746031746032, 0.19246031746031744]
```

### GET `/`
Health check

## 📊 Estrutura

```
sparta_teste_backendJR/
├── app/
│   ├── main.py          # FastAPI app
│   ├── schemas.py       # Pydantic models
│   ├── services.py      # Business logic
│   └── exceptions.py    # Custom exceptions
├── test_services.py     # Unit tests
└── requirements.txt
```

## 🏛️ Decisões Principais que Tomei

A seguir, apresento as principais decisões e a minha linha de pensamento durante o desenvolvimento do desafio.

### Desafios e Linha de Pensamento

O meu primeiro e principal desafio foi traduzir a fórmula matemática do ramo financeiro para uma estrutura de código que fosse limpa e fizesse sentido. A maior dificuldade foi, sem dúvida, "traduzir" a fórmula do mundo financeiro para a lógica de programação (kkk).

*Nota: O brainstorm inicial que fiz no papel para entender a fórmula e planejar a implementação está disponível em PDF no repositório.*

Para isso, segui uma abordagem de "dividir para conquistar". Em vez de colocar tudo numa única função, o meu primeiro passo foi quebrar a fórmula em partes lógicas. Comecei por definir uma função só para determinar o número de cotistas (`_obter_num_cotistas`). Quis fazer assim para ter mais legibilidade no código e para que o entendimento da lógica matemática ficasse mais claro.

Após isso, pensei que, se eu quebrasse em ainda mais funções, poderia ficar com muita engenharia para pouca coisa, então decidi criar apenas duas funções auxiliares e uma função principal que as chamaria. Com a lógica implementada, executei alguns testes básicos, principalmente para garantir que o número de cotistas não iria flutuar de um dia para o outro, conforme a regra prevista no enunciado. Depois disso, fiz alguns ajustes finais na separação e organização dos ficheiros.

### Futuras Observações e Melhorias

Para este projeto, optei por manter a estrutura de ficheiros simples (`main.py`, `services.py`, etc.). No futuro, para um projeto ideal ou de maior escopo, eu certamente separaria o código em pastas mais específicas, como `services/`, `controllers/` e `tests/`. Contudo, para a dimensão deste desafio, achei que isso limitaria muito os imports e o movimento entre os ficheiros, então mantive uma abordagem mais direta.

## 👨‍💻 Autor

**Caio Dib** - Desenvolvedor Backend Júnior