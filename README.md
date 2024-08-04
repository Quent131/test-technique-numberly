# test-technique-numberly

Ce projet est le test technique à destination de Numberly. Le but était de réaliser un programme permettant de générer des URL raccourcis. <br/>

## Prérequis

Ce projet a été créé en utilisant `Python 3.9.6`. <br/>
Docker est également nécessaire afin de faire tourner une instance `MySQL`. <br/>
[Transcrypt](https://github.com/elasticdog/transcrypt) a été utilisé afin de crypter les fichiers sensibles.

## Configuration

La première chose à faire est de décrypter les fichiers `.env` et `docker-compose.yml`. Pour se faire, il faut installer [Transcypt](https://github.com/elasticdog/transcrypt/blob/main/INSTALL.md), et lancer `transcrypt -c aes-256-cbc -p cle` où `cle` est la clé utilisée pour crypter les fichiers, que je transmettrais par email.<br/>
J'ai créé un `Makefile` pour les commandes importantes :

- `make db_setup` est la commande permettant d'initialiser la base de donnée et qui utilise `Docker` et `docker-compose`.

- `make setup` permet d'installer les différentes dépendances nécessaire au bon fonctionnement de l'application.

- `make run` permet de lancer l'application.

Comme souhaité, l'application dispose de 3 fonctionnalités :

- La réduction d'URL long
- L'expansion d'URL court vers l'URL long associé
- Les statistiques associées à un couple d'URL long-court
