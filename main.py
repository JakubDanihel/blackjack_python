import random
import sys

HEARTS = chr(9829)  # ♥
DIAMONDS = chr(9830)  # ♦
SPADES = chr(9824)  # ♠
CLUBS = chr(9827)  # ♣

def main():
    peniaze = 5000

    while True:
        if peniaze < 0:
            print("Nemas love kamo...\nHadam mas stastie v laske... kek")
            sys.exit()

        print("Peniaze ", peniaze)
        vklad = getVkladPeniaze(peniaze)

        kopa = getDeck()
        deelerHand = [kopa.pop(), kopa.pop()]
        playerHand = [kopa.pop(), kopa.pop()]

        print("Vklad je: ", vklad)

        while True:
            ukazRuky(playerHand, deelerHand, False)
            print("")

            if getRukaHodnota(playerHand) > 21:
                break

            move = getMove()
            if move == "D":
                dalsiVklad = getVkladPeniaze(min(vklad, (peniaze - vklad)))
                vklad += dalsiVklad
                print("Vklad zvyseny na {}".format(vklad))
                print("Vklad: ", vklad)

            if move in ("H", "D"):
                novaKarta = kopa.pop()
                rank, suit = novaKarta
                print("Potiahol si si: {} {}".format(rank, suit))
                playerHand.append(novaKarta)

                if getRukaHodnota(playerHand) > 21:
                    continue

            if move in ("S", "D"):
                break

        if getRukaHodnota(playerHand) <= 21:
            while getRukaHodnota(deelerHand) < 17:
                print("Deeler taha: ")
                deelerHand.append(kopa.pop())
                ukazRuky(playerHand, deelerHand, False)

                if getRukaHodnota(deelerHand) > 21:
                    break

                input("Dalsie kolo")
                print("\n\n")

        ukazRuky(playerHand, deelerHand, False)

        playerhodnota = getRukaHodnota(playerHand)
        deelerhodnota = getRukaHodnota(deelerHand)

        if deelerhodnota > 21:
            print("Vihral si! Ziskal si {}".format(vklad))
            peniaze += vklad
        elif (playerhodnota > 21) or (playerhodnota < deelerhodnota):
            print("Prehral si.")
            peniaze -= vklad
        elif playerhodnota > deelerhodnota:
            print("Vyhral si {}".format(vklad))
            peniaze += vklad
        elif playerhodnota == deelerhodnota:
            print("Remiza")
        input("Zadaj enter pre pokracovanie: ")

        print("\n\n")

def getVkladPeniaze(maxVklad):
    while True:
        print("Kolko chces vlozit? 1 - {} alebo QUIT pre ukoncenie".format(maxVklad))
        vklad = input("> ").upper().strip()

        if vklad == "QUIT":
            print("Dakujem za hru")
            sys.exit()

        if not vklad.isdecimal():
            continue

        vklad = int(vklad)
        if 1 <= vklad <= maxVklad:
            return vklad

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def getRukaHodnota(karty):
    hodnota = 0
    pocetEs = 0

    for karta in karty:
        rank = karta[0]
        if rank == "A":
            pocetEs += 1
        elif rank in ("J", "Q", "K"):
            hodnota += 10
        else:
            hodnota += int(rank)

    hodnota += pocetEs
    for i in range(pocetEs):
        if hodnota + 10 <= 21:
            hodnota += 10
    return hodnota

def ukazRuky(playerHand, deelerHand, holeCard):
    rows = ["", "", "", "", ""]

    for i, karta in enumerate(playerHand):
        rows[0] += "___"
        if karta == "Hole" and holeCard:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "| ##| "
        else:
            rank, suit = karta
            rows[1] += "|{}  | ".format(rank.ljust(2))
            rows[2] += "| {} | ".format(suit)
            rows[3] += "|  {}| ".format(rank.rjust(2, "_"))

    print("\n".join(rows))

def getMove():
    while True:
        move = ["(H)it", "(S)tand"]
        movePrompt = ", ".join(move) + "> "
        tah = input(movePrompt).upper()
        if tah in ("H", "S"):
            return tah

if __name__ == "__main__":
    main()
