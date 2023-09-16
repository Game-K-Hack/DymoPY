<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/DymoPY/master/images/icon.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.0" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=Stable&color=green" alt="Version - Stable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
</div>

<h4 align="center">DymoPY</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a>
</p>

<br>
<br>

## Description

**DymoPY** est une application Python qui permet d'imprimer des étiquettes à partir de fichiers texte en utilisant une imprimante Dymo LabelWriter. Il est conçu pour automatiser le processus d'impression d'étiquettes à partir de fichiers dans un dossier spécifié.

<br>

## Usage

Pour utiliser DymoPY, suivez ces étapes :
1. Assurez-vous d'avoir installé toutes les dépendances répertoriées dans `requirements.txt`.
2. Configurez vos préférences dans le fichier `config.yml`. Vous devrez spécifier le nom de votre imprimante, le chemin du fichier d'étiquette et le dossier de scan.
3. Exécutez le fichier `main.py` pour lancer l'application.
4. L'application surveillera en permanence le dossier de scan. Lorsqu'elle détecte un fichier correspondant à l'extension spécifiée dans la configuration, elle créera une étiquette temporaire en remplaçant un texte balisé dans le fichier d'étiquette par le code extrait du nom du fichier. Ensuite, elle enverra cette étiquette à l'imprimante Dymo.
5. Une fois que l'étiquette a été imprimée avec succès, le fichier source dans le dossier de scan sera supprimé.

<br>

## Configuration

Le fichier `config.yml` contient les paramètres de configuration de l'application :
- `default`: Vous pouvez spécifier les valeurs par défaut pour l'imprimante, le fichier d'étiquette et le dossier de scan.
- `gui`: Vous pouvez personnaliser la taille des zones de saisie dans l'interface graphique.
- `config`: Vous pouvez configurer le chemin du fichier de profil, les balises de texte à remplacer dans le fichier d'étiquette et l'extension de fichier à surveiller.

Assurez-vous de configurer ces valeurs selon vos besoins avant d'exécuter l'application.

<br>

## Bonus

Dans cette section, l'auteur du projet mentionne des fonctionnalités bonus ou des outils supplémentaires inclus dans le projet. Il s'agit apparemment de fichiers batch (scripts Windows) qui sont conçus pour faciliter l'utilisation du logiciel.

- `INSTALLATION.bat` *(bientôt)*: Ce fichier batch est destiné à simplifier le processus d'installation du logiciel. Plus précisément, il permet de créer un nouvel environnement Python (un environnement virtuel, probablement) et d'installer les dépendances requises pour exécuter le logiciel. Cela peut être utile pour les utilisateurs qui ne sont pas familiers avec la configuration de l'environnement Python et souhaitent un processus d'installation automatisé.

- `START.bat` : Ce fichier batch est conçu pour simplifier le lancement du logiciel. Il permet aux utilisateurs de lancer le logiciel sans avoir à ouvrir et à maintenir une fenêtre de commande (CMD) ouverte. Cela peut être pratique car cela évite aux utilisateurs de devoir saisir manuellement des commandes pour exécuter le logiciel.
