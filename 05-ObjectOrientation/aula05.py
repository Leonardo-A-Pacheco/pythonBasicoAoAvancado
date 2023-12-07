# mantendo estados dentro da classe
class camera:
    def __init__(self, nome, filmando = False):
        # recebendo instancia nome e estado predefinido como false
        self.nome = nome
        self.filmando = filmando
        self.light = False

    # criando uma função para filmar
    def rec(self):
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return

        print(f'{self.nome} está filmando...') 
        self.filmando = True
    
    def stop_rec(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando.')
            return
        print(f'{self.nome} parando de filmar...')
        self.filmando = False

    def on_light(self):
        if self.light:
            print(f'{self.nome}: A luz já está acesa!')
            return
        self.light = True
        print(f'{self.nome}: agora a luz está acesa!')

    def off_light(self):
        if self.light == False:
            print(f'{self.nome}: ja está com a luz apagada!')
            return
        self.light = False
        print(f'{self.nome}: a luz foi apagada!')

# instanciando a classe
c1 = camera('polaroid')
# testando funções
c1.rec()
c1.stop_rec()
c1.off_light()
c1.on_light()
c1.off_light()
c1.off_light()
c1.on_light()
c1.on_light()
