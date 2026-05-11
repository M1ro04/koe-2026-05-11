"""
Viikonpäivä

ISO 8601 -standardin (https://en.wikipedia.org/wiki/ISO_8601) mukaan viikonpäivät on numeroitu
siten, että maanantai on 1 ja sunnuntai 7. Tässä tehtävässä sinun tulee toteuttaa funktio nimeltä
`viikonpaiva`, joka saa parametrinaan kokonaisluvun, joka edustaa viikonpäivän numeroa 1-7.

Funktion tulee palauttaa merkkijonona viikonpäivän nimi suomeksi seuraavasti:

    - 1: "maanantai"
    - 2: "tiistai"
    - 3: "keskiviikko"
    - 4: "torstai"
    - 5: "perjantai"
    - 6: "lauantai"
    - 7: "sunnuntai"

Esimerkit:

    >>> viikonpaiva(1)
    'maanantai'

    >>> viikonpaiva(3)
    'keskiviikko'

    >>> viikonpaiva(6)
    'lauantai'

    >>> viikonpaiva(7)
    'sunnuntai'

Jos funktiolle annetaan luku, joka ei ole välillä 1-7, sen tulee palauttaa tyhjä merkkijono "".

    >>> viikonpaiva(0)      # Luku on liian pieni (palauttaa tyhjän merkkijonon)
    ''

    >>> viikonpaiva(8)      # Luku on liian suuri (palauttaa tyhjän merkkijonon)
    ''

Huomaa, että funktiosi ei saa tulostaa mitään, vaan sen tulee palauttaa viikonpäivän nimi.

    >>> viikonpaiva(2) == 'tiistai'     # funktio palauttaa arvon, ei tulosta sitä
    True

Voit käyttää tehtävässä apunasi esimerkiksi listaa, sanakirjaa tai if-lauseita. Oleellista on,
että funktiosi toimii oikein ja palauttaa oikeat viikonpäivien nimet oikeilla numeroilla.

Voit olettaa, että annettu päivän numero on aina kelvollinen kokonaisluku.
"""

def viikonpaiva(paiva_numero): 
    """Palauttaa viikonpäivän numeron perusteella."""
    viikonpaivat = {
        1: "maanantai",
        2: "tiistai",
        3: "keskiviikko",
        4: "torstai",
        5: "perjantai",
        6: "lauantai",
        7: "sunnuntai"
    }

    return viikonpaivat.get(paiva_numero, "")T
