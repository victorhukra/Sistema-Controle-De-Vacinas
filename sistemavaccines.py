class NãoEncontrado(Exception):
    pass

class EstoqueInsuficiente(ValueError):
    pass

class RegistroVazio(Exception):
    pass

class DoseInvalida(ValueError):
    pass

def cadastrarVacina(lista):

    while True:
        try:
            qtdEstoque = int(input('\nInforme a quantidade de vacinas que deseja cadastrar: '))
            break
        except ValueError:
             print('\nInforme um valor valor válido.')
    for i in range(qtdEstoque):
        nomeVacina = input(f'\nVacina ({i+1}) - Nome: ')
        codigoVacina = input(f'{nomeVacina} - Código: ')
        while True:
            try:
                dosesVacina = int(input(f'{nomeVacina} - Doses necessárias: '))
                if dosesVacina > 6 or dosesVacina <= 0:
                    print('\nA dose aplicada é inválida. (máximo: 6)')
                    continue
                break
            except ValueError:
                print('\nInforme um valor válido para as doses.')
        while True:
            try:
                estoqueVacina = int(input(f'{nomeVacina} - Estoque: '))
                break
            except ValueError:
                print('\nInforme um valor válido para o estoque.')

        dictVacina = {'nome': nomeVacina, 'codigo': codigoVacina, 'doses': dosesVacina, 'estoque': estoqueVacina}
        lista.append(dictVacina)

    return f'\n{qtdEstoque} vacinas cadastradas com sucesso!'

def cadastrarPaciente(lista):

    while True:
        try:
            qtdPaciente = int(input('\nInforme a quantidade de pacientes que deseja cadastrar: '))
            break
        except ValueError:
            print('\nInforme um valor válido.')
    for i in range(qtdPaciente):
        nomePaciente = input(f'\nPaciente ({i+1}) - Nome: ')
        codigoPaciente = input(f'{nomePaciente} - Código: ')
        while True:
            try:
                idadePaciente = int(input(f'{nomePaciente} - Idade: '))
                break
            except ValueError:
                print(f'\nInforme uma idade válida para {nomePaciente}.')

        dictPaciente = {'nome': nomePaciente, 'codigo': codigoPaciente, 'idade': idadePaciente}
        lista.append(dictPaciente)

    return f'\n{qtdPaciente} Pacientes cadastrados com sucesso!'


def registroAplicacoes(vacina, paciente, registros):
    if len(vacina) == 0 or len(paciente) == 0:
        raise RegistroVazio('\nOs registros necessários para executar essa opção ainda não foram efetuados.')

    while True:
    
        codeVacina = input('\nInforme o código da vacina: ')
        codePaciente = input('Informe o código do paciente: ')
        while True:
            try:
                doseAplicada = int(input('Informe a dose aplicada: '))
                if 0 <= doseAplicada > 6:
                    print('\nA dose aplicada é inválida. (máximo: 6)')
                    continue
                break
            except ValueError:
                print('\nInforme um valor válido para doses.')


        encontrado = False
        for vaccine in vacina:
            for patient in paciente:
                if codeVacina == vaccine['codigo'] and codePaciente == patient['codigo']:
                    encontrado = True
                    if vaccine['estoque'] > 0:
                        vaccine['estoque'] -= 1
                    else:
                        raise EstoqueInsuficiente('\nEstoque Insuficiente.')
                    
                    if doseAplicada > vaccine['doses']:
                        raise DoseInvalida('\nDose inválida.')

        if not encontrado:
            raise NãoEncontrado('\nCódigo inválido.')
        
        else:
            dictRegistro = {'vacina': codeVacina, 'paciente': codePaciente, 'doses': doseAplicada}
            registros.append(dictRegistro)

        continuar = input('\nDeseja continuar a registrar aplicações? (s/n): ').lower()
        if continuar != 's':
            break

    return '\nAplicação registrada!'


