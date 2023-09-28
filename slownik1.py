meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "CREEPY": "coś strasznego lub przyprawiającego o gęsią skórkę",
            "SZEŚĆDZIESIONA": "konfident, skarżypyta",
            "XD": "symbol,emotka oznaczjąca śmianie się",
            "REL": "właśnie tak, dokłanie itp",
            "CRUSH": "osoba w której się podkochujemy/po tajemnie podoba nam się",
            "RANDOM": "ktoś losowy/coś losowego"
            }
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("nie ma jeszcze takiego słowa")
