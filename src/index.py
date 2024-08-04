from db import db
from utils import clear, shorten_url, expand_url, get_url_stats


def main():
    while 1:
        functionnality = input(
            "Quelle fonctionnalité souhaitez-vous utiliser ?\n1. Raccourcir un URL\n2. Développer un URL\n3. Obtenir les stats d'un URL\n4. Quitter\n"
        )
        try:
            functionnality = int(functionnality)
            if functionnality == 1:
                url = input("Entrez l'URL à raccourcir : ")
                print(
                    "L'URL {url} est maintenant associé à l'URL raccourci : {shorten}".format(
                        shorten=shorten_url(url), url=url
                    )
                )
            elif functionnality == 2:
                url = input("Entrez l'URL à développer : ")
                print(
                    "L'URL raccourci {url} est associé à l'URL ${long_url}".format(
                        url=url, long_url=expand_url(url)
                    )
                )
            elif functionnality == 3:
                url = input("Entrez l'URL dont vous voulez obtenir les statistiques : ")
                print(get_url_stats(url))
            elif functionnality == 4:
                break
            else:
                print("Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            clear()
            print("Veuillez entrer un nombre entre 1 et 4.")
        except Exception as e:
            print(e)
    db.close()


main()
