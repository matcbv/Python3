# MIME (Multipurpose Internet Mail Extensions) é um padrão que permite a inclusão de conteúdos
# não apenas em formato de texto simples, mas também em formatos como HTML, imagens, áudio, vídeo e outros,
# em mensagens de email.

# O módulo email.mime fornece várias subclasses que representam diferentes partes de uma mensagem MIME.
# Alguns dos principais submódulos incluem:

# email.mime.multipart: Este submódulo é usado para criar mensagens MIME multipart,
# que podem conter várias partes independentes. Por exemplo, uma mensagem MIME multipart pode conter
# um texto simples, um HTML e um ou mais anexos.

# email.mime.text: Este submódulo é utilizado para criar partes de texto em uma mensagem MIME.
# Você pode usar isso para incluir texto simples em um email.

# email.mime.image, email.mime.audio, email.mime.video: Esses submódulos são usados para representar
# partes de uma mensagem MIME que contêm imagens, áudio e vídeo, respectivamente.

# email.mime.application: Este submódulo é utilizado para criar partes de aplicativos em uma mensagem MIME,
# que são geralmente usadas para representar anexos de arquivos.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = MIMEMultipart()
print(type(email))

# Quando você faz mensagem['From'] = 'remetente@example.com' em um objeto MIMEMultipart,
# está, na verdade, chamando o método __setitem__() da classe MIMEMultipart.
# Esse método permite que você defina ou atualize os cabeçalhos da mensagem MIME diretamente,
# usando a sintaxe de indexação ([]).

# Internamente, esse método converte as chaves e valores fornecidos em chamadas para os métodos
# add_header() ou replace_header() da classe MIMEMultipart.
# Dependendo se o cabeçalho já existe ou não, o método apropriado será chamado para adicionar um novo cabeçalho ou substituir um cabeçalho existente.
email['From'] = 'matheuscbv23@gmail.com'
email['To'] = 'matheuscbv2332@gmail.com'
email['Subject'] = 'Este é um email de teste'

print(email.as_string())

# Ao utilizarmos nosso construtor MIMEText, devemos passar o texto que queremos adicionar.
# Esse, deve ser em formato de string. Também podemos passar um subtipo, esse, pode ter o
# valor plain, caso o arquivo contivesse apenas texto simples.
corpo_email = MIMEText('Mensagem de teste.', 'html', 'utf-8')
email.attach(corpo_email)