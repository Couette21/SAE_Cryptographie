# SAE_Cryptographie

Le projet a été réalisé par :
- Axel Marchand/Couette21
- Théo Beausaert/Thorsyss

---

## **Introduction**

Notre objectif est d'explorer la faille de collision de MD5, en nous concentrant sur l'introduction théorique et pratique aux concepts de cryptographie.

---

## **Table des matières**

1. [**Présentation du hachage**](#présentation-du-hachage) 📜
2. [**Découverte des différentes fonctions en pratique**](#découverte-des-différentes-fonctions-en-pratique) 🔍
3. [**Programme de vérification de collision**](#programme-de-vérification-de-collision) 🛠️
4. [**Programme de création de collision**](#programme-de-création-de-collision) 🛠️
5. [**Paradoxe des anniversaires**](#paradoxe-des-anniversaires) 🎉
6. [**Craquage de mot de passe avec Hashcat**](#craquage-de-mot-de-passe-avec-hashcat) 💻
7. [**Craquage de mot de passe avec John the Ripper**](#Craquage-de-mot-de-passe-avec-John-the-Ripper) 🔍
8. [**Préparer l'attaque**](#préparer-lattaque) 🚀
    - [**Trouver une façon de s'introduire**](#trouver-une-façon-de-sintroduire) 🔍
    - [**Attaque**](#attaque) ⚔️
    - [**Rapport réussi 20/20**](#rapport-réussi-2020) 📊

---

## **Présentation du hachage**

Qu'est-ce que le hachage ?
Le hachage est une fonction cryptographique qui transforme une entrée (ou message) de taille variable en une sortie (ou hash) de taille fixe. Cette sortie est souvent représentée sous forme de chaîne de caractères hexadécimaux. Les fonctions de hachage sont largement utilisées en informatique pour des applications telles que la vérification de l'intégrité des données, le stockage sécurisé des mots de passe, et les signatures numériques.

---

## **Découverte des différentes fonctions en pratique**

Nous explorerons différentes fonctions de hachage et leur utilisation pratique pour comprendre leur fonctionnement et leurs limites.

---

## **Programme de vérification de collision**

Ce programme permet de vérifier si deux fichiers différents produisent le même hash MD5.

![Image Programme de vérification de collision](Captures/verif.png)

---

## **Programme de recherche de hash specifique**

Nous avons développé un programme pour rechercher un hash spécifique. Le principe est simple : créer un fichier contenant une pop-up, modifier le contenu sans altérer sa fonction de base, et ajouter des zéros afin que notre programme puisse trouver le hash spécifique.

![Image Programme de création de collision](images/creation_collision.png)

---

## **Paradoxe des anniversaires**

Le paradoxe des anniversaires montre qu'avec un nombre relativement faible de tentatives, il y a une probabilité élevée de trouver deux entrées avec le même hash.

![Image Paradoxe des anniversaires](Captures/Paradoxe.png)

---

## **Craquage de mot de passe avec Hashcat**

Hashcat est un outil puissant pour craquer les mots de passe en exploitant la puissance des GPU pour accélérer le processus.

![Craquage de mot de passe avec Hashcat](Captures/hashcat.png)

![Craquage de mot de passe avec Hashcat](Captures/hash2.png)

---
## **Craquage de mot de passe avec John the Ripper**

John the Ripper est un outil puissant pour craquer les mots de passe en utilisant des techniques de cryptanalyse et de force brute pour identifier les mots de passe à partir de leurs hachages. Cet outil est flexible et peut être utilisé sur une variété de systèmes pour effectuer des attaques par dictionnaire, par force brute et basées sur des règles.

![Craquage de mot de passe avec John the Ripper](Captures/crack_hash.png)

---

## **Préparer l'attaque**

### **Trouver une façon de s'introduire**

Nous explorerons différentes méthodes d'attaque, y compris l'exploitation de mises à jour de système ou d'applications et les vulnérabilités de gestion de mots de passe. L'objectif est d'identifier les points faibles dans les systèmes de sécurité actuels.

### **Attaque**

Nous mettrons en pratique les concepts appris pour simuler des attaques et évaluer leur succès.

### **Rapport réussi 20/20**

Nous conclurons notre projet en partageant nos résultats et en tirant des conclusions sur la sécurité des systèmes utilisant MD5.



