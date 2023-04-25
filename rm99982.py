import json
import requests

encerrar = '1'

while encerrar == '1':
    rm = input("\nDigite o seu RM: ")
    with open('base_tdspy.json', 'r') as f:
        urls = json.load(f)

    if rm in urls:
        urls_rm = urls[rm]
    else:
        while rm not in urls:
            print(f"RM {rm} inválido. Por favor, tente novamente.")
            rm = input("\nDigite o seu RM: ")
        urls_rm = urls[rm]

    print(f'\nForam encontradas {len(urls_rm)} URLs correspondentes ao RM {rm}:\n')

    for url in urls_rm:
        try:
            response = requests.get(f"https://{url}")
            with open(f"{url}.html", 'w', encoding='utf-8') as f:
                f.write(response.text)
                print(f'Obtemos o conteúdo da URL: {url}')
        except requests.exceptions.RequestException as e:
            print(f"Não foi possível obter o conteúdo da URL: {url}")

    while True:
        encerrar = input('\nCaso queira encerrar:\n' 
                        'Digite 1 -> Tentar outro RM.\n'
                        'Digite 2 -> Encerrar\n')
        if encerrar == '1':
            break
        elif encerrar == '2':
            print(f'\nObrigado por usar nosso sistema de consulta JSON!')
            break
        elif encerrar != '1':
            print(f'\nInformação inválida, digite 1 ou 2!') 