# SAE_Cryptographie

Le projet a été réalisé par :
- Axel Marchand/Couette21
- Théo Beausaert/Thorsyss

---

## **Introduction**

Notre objectif est d'explorer la faille de collision de MD5 à des fins éducatives, en nous concentrant sur l'introduction théorique et pratique aux concepts de cryptographie.

---

## **Table des matières**

1. [**Présentation du hachage**](#présentation-du-hachage)
2. [**Découverte des différentes fonctions en pratique**](#découverte-des-différentes-fonctions-en-pratique)
3. [**Programme de vérification de collision**](#programme-de-vérification-de-collision)
4. [**Programme de création de collision**](#programme-de-création-de-collision)
5. [**Paradoxe des anniversaires**](#paradoxe-des-anniversaires)
6. [**Craquage de mot de passe avec Hashcat**](#craquage-de-mot-de-passe-avec-hashcat)
7. [**Essai avec DES**](#essai-avec-des)
8. [**Préparer l'attaque**](#préparer-lattaque)
    - [**Trouver une façon de s'introduire**](#trouver-une-façon-de-sintroduire)
    - [**Attaque**](#attaque)
    - [**Rapport réussi 20/20**](#rapport-réussi-2020)

---

## **Présentation du hachage**

Le hachage est une fonction cryptographique qui prend une entrée (ou message) et produit une sortie (ou hash) de taille fixe. MD5 est une fonction de hachage largement utilisée malgré ses vulnérabilités.

---

## **Découverte des différentes fonctions en pratique**

Nous explorerons différentes fonctions de hachage et leur utilisation pratique pour comprendre leur fonctionnement et leurs limites.

---

## **Programme de vérification de collision**

Ce programme permet de vérifier si deux fichiers différents produisent le même hash MD5.

---

## **Programme de création de collision**

Nous développerons un programme pour générer des collisions MD5, c'est-à-dire trouver deux entrées distinctes produisant le même hash MD5.

---

## **Paradoxe des anniversaires**

Le paradoxe des anniversaires montre qu'avec un nombre relativement faible de tentatives, il y a une probabilité élevée de trouver deux entrées avec le même hash.

---

## **Craquage de mot de passe avec Hashcat**

Hashcat est un outil puissant pour craquer les mots de passe en exploitant la puissance des GPU pour accélérer le processus.

---

## **Essai avec DES**

Le DES (Data Encryption Standard) est un ancien standard de chiffrement symétrique, bien qu'il soit obsolète pour les applications sécurisées.

---

## **Préparer l'attaque**

### **Trouver une façon de s'introduire**

Nous explorerons différentes méthodes d'attaque, y compris l'exploitation de mises à jour de système ou d'applications et les vulnérabilités de gestion de mots de passe.

### **Attaque**

Nous mettrons en pratique les concepts appris pour simuler des attaques et évaluer leur succès.

### **Rapport réussi 20/20**

Nous conclurons notre projet en partageant nos résultats et en tirant des conclusions sur la sécurité des systèmes utilisant MD5.

---

Ce fichier README.md est conçu pour fournir une introduction claire et un guide pratique sur chaque aspect exploré dans votre projet de cryptographie. Vous pouvez personnaliser les sections et les détails selon vos besoins spécifiques et ajouter des détails supplémentaires au fur et à mesure de l'avancement de votre projet.
