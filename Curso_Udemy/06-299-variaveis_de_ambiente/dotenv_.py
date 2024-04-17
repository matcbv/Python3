from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path().absolute() / '.env'
# O método lead_dotenv é responsável por buscar e carregar nosso arquivo .env. Por padrão, ele
# sempre procura no diretório raíz de nosso projeto, que em nosso caso é Curso_Udemy. No nosso
# caso, passamos o caminho que nosso arquivo env está contido.
load_dotenv(env_path)

# Através do método getenv do módulo os, conseguimos obter o valor de nossas variáveis de ambiente:
print(os.getenv('DB_PASSWORD'))
