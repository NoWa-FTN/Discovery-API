Voici une version corrigée et mieux structurée de ton `README.md` pour qu'il soit clair et facile à suivre.

---

# Projet Flask API - Page de Connexion et Appel API

Ce projet est une petite application web utilisant Python (Flask) avec une page de connexion et un appel API externe. L'application permet de s'authentifier, d'accéder à une page d'accueil et de récupérer des données d'une API publique.

---

## Fonctionnalités

- Page de connexion avec gestion des sessions.
- Page d'accueil affichant un bouton pour récupérer des articles depuis une API publique.
- Appel API externe vers [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/).

---

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés :

- **Python 3.7 ou plus** (Python 3.10 recommandé).
- **pip** (inclus avec Python).
- **Git** (facultatif pour cloner le projet).

---

## Installation et Configuration

### Étapes sous **Linux** ou **Windows**

1. **Clonez le projet**  
   Si vous avez Git installé, clonez le dépôt GitHub. Sinon, téléchargez simplement le fichier ZIP du projet :
   ```bash
   git clone https://github.com/votre-utilisateur/projet-flask-api.git
   cd projet-flask-api
   ```

2. **Créez un environnement virtuel**  
   ```bash
   python -m venv venv
   ```

3. **Activez l'environnement virtuel**  
   - Sous **Linux/macOS** :
     ```bash
     source venv/bin/activate
     ```
   - Sous **Windows (cmd)** :
     ```bash
     venv\Scripts\activate
     ```
   - Sous **Windows (PowerShell)** :
     ```powershell
     .\venv\Scripts\Activate
     ```

4. **Installez les dépendances**  
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancez l'application**  
   ```bash
   python app.py
   ```

6. **Accédez à l'application dans votre navigateur**  
   Ouvrez [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Structure du Projet

```
projet-flask-api/
│
├── app.py              # Fichier principal de l'application Flask
├── requirements.txt    # Liste des dépendances Python
├── templates/          # Fichiers HTML
│   ├── index.html      # Page d'accueil
│   └── login.html      # Page de connexion
├── static/             # Fichiers statiques (CSS, JS, images)
│   └── style.css       # Style de base pour les pages
├── README.md           # Documentation du projet
└── venv/               # Environnement virtuel (non inclus dans Git)
```

---

## Dépendances

Les principales bibliothèques utilisées dans ce projet sont :

- **Flask** : Framework web léger pour Python.
- **Requests** : Pour effectuer des appels API externes.

Les dépendances sont listées dans le fichier `requirements.txt` :
```txt
Flask==2.2.3
requests==2.28.2
```

---

## Problèmes courants et solutions

1. **Erreur lors de l'import de `werkzeug`**  
   Si vous obtenez une erreur liée à `werkzeug` ou à une version incompatible de Flask, exécutez la commande suivante pour installer une version compatible :  
   ```bash
   pip install werkzeug==2.2.3
   ```

2. **Le bouton "Fetch Posts" ne fonctionne pas**  
   - Assurez-vous que le backend Flask est bien en cours d'exécution.
   - Vérifiez que l'endpoint `/api/posts` est accessible en testant directement :  
     [http://127.0.0.1:5000/api/posts](http://127.0.0.1:5000/api/posts).

3. **Problème avec l'environnement virtuel**  
   - Si l'environnement virtuel ne s'active pas, vérifiez que vous utilisez la commande correcte pour votre système d'exploitation (Linux/macOS/Windows).

---

## Auteur

**NoWa-FTN**  
[NoWa-FTN](https://github.com/NoWa-FTN)

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
```
