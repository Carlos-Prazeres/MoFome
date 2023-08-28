class AvaliacaoDeReceitas():
    def __init__(self):
        self.notaMedia = 0.0
        self.quantidadeDeAvaliacoes = 0
        self.somaDeNotas = 0
        self.notaAntiga = 0.0
        self.quantidadeDeAvaliacoesAntigas = 0
        self.avaliacoesNovas = 0
        self.cometariosNovos = 0

    def atualizarAvaliacao(self, avaliacao):
        self.notaAntiga = self.notaMedia
        self.quantidadeDeAvaliacoesAntigas = self.quantidadeDeAvaliacoes
        self.somaDeNotas += int(avaliacao)
        self.quantidadeDeAvaliacoes += 1
        self.notaMedia = self.somaDeNotas / self.quantidadeDeAvaliacoes
        self.avaliacoesNovas += 1