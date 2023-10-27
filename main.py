import spacy
import re

class DetectorPhishing:
    def __init__(self, palavras_chave):
        self.palavras_chave = palavras_chave
        self.nlp = spacy.load('pt_core_news_sm')

    def checar_phishing(self, email):
        doc = self.nlp(email)

        for entidade in doc.ents:
            if entidade.label_ == "EMAIL":
                return True

        for palavra_chave in self.palavras_chave:
            padrao = re.compile(fr'\b{re.escape(palavra_chave)}\b', flags=re.IGNORECASE)
            if re.search(padrao, email):
                return True
        return False

def main():
    palavras_chave = ['senha', 'urgente', 'clique aqui', 'confirme sua identidade']

    detector = DetectorPhishing(palavras_chave)

    email = str(input('Cole o conteúdo do e-mail aqui para verificar: '))

    if detector.checar_phishing(email):
        print("ALERTA: Este e-mail pode ser uma tentativa de phishing!")
    else:
        print("O e-mail parece ser seguro!")

if __name__ == "__main__":
    main()
