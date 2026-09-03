# Chaîne de Recherche Retenue pour Dimensions AI (2006 – 2026)

**Projet :** Analyse Bibliométrique sur la Traduction Automatique et Parole-à-Parole (*Speech-to-Speech*)  
**Période couverte :** 2006 – 2026 (20 ans)  
**Base de données :** Dimensions AI  
**Type de requête :** Requête globale élargie (Option 1)  

---

## 1. Requête Brute Prête à Copier-Coller dans Dimensions AI

```text
("machine translation" OR "neural machine translation" OR "statistical machine translation" OR "speech-to-speech translation" OR "speech-to-speech" OR "speech to speech" OR "voice-to-voice translation" OR "voice to voice" OR "speech translation" OR "spoken language translation" OR "direct speech translation" OR "cascaded speech translation" OR "automatic translation")
```

---

## 2. Décomposition et Rationale des Termes Inclus

| Groupe de Termes | Termes Inclus dans la Requête | Justification & Couverture Temporale |
| :--- | :--- | :--- |
| **Traduction Automatique Classique & Neuronale** | `"machine translation"`, `"neural machine translation"`, `"statistical machine translation"`, `"automatic translation"` | Capturer l'évolution historique globale depuis la traduction basée sur des règles et la SMT (2006-2014) jusqu'à la NMT neuronale (2014-2026). |
| **Traduction Vocale / Parole-à-Parole (S2S)** | `"speech-to-speech translation"`, `"speech-to-speech"`, `"speech to speech"`, `"voice-to-voice translation"`, `"voice to voice"` | Cibler spécifiquement les approches qui traduisent directement la voix/parole d'une langue vers une autre. |
| **Traduction de la Parole (Speech Translation)** | `"speech translation"`, `"spoken language translation"`, `"direct speech translation"`, `"cascaded speech translation"` | Englober à la fois les approches en cascade (*ASR $\rightarrow$ MT $\rightarrow$ TTS*) et les approches directes unifiées (*End-to-End S2S*). |

---

## 3. Configuration des Filtres dans l'Interface Dimensions AI

Pour garantir la qualité et la reproductibilité du corpus bibliométrique, appliquez les filtres suivants dans l'interface de **Dimensions AI** :

1. **Champ de recherche (*Search Field*) :**  
   Sélectionner **`Title and Abstract`** (Titre et Résumé).  
   *(Éviter "Full data" qui génère du bruit non pertinent).*

2. **Années de publication (*Publication Year*) :**  
   Filtrer sur l'intervalle **`2006` à `2026`** (20 ans).

3. **Type de document (*Document Type*) :**  
   Sélectionner **`Article`** ET **`Proceeding`** (Actes de conférences).  
   *(En TAL/IA, les conférences majeures comme ACL, EMNLP, Interspeech, ICASSP et NeurIPS sont publiées sous forme de Proceedings).*

4. **Domaines de recherche (*Fields of Research - FOR 2020*) :**  
   *(Optionnel si le corpus reste très ciblé)* :  
   - `46 Information and Computing Sciences` (et sous-catégories `4602 Artificial Intelligence`, `4611 Software Engineering`)  
   - `47 Language, Communication and Culture` (`4704 Linguistics`).

---

## 4. Étapes Suivantes pour la Collecte des Données

1. Exécuter la requête dans **Dimensions AI**.
2. Noter le nombre total de résultats obtenus (Volume brut).
3. Exporter les données au format **CSV** ou **BibTeX** (comprenant les titres, résumés, auteurs, affiliations, citations, mots-clés et références citées).
4. Importer le fichier exporté dans **R / Bibliometrix (`Biblioshiny`)** pour débuter le nettoyage et les analyses statistiques.
