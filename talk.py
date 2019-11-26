class speach:
    initial_spich="Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave "  # default message at the start

class pairs:
    def get_pairs():
        pairs = [
            [
                # in line below You can find question to bot, on next line is answer
                r"nazywam się (.*)",
                ["Cześć %1, podasz mi swój login ?", ]
            ],
            [
                r"jak się nazywasz?|jak sie nazywasz?",
                ["Nazywam się Chatty i jestem chatbotem, ale będę Terminatorem", ]
            ],
            [
                r"jak się masz?",
                ["Wszytko dobrze\nA jak u Ciebie ?", ]
            ],
            [
                r"przepraszam (.*)",
                ["W porządku", "OK, nie ważne", ]
            ],
            [
                r"(.*) dobrze",
                ["Miło to słyszeć", "Super :)", ]
            ],
            [
                r"cześć|dzień dobry|siema",
                ["Cześć", "Dzień dobry", "Uszanowanko"]
            ],
            [
                r"(.*) wiek?| (.*) lat?",
                ["Jestem programem komputerowym koleś\nPoważnie o to mnie pytasz?", ]

            ],
            [
                r"chcesz (.*) ?",
                ["Złożyłeś mi ofertę, nie mogę odmówić", ]
            ],
            [
                r"(.*) stworzył?",
                ["Programista używający Python z biblioteką NLTK library ", "top secret ;)", ]
            ],
            [
                r"(.*) (lokalizacja|miasto|gdzie mieszkasz)?",
                ['Gdańsk, Polska', ]
            ],
            [
                r"jaka jest pogoda w (.*)?",
                ["Pogoda w %1 jest super jak zawsze", "Jest za gorąco dla mnie w %1", "Jest za zimno dla mnie w %1",]
            ],
            [
                r"pracuje w (.*)?",
                ["%1 jest wspaniałą firmą, słyszałem o tym.", ]
            ],
            [
                r"(.*) (sport|gra) ?",
                ["jestem wielkim fanem footballu", ]
            ],
            [
                r"kto (.*) sportowcem ?",
                ["Messy", "Ronaldo", "Roony"]
            ],
            [
                r"kto (.*) (gwiazdą filmową|aktorem)?",
                ["Brad Pitt"]
            ],
            [
                r"quit",
                ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
            ],
            ]

        return pairs