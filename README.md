# ORGANIX-GESTION-DE-TACHES


---

# 🚀 **Organix – Application de Gestion de Tâches**

Organix est une application simple et efficace permettant aux utilisateurs **d’organiser, classer et prioriser leurs tâches** en fonction de leur **date d’échéance**, de leur **niveau de priorité**, et de leur **état d’avancement**.

---

## 📌 **Fonctionnalités principales**

### ✔️ **Gestion des tâches**

* Ajouter une nouvelle tâche
* Modifier une tâche existante
* Supprimer une tâche
* Marquer une tâche comme *en cours* ou *terminée*
* * Authentification des utilisateurs
* Tableau de bord avancé

### 🗂️ **Classification & tri**

* Trier les tâches par **date d’échéance**
* Trier par **priorité** (haute, moyenne, basse)
* Filtrer par **statut** (en cours, terminée)

### ⏰ **Rappels & échéances**

* Visualisation claire des deadlines
* Mise en avant des tâches urgentes

### 🎨 **Interface intuitive**

* Interface simple et ergonomique
* Navigation fluide
* Statistiques : nombre de tâches terminées, en cours, prioritaires…

---

## 🛠️ **Technologies utilisées**

| Composant          | Technologie                      |
| ------------------ | -------------------------------- |
| Backend            | Python / Django                  |
| Frontend           | HTML, CSS, JS / Django Templates |
| Base de données    | SQLite ou autre selon config     |
| Environnement      | Virtualenv (.venv)               |
| Gestion de version | Git & GitHub                     |

---

## 📁 **Structure du projet**

```
Organix/
│── tasks/              # Application principale
│── templates/          # Templates HTML
│── static/             # Fichiers CSS, JS, images
│── Organix/            # Réglages du projet Django
│── db.sqlite3          # Base de données
│── manage.py
│── requirements.txt
└── README.md
```

---

## ⚙️ **Installation & exécution**

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/HenoyxDxve/ORGANIX-GESTION-DE-TACHES.git
cd ORGANIX-GESTION-DE-TACHES
```

### 2️⃣ Créer l’environnement virtuel

```bash
python -m venv .venv
```

### 3️⃣ Activer l’environnement

**Windows :**

```bash
.venv\Scripts\activate
```

**Linux / Mac :**

```bash
source .venv/bin/activate
```

### 4️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5️⃣ Lancer le serveur

```bash
python manage.py runserver
```

L'application sera disponible à :
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 **Fonctionnalités à venir**
* Notification email pour les deadlines
* Mode sombre
* API REST

�
