import string

texte = open("trois_petites_oies.txt", encoding="utf-8").read()
minuscules = texte.lower()

propre = minuscules.translate( str.maketrans('’',' ', string.punctuation + '…\t\n' ) )
mots   = propre.split()

mots_inutiles = [
    "à", "aujourd'hui", "alors", "au", "aucuns", "aussi", "autre", "avant", "avec", "avoir",
    "bon",
    "ça", "car", "ce", "cela", "ces", "ceux", "chaque", "ci", "comme", "comment",
    "dans", "des", "du", "dedans", "dehors", "depuis", "devrait", "doit", "donc", "dos", "début",
    "elle", "elles", "en", "encore", "essai", "est", "et", "eu",
    "fait", "faites", "fois", "font",
    "hors",
    "ici", "il", "ils",
    "je", "juste",
    "la", "le", "les", "leur",
    "ma", "maintenant", "mais", "mes", "mien", "moins", "mon", "mot", "même",
    "ni", "nommés", "notre", "nous",
    "ou", "où",
    "par", "parce", "pas", "peut", "peu", "plupart", "pour", "pourquoi",
    "quand", "que", "quel", "quelle", "quelles", "quels", "qui",
    "sa", "sans", "ses", "seulement", "si", "sien", "son", "sont", "sous", "soyez",	 "sujet", "sur",
    "ta", "tandis", "tellement", "tels", "tes", "ton", "tous", "tout", "trop", "très", "tu",
    "voient", "vont", "votre", "vous", "vu",
    "étaient", "état", "étions", "été", "être"
]

mots_utiles = []
for mot in mots :
    if mot not in mots_inutiles and len(mot)>1:
        mots_utiles.append(mot)

mots_utiles = [mot for mot in mots if mot not in mots_inutiles and len(mot)>1]

print(mots_utiles)
