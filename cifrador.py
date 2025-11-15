from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

def cifrar_aes(mensagem):
    # Gera uma chave de 16 bytes (128 bits) para AES
    chave = get_random_bytes(16)
    
    # Cria o cifrador AES no modo ECB
    cipher = AES.new(chave, AES.MODE_ECB)
    
    # Converte a mensagem para bytes e adiciona padding
    mensagem_bytes = mensagem.encode('utf-8')
    mensagem_padded = pad(mensagem_bytes, AES.block_size)
    
    # Cifra a mensagem
    texto_cifrado = cipher.encrypt(mensagem_padded)
    
    # Retorna o texto cifrado em hexadecimal e a chave
    return binascii.hexlify(texto_cifrado).decode('utf-8'), chave


def decifrar_aes(texto_cifrado_hex, chave):

    # Converte o texto hexadecimal de volta para bytes
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)
    
    # Cria o cifrador AES no modo ECB com a mesma chave
    cipher = AES.new(chave, AES.MODE_ECB)
    
    # Decifra a mensagem
    mensagem_padded = cipher.decrypt(texto_cifrado)
    
    # Remove o padding
    mensagem_bytes = unpad(mensagem_padded, AES.block_size)
    
    # Retorna a mensagem original
    return mensagem_bytes.decode('utf-8')


def cifrar_des(mensagem):
    # Gera uma chave de 8 bytes (64 bits) para DES
    chave = get_random_bytes(8)
    
    # Cria o cifrador DES no modo ECB
    cipher = DES.new(chave, DES.MODE_ECB)
    
    # Converte a mensagem para bytes e adiciona padding
    mensagem_bytes = mensagem.encode('utf-8')
    mensagem_padded = pad(mensagem_bytes, DES.block_size)
    
    # Cifra a mensagem
    texto_cifrado = cipher.encrypt(mensagem_padded)
    
    # Retorna o texto cifrado em hexadecimal e a chave
    return binascii.hexlify(texto_cifrado).decode('utf-8'), chave


def decifrar_des(texto_cifrado_hex, chave):
    # Converte o texto hexadecimal de volta para bytes
    texto_cifrado = binascii.unhexlify(texto_cifrado_hex)
    
    # Cria o cifrador DES no modo ECB com a mesma chave
    cipher = DES.new(chave, DES.MODE_ECB)
    
    # Decifra a mensagem
    mensagem_padded = cipher.decrypt(texto_cifrado)
    
    # Remove o padding
    mensagem_bytes = unpad(mensagem_padded, DES.block_size)
    
    # Retorna a mensagem original
    return mensagem_bytes.decode('utf-8')


def main():
    print("=" * 50)
    print("Cifrador/Decifrador Básico")
    print("=" * 50)
    
    # Menu de escolha do algoritmo
    print("\nEscolha o algoritmo (1-AES, 2-DES): ", end="")
    escolha = input().strip()
    
    if escolha not in ['1', '2']:
        print("Opção inválida!")
        return
    
    # Solicita a mensagem do usuário
    print("Digite a mensagem: ", end="")
    mensagem = input()
    
    # Cifra a mensagem
    if escolha == '1':
        print("\n--- Cifrando com AES ---")
        texto_cifrado, chave = cifrar_aes(mensagem)
    else:
        print("\n--- Cifrando com DES ---")
        texto_cifrado, chave = cifrar_des(mensagem)
    
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Decifra a mensagem
    print(f"\nDigite texto cifrado: ", end="")
    texto_para_decifrar = input().strip()
    
    try:
        if escolha == '1':
            texto_original = decifrar_aes(texto_para_decifrar, chave)
        else:
            texto_original = decifrar_des(texto_para_decifrar, chave)
        
        print(f"Texto original: {texto_original}")
    except Exception as e:
        print(f"Erro ao decifrar: {e}")
        print("Certifique-se de digitar o texto cifrado corretamente.")


if __name__ == "__main__":
    main()
