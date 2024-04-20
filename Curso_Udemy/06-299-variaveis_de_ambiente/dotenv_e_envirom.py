import os
from dotenv import load_dotenv

# O método lead_dotenv é responsável por buscar e carregar nosso arquivo .env. Por padrão, ele
# sempre procura no diretório raíz de nosso projeto, que em nosso caso é Curso_Udemy. No entanto,
# também podemos passar o caminho que nosso arquivo env está contido.
load_dotenv()

# Através do método getenv do módulo os, conseguimos obter o valor de nossas variáveis de ambiente:
print(os.getenv('DB_PASSWORD'))

# Podemos checar todas as nossas variáveis de ambiente através do método envirom:
variaveis_de_ambiente = os.environ
print(variaveis_de_ambiente)
for k, v in variaveis_de_ambiente.items():
    print(k, v, sep=': ')
