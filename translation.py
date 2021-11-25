class Translation(object):

      
      START_TEXT = """
(＃＞＜) Opa jovem {},

• Comandos para essa base.
- /set_cap Para alterar sua legenda
- /set_btn Para alterar o botão 
- /rmv_cap Para remover a legenda
- /rmv_btn Para remover o botão 

➡️ Um Aviso:
➪ Essa é uma base pra aprimorar para legendar arquivos, fotos, músicas (arquivos files) mais rápido, se quiser usar essa base use os comandos acima e veja como funciona! Se não souber, chame o criador. (⌒_⌒;) 
"""    
      DYNAMIC_TEXT = """
🔰 <u>Sobre as dinâmicas para usar nessa base</u>


- Você pode adicionar {variable_name} na legenda, bot substituirá essas variáveis pelo seu valor de acordo com o arquivo.

  Exemplo: Título: {filename}

  Variáveis suportadas:
  filename, ext, mime_type

  Variáveis adicionais:
  Para arquivos de vídeo: width, height, duration
  Para arquivos de áudio: title, artist, duration
"""


      MARKDOWN_TEXT = """
😴 <u>Sobre o 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧</u>


👉 <b>Textos Bold</b>

ヅ <code>**Texto**</code>

👉 <b>Italic Texto</b>

ヅ <code>__Texto__</code>

👉 <b>Underline Texto</b>

ヅ <code>--Texto--</code>

👉 <b>Strike Texto</b>

ヅ <code>~~Texto~~</code>

👉 <b>Code Texto</b>

ヅ <code>`texto`</code>

👉 <b>Hyperlink texto</b>

ヅ <code>[texto do guei](https://t.me/durov)</code>
"""
