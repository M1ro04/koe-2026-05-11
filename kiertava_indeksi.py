"""
Kiertävä indeksi

Tehtäväsi on toteuttaa funktio `kiertava_indeksi`, joka mahdollistaa arvojen hakemisen listalta
listan "rajojen yli". Käytännössä tämä tarkoittaa sitä, että jos indeksi ylittää listan pituuden,
laskenta aloitetaan uudelleen listan alusta:

    >>> lista = ['Ois', 'viisaampi', 'häipyy', 'täält']    # esimerkkilista

    >>> kiertava_indeksi(lista, 0)      # listan ensimmäinen indeksi
    'Ois'

    >>> kiertava_indeksi(lista, 1)      # listan toinen indeksi
    'viisaampi'

    >>> kiertava_indeksi(lista, 2)      # listan kolmas indeksi
    'häipyy'

    >>> kiertava_indeksi(lista, 3)      # 3 on esimerkkilistan viimeinen normaali indeksi
    'täält'

    >>> kiertava_indeksi(lista, 4)      # indeksi 4 kiertää esimerkkilistan "ympäri" alkuun:
    'Ois'

    >>> kiertava_indeksi(lista, 8)      # indeksi 8 kiertää esimerkkilistan "ympäri" kahdesti:
    'Ois'


Funktiolle annettava indeksi voi olla niin suuri, että indeksit pyörähtävät ympäri useasti:

    >>> kiertava_indeksi(lista, 1_000_000_000)
    'Ois'


Saman logiikan tulee toimia myös negatiivisilla indekseillä ja eri pituisilla listoilla:

    >>> kiertava_indeksi(lista, -1) # listan viimeinen arvo
    'täält'

    >>> kiertava_indeksi(lista, -5) # indeksi pyörähtää ympäri viimeiseen arvoon:
    'täält'

    >>> kiertava_indeksi(lista, -6) # indeksi pyörähtää ympäri toiseksi viimeiseen arvoon:
    'häipyy'

    >>> kiertava_indeksi( ["I" , "can't", "get", "you", "out", "of", "my", "system"], 15)
    'system'

Huomaa, että funktion tulee aina palauttaa arvo, eikä esimerkiksi tulostaa sitä:

    >>> kiertava_indeksi(lista, 999_999_999) == 'täält'        # funktio palauttaa, ei tulosta
    True


Voit olettaa, että funktiolle annettavassa listassa on aina vähintään yksi arvo ja että indeksit
ovat aina kelvollisia kokonaislukuja. Funktiosi tulee toimia minkä pituisilla listoilla tahansa.

Vinkki: indeksin laskemisessa voi olla apua jakojäännöksestä eli "modulo"-operaattorista (%) sekä
len-funktiosta.
"""


def kiertava_indeksi(arvot: list, indeksi: int) -> str:
    """Palauttaa listan arvon kiertävän indeksin perusteella."""
    return arvot[indeksi % len(arvot)]

lista = ['Ois', 'viisaampi', 'häipyy', 'täält']

print(kiertava_indeksi(lista, 0))   # Ois
print(kiertava_indeksi(lista, 4))   # Ois
print(kiertava_indeksi(lista, -1))  # täält
print(kiertava_indeksi(lista, -6))  # häipyy


