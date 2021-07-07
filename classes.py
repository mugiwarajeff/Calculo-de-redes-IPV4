class IPV4():
    """
    Essa classe tem como objetivo, realizar todas as funções relacionadas a ips do tipo IPV4
    """
    def __init__(self, ip):
        """
        esse metodo, faz a inicialização de todas as variaveis que serão utilizadas pelos outros metodos da classe
        :param ip: O ip a ser instanciado
        """
        self.ip = ip
        self.ip_binario = ""
        self.ip_mascara_binario = ""
        self.mascara = 0
        self.numeros = [128, 64, 32, 16, 8, 4, 2, 1]
        self.primeiro = 0
        self.segundo = 0
        self.terceiro = 0
        self.quarto = 0
        self.digito_mascara = 0
        self.giro = 0
        self.num_de_host = 0
        self.todos_os_host = []
        self.ip_da_rede = ""
        self.ip_de_broadcast = ""
        self.primeiro_ip = ""
        self.ultimo_ip = ""

    def sep_octetos(self):
        """
        método que separa o numero ip em 5 grupos de numeros, para facilitar a conversão em binário
        primeiro, segundo, terceiro e quarto grupo, além do numero para mascara
        O atributo self.giro é usado temporariamente para armazenar a ultima, primeira separação que fica com o / entre os numeros e depois é dividido novamente
        :return: None
        """
        nuns = self.ip.split(".")
        self.primeiro = int(nuns[0])
        self.segundo = int(nuns[1])
        self.terceiro = int(nuns[2])
        self.giro = nuns[3]
        nuns = self.giro.split("/")
        self.quarto = int(nuns[0])
        self.digito_mascara = int(nuns[1])

    def mostra(self):
        """mostra o IP em versão binaria"""
        print(self.primeiro, self.segundo, self.terceiro, self.quarto, self.digito_mascara)

    def transforma_binario(self, numero):
        """
        metodo que faz a conversão de um numero decimal em um octeto binario
        nessa classe esse metodo é chamado pelo metodo chama_blocos
        :param numero: numero em decimal que vai ser convertido
        :return:
        """
        numero_binario = ""
        for c in self.numeros:
            if c <= numero:
                numero -= c
                numero_binario += "1"
            else:
                numero_binario += "0"
        self.ip_binario += numero_binario

    def chama_blocos(self):
        """
        ultiliza o método transforma_binario para converter todos os 4 números decimais divididos em octetos binarios
        jogando cada um na sua respectiva variável
        """
        lista_dos_blocos = [self.primeiro, self.segundo, self.terceiro, self.quarto]
        for c in lista_dos_blocos:
            self.transforma_binario(c)

    def mascara_binaria(self):
        """
        esse método cria a nossa mascara da rede em binario com base no digito_mascara
        :return: None
        """
        cont = 0
        for c in range(0,32,1):
            if cont < self.digito_mascara:
                self.ip_mascara_binario += "1"
                cont += 1
            else:
                self.ip_mascara_binario += "0"
                cont += 1

    def definir_numero_hosts(self):
        """
        descobre o numero de host com base na nossa mascara em binário
        :return: None
        """
        self.num_de_host = (2 ** self.ip_mascara_binario.count("0")) - 2

    def alocar_todos_os_hosts(self):
        """
        cria uma lista com todos os hosts possiveis dentro desse numero de IP
        :return: None
        """
        for c in range(self.num_de_host + 2):
            if c == 0 or c == 1 or c == self.num_de_host or c == self.num_de_host + 1:
                self.todos_os_host.append(c)

    def oct_mascara(self, oct):
        """esse metodo obtem o ultimo numero da mascacara em decimal"""
        oct_bin = oct
        soma = 0
        for c,d in enumerate(oct_bin):
            if d == "1":
                soma += self.numeros[c]
            else:
                pass
        return soma

    def formata_mostra_ips(self):
        """
        Esse ultimo metodo formata todos os ips obtidos anteriormente e mostra eles na tela
        :return: None
        """
        self.primeiro_ip = f"{self.primeiro}.{self.segundo}.{self.terceiro}.{self.todos_os_host[1]}/{self.digito_mascara}"
        self.ultimo_ip = f"{self.primeiro}.{self.segundo}.{self.terceiro}.{self.todos_os_host[-2]}/{self.digito_mascara}"
        self.ip_de_broadcast = f"{self.primeiro}.{self.segundo}.{self.terceiro}.{self.todos_os_host[-1]}/{self.digito_mascara}"
        self.ip_da_rede = f"{self.primeiro}.{self.segundo}.{self.terceiro}.{self.todos_os_host[0]}/{self.digito_mascara}"
        mascara_da_rede = f"{self.oct_mascara(self.ip_mascara_binario[0:8])}.{self.oct_mascara(self.ip_mascara_binario[8:16])}.{self.oct_mascara(self.ip_mascara_binario[16:24])}.{self.oct_mascara(self.ip_mascara_binario[24:])}"
        print(f"Mascara da Rede: {mascara_da_rede}\nPrimeiro IP: {self.primeiro_ip}\nUltimo IP: {self.ultimo_ip}\nIP de Broadcast: {self.ip_de_broadcast}\nIP da Rede: {self.ip_da_rede}")

    def calcular(self):
        """
        chama todos os metodos necessarios da classe para obter o calculo e manter a organização do programa
        :return:
        """
        self.sep_octetos()
        self.chama_blocos()
        self.mascara_binaria()
        self.definir_numero_hosts()
        self.alocar_todos_os_hosts()
        self.formata_mostra_ips()

