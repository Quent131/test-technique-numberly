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
                shorten = shorten_url(url.strip())
                print(
                    "L'URL {url} est maintenant associé à l'URL raccourci : {shorten}".format(
                        shorten=shorten, url=url
                    )
                )
            elif functionnality == 2:
                url = input("Entrez l'URL à développer : ")
                long_url = expand_url(url.strip())
                print(
                    "L'URL raccourci {url} est associé à l'URL {long_url}".format(
                        url=url, long_url=long_url
                    )
                )
            elif functionnality == 3:
                url = input("Entrez l'URL dont vous voulez obtenir les statistiques : ")
                result = get_url_stats(url.strip())
                print(
                    "L'URL {long_url} est associé à l'URL {short_url} et a été consulté {redirection_count} fois".format(
                        **result
                    )
                )
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