def listarVacina(vacina):
    if len(vacina) == 0:
        raise RegistroVazio('\nNão há nenhuma vacina cadastrada.')
    else:
        print('\nVacinas cadastradas:')
        for vaccine in vacina:
            print(f'{vaccine['nome']} - {vaccine['codigo']} | Estoque: {vaccine['estoque']}un - Doses: {vaccine['doses']}')


def listarPaciente(paciente):
    if len(paciente) == 0:
        raise RegistroVazio('\nNão há nenhum paciente cadastrado.')
    else:
        print('\nPacientes cadastrados:')
        for patient in paciente:
            print(f'{patient['nome']} | {patient['codigo']} - Idade: {patient['idade']}')

def listarAplicacoes(registro):
    if len(registro) == 0:
        raise RegistroVazio('\nNão há nenhuma aplicação cadastrada.')
    else:
        print('\nAplicações cadastradas:')
        for register in registro:
            print(f'Vacina: {register['vacina']} - Paciente: {register['paciente']} | {register['doses']}ª Dose')


def vacinacaoIncompleta(vacina, registro):
    if len(vacina) == 0 or len(registro) == 0:
        raise RegistroVazio('\nOs registros necessários para executar essa opção ainda não foram efetuados.')
    
    listaDoses = []
    existe = False
    for vaccine in vacina:
        for register in registro:
            if vaccine['codigo'] == register['vacina']:
                existe = True
                if register['doses'] < vaccine['doses']:
                    faltam = vaccine['doses'] - register['doses']
                    dictIncompleto = {'paciente': register['paciente'], 'faltam': faltam}
                    listaDoses.append(dictIncompleto)
    
    for dose in listaDoses:
        print(f'- Paciente: {dose['paciente']} | Faltam: {dose['faltam']}')

def estoqueBaixo(vacina):

    list = []

    if len(vacina) == 0:
        raise RegistroVazio('\nNão há nenhuma vacina cadastrada.')
    
    else:
        print('\nVacinas com baixo estoque:')
        for vaccine in vacina:
            if vaccine['estoque'] <= 5:
                print(f'{vaccine['nome']} - {vaccine['codigo']} | Estoque: {vaccine['estoque']}un')
                list.append(vaccine['estoque'])

    if len(list) == 0:
        print('\nNão há nenhuma vacina com baixo estoque.')

def showMenu():
    print('\n---------MENU PRINCIPAL---------\n')
    print('1 - Cadastrar vacina no estoque')
    print('2 - Cadastrar paciente')
    print('3 - Registrar aplicação de vacina')
    print('4 - Listar vacinas')
    print('5 - Listar pacientes')
    print('6 - Listar aplicações')
    print('7 - Mostrar pacientes com vacinação incompleta')
    print('8 - Mostrar vacinas com estoque baixo')
    print('0 - Sair')

if __name__ == '__main__':

    listaVacina = []
    listaPaciente = []
    listaRegistros = []


    while True:
        try:
            showMenu()
            opcao = int(input(f'\nInforme sua opção: '))

            match opcao:
                case 1:
                    cadastrarVacina(listaVacina)

                case 2:
                    cadastrarPaciente(listaPaciente)
                
                case 3:
                    registroAplicacoes(listaVacina, listaPaciente, listaRegistros)
                
                case 4:
                    listarVacina(listaVacina)

                case 5:
                    listarPaciente(listaPaciente)

                case 6:
                    listarAplicacoes(listaRegistros)

                case 7:
                    vacinacaoIncompleta(listaVacina, listaRegistros)

                case 8:
                    estoqueBaixo(listaVacina)

                case 0:
                    print('Programa encerrado!')
                    break

        except Exception as e:
            print(f'{e}')
        except NãoEncontrado as e:
            print(f'{e}')
        except EstoqueInsuficiente as e:
            print(f'{e}')
        except RegistroVazio as e:
            print(f'{e}')

        except DoseInvalida as e:

            print(f'{e}')
