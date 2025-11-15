# Cifrador/Decifrador Básico

## Descrição
Programa que permite cifrar e decifrar mensagens usando AES ou DES no modo ECB.

## Requisitos
- Python 3.x
- pycryptodome

## Instalação
```bash
pip install -r requirements.txt
```

## Como Usar
```bash
python cifrador.py
```

## Exemplo de Uso
```
Escolha o algoritmo (1-AES, 2-DES): 1
Digite a mensagem: Hello World
Texto cifrado: a1b2c3d4e5f6...
Digite texto cifrado: a1b2c3d4e5f6...
Texto original: Hello World
```

## Funcionalidades
- Menu interativo para escolher entre AES e DES
- Entrada de texto pelo teclado
- Saída do texto cifrado em hexadecimal
- Decifração usando o texto cifrado em hexadecimal
- Modo ECB para simplicidade

## Características Técnicas
- **AES**: Chave de 128 bits (16 bytes)
- **DES**: Chave de 64 bits (8 bytes)
- **Modo**: ECB (Electronic Codebook)
- **Padding**: PKCS7
- **Formato de saída**: Hexadecimal
