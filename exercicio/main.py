from contas import ContaCorrente, ContaPoupanca

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
