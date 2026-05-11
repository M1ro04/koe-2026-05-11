r"""
Vapaat paikat

Tehtäväsi on toteuttaa funktio `vapaat_paikat`, joka saa parametrinaan merkkijonon, joka kuvaa
jalkapallostadionin katsomon istumajärjestystä. Merkkijonossa kukin rivi vastaa yhtä katsomon riviä
ja kullakin rivillä kukin merkki vastaa yhtä istuinta. 

Istuin voi olla joko vapaa tai varattu:

- vapaa istuin merkitään alaviivalla `_`
- varattu istuin on merkitään X:llä (iso x-kirjain)

Lisäksi merkkijonossa voi olla välilyöntejä ja rivinvaihtoja, jotka erittelevät rivit ja istuimet
toisistaan. Nämä välit tulee jättää huomiotta.

Esimerkiksi seuraava merkkijono kuvaa katsomoa, jossa on kolme riviä ja kussakin rivissä seitsemän
istuinta:

    >>> katsomo = '''
    ... _ X _ _ X X _
    ... X X X X X X X
    ... _ _ _ X _ _ _
    ... '''

Yllä olevassa katsomossa on yhteensä kymmenen vapaata istuinta (`_`):

* neljä vapaata ensimmäisellä rivillä
* ei yhtään vapaata toisella rivillä
* kuusi vapaata kolmannella rivillä.

Funktion `vapaat_paikat` tulee siis tässä tapauksessa palauttaa vapaiden määrä eli 4 + 0 + 6 = 10:

    >>> vapaat_paikat(katsomo)
    10


Seuraavassa katsomossa on vain yksi rivi, jolla on viisi vapaata istuinta, joten paluuarvo on 5:

    >>> vapaat_paikat('X _ X _ X _ _ X X _')    # 5 vapaata istuinta (_)
    5


Funktiosi tulee toimia eri kokoisilla ja muotoisilla katsomoilla, joissa on eri määriä rivejä
ja istuimia per rivi. Voit olettaa, että annetussa katsomossa on aina vähintään yksi rivi ja
vähintään yksi istuin.

    >>> vapaat_paikat('X X X')                  # yksi rivi, ei yhtään vapaata istuinta
    0

    >>> vapaat_paikat('_ _ _\n_ _ _')           # kaksi riviä, kaikki istuimet vapaita
    6

Huomaa, että funktio ei saa tulostaa mitään, vaan tulos täytyy palauttaa paluuarvona:

    >>> vapaat_paikat('X _ X _') == 2           # funktio ei tulosta, vaan se palauttaa
    True

Funktiosi tulee toimia minkä tahansa muotoisilla ja kokoisilla katsomoilla, esimerkiksi:

    >>> vapaat_paikat('_ \n _ _ \n _ _ _')      # epäsymmetrinen katsomo
    6

    >>> vapaat_paikat('_ _ _\n' * 333)          # 333 riviä, jokaisella rivillä 3 vapaata istuinta
    999


Vinkki: tässä tehtävässä ainoa merkki, jolla on merkitystä, on alaviiva `_`. Kaikki muut merkit
voidaan jättää huomiotta.
"""


def vapaat_paikat(katsomo):
    """Laskee katsomon vapaiden paikkojen määrän."""

    return katsomo.count("_")


