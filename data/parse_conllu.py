# -*- coding: utf-8 -*-

"""
Helps parsing a conllu file into sentences and words
See http://universaldependencies.org/format.html 
"""


class Word:
    """
    A word (i.e. a line of a conll file) with its features
    """

    def __init__(
        self,
        nid="_",
        form="_",
        lemma="_",
        upos="_",
        xpos="_",
        feats="_",
        head="_",
        dep_rel="_",
        deps="_",
        misc="_",
    ):
        self.nid = nid
        self.form = form
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.feats = feats
        self.head = head
        self.dep_rel = dep_rel
        self.deps = deps
        self.misc = misc

    def __str__(self):
        text = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            self.nid,
            self.form,
            self.lemma,
            self.upos,
            self.xpos,
            self.feats,
            self.head,
            self.dep_rel,
            self.deps,
            self.misc,
        )
        return text


class Sentence:
    """
    A sentence is composed of a list of Word objects and a list of comments (str)
    """

    def __init__(self):
        self.words = []
        self.sent_id = ""
        self.text = ""

    def __str__(self):
        lines = ""
        lines += "# sent_id = "
        lines += self.sent_id + "\n"
        lines += "# text = "
        lines += self.text + "\n"
        for word in self.words:
            lines += str(word)
            lines += "\n"
        return lines

    def add_word(self, line):
        """
        Add a Word to the words list
        Args:
            line (str): a line of an orfeo file with a word informations
        """
        #ajouter un MOT(avec tous les arguments) à la liste de mots danns PHRASE
        self.words.append(Word(*line.strip().split("\t")))
        #on crée UNE liste avec à partir de la ligne 
        #python pense que la liste est un argument et tous les autres champs vonts être des _
        #débaler une séquence avec * : prend les éléments de la liste et les mets 1 par 1 dans les agts
        # strip retire \n
        #pour débaler dico **


def parse_file(filename):
    """
    Create list
    Turns a file into a list of sentences
    Args: 
        filename (str): the file path
    Return:
        list of Sentence
    """
    sentences = [] #on va accumuler les phrases ici (liste)
    with open(filename) as fichier:
        sentence = Sentence() #contient objet - on crée la phrase où on va ajouter des mots
        for line in fichier:
            if line.startswith("#"):
                continue
            if not line.strip(): #retirer les caractères d'espace au début et à la fin - la ligne vide sépare 2 phrases
                sentences.append(sentence)
                sentence = Sentence() #on met à jour la phrase "courante"
            else:  #on lit un mot et on l'ajout à la phrase
                sentence.add_word(line)
    return sentences
    


def number_of_tokens(sentences, category=None):
    """
    Count the number of words in sentences
    If category is given, only count words of this category, otherwise count all
    Args:
        sentences (list) : the list of Sentence objects
        category (str, default None) : the category to count
    Return:
        the count of words in sentences of category
    """
    #si catégore = NON on prend tous les mots
    #sinon on prends tous les mots avec la bonne catégorie
#    return sum([word for word in sentence.words 
#               for sentence in sentences 
#               if category is None or word.upos == category])
    somme = 0 
    for sentence in sentences:
        for word in sentence.words:
            if category is None:
                somme =+1
            elif word.upos == category:
                somme += 1
    return somme
                

def ments_not_adv(sentences):
    """
    Count the number of words in sentences that end with "ment" but are not ADV
    Args:
        sentences (list) : the list of Sentence objects
    Return:
        the list of words
    """
    ments = []
    for sentence in sentences:
        for word in sentence.words:
            if word.lemma.endswith("ment") and word.upos != 'ADV':
                ments.append(word)
    return ments


sentences = parse_file('fr_gsd-ud-test.conllu')
assert len(sentences) == 416
assert number_of_tokens(sentences) == 10300
pos = input(f"\n\nLes tokens de quel POS voulez-vous compter ? ")
nb_tokens = number_of_tokens(sentences, pos)
print(f"Le fichier contient {nb_tokens} tokens annotés {pos}.")
assert number_of_tokens(sentences, "NOUN") == 1852
ments = ments_not_adv(sentences)
assert len(ments) == 54
# affichez les -ments non ADV triés par forme et par fonction
