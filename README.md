# projetServeur 2025

## 👨‍💻Binome : Syrine BEN HASSINE / Jean-baptiste LARGERON

## 🏷️Badges
![Static Badge](https://img.shields.io/badge/Python-3.12-green)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Repo size](https://img.shields.io/github/repo-size/Syrinbh/projetServeur)
![Last commit](https://img.shields.io/github/last-commit/Syrinbh/projetServeur)




## 📦 Installation

Vous pouvez installer le site web via le fichier.zip que nous vous avons soumis
ou en utilisant git:

`git clone https://github.com/Syrinbh/projetServeur.git`


## 📝 Resumé du Projet

### 🎯 Objectifs du projet 

    Le projet à pour but de manipuler le framework Django utilisant une interface WSGI (Web Server Gateway Interface)
    Le principal avantage étant la facilité de déploiement pour n'importe quel environnement web Python

    Nous avions pour but de faire un site, permettant de manipuler des équipes et des tâches. 



    Un utilisateur doit pouvoir se connecter /se déconnecter / s'enregistrer ainsi que de rejoindre une équipe ou d'en créer une
  

    Un utilisateur peut créer une tâche à assignée a une équipe. Nous avons fait le choix que n'importe quel utilisateur puisse le faire. Cependant,
    nous aurions pu restreindre cela aux superutilisateur uniquement (dans le cadre d'une entreprise par exemple ou seul les managers pourrait créer
    une tâche et les affiliées aux équipes comme nous l'avons fait pour la suppression d'équipe)

    Un utilisateur peut voir le profile des équipes, contenant les tâches qui leurs sont assignées ainsi que les membres qui la composent
    Un utilisateur peut quitter une équipe à tout moment.

    Une tâche doit pouvoir être modifiable

### 🛠️ Choix de notre part

    Le cahier des charges ne spécifiait pas de contraintes particulières concernant l’aspect graphique de l’application, nous avons tout de même
    fait le choix d'implémenter un fichier css afin de proposer une application propre, ergonomique et fluide

    Nous avons fait le choix de donner le droit à la suppression d'une équipe aux superutilisateurs (admin) uniquement pour éviter les suppressions accidentelles par des membres non autorisés.

    Le système ne fait pas de distinction entre un créateur d’équipe et un simple membre (pas de rôle "chef d’équipe"). Cela a été un choix de simplification pour se concentrer sur la gestion des tâches.

    Vous trouverez ci-dessous les tableaux des fonctionnalités de chaque page ainsi qu'une vision de l'ensemble de la structure du projet

### 💡 Pistes d'amélioration

    Ajout d’un système de rôles (admin / membre / manager)

    Ajout d’un système de validation pour les tâches.

    Intégration d’un système de notifications (ex : email quand une tâche est assignée)


## 🌐 Routes Principales


### 🌳 Arbre de structure du projet

    Voici l'arbre de structure du projet afin d'avoir un visuel global de la structure des fichiers du projet


        projetServeur
        ├── db.sqlite3
        ├── manage.py
        ├── monProjet
        │   ├── asgi.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── README.md
        └── tasks
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── __init__.py
            ├── migrations
            │   ├── 0001_initial.py
            │   ├── 0002_remove_user_name.py
            │   ├── 0003_task_parenttask_task_sontask_alter_task_description_and_more.py
            │   ├── 0004_creattask.py
            │   ├── 0005_remove_task_parenttask_remove_task_sontask_and_more.py
            │   ├── 0006_task_private.py
            │   ├── 0007_team_members_team_task_list_alter_task_statut.py
            │   ├── 0008_alter_user_email.py
            │   ├── 0009_alter_team_members_alter_user_email.py
            │   ├── 0010_alter_task_assignedteams.py
            │   ├── __init__.py
            │   └── __pycache__
            ├── models.py
            ├── __pycache__
            ├── static
            │   └── styles.css
            ├── templates
            │   └── tasks
            │       ├── Create_task.html
            │       ├── Create_team.html
            │       ├── Delete_task.html
            │       ├── Delete_team.html
            │       ├── home.html
            │       ├── Join_team.html
            │       ├── List_task.html
            │       ├── List_team.html
            │       ├── login.html
            │       ├── member_profile.html
            │       ├── Quit_team.html
            │       ├── register.html
            │       ├── team_profile.html
            │       └── Update_task.html
            ├── tests.py
            ├── urls.py
            └── views.py

## Recapitulatif des fonctions proposées

### 🔒Authentification Required

| URL                      | Méthode    |Description                   | Authentification Requise |
|--------------------------|------------|------------------------------|--------------------------|
| `/register/`             | GET/POST   | Inscription utilisateur      |           Non            |
| `/listTeam/`             | GET        | Lister les équipes           |           Non            |
| `/login/`                | GET/POST   | Connexion                    |           Oui            |
| `/logout/`               | GET        | Déconnexion                  |           Oui            |
| `/create/`               | GET/POST   | Créer une nouvelle tâche     |           Oui            |
| `/list/`                 | GET        | Lister toutes les tâches     |           Oui            |
| `/update/<int:task_id>/` | GET/POST   | Modifier une tâche existante |           Oui            |
| `/delete/<int:task_id>/` | POST       | Supprimer une tâche          |           Oui            |
| `/createTeam/`           | GET/POST   | Créer une nouvelle équipe    |           Oui            |
| `/joinTeam/`             | POST       | Rejoindre une équipe         |           Oui            |
| `/quitTeam/<int:team_id>`| POST       | Quitter une équipe           |           Oui            |
| `/deleteTeam/`           | POST       | Supprimer une équipe         |           Oui            |


### ✅ Gestion des Tâches 

| URL                      | Méthode  | Description                  | Paramètres |
|--------------------------|----------|------------------------------|------------|
| `/create/`               | GET/POST | Créer une nouvelle tâche     |     -      |
| `/list/`                 | GET      | Lister toutes les tâches     |     -      |
| `/update/<int:task_id>/` | GET/POST | Modifier une tâche existante | `task_id`  |
| `/delete/<int:task_id>/` | POST     | Supprimer une tâche          | `task_id`  |


### 👥 Gestion des Équipes

| URL                       | Méthode  | Description               | Paramètres |
|---------------------------|----------|---------------------------|------------|
| `/createTeam/`            | GET/POST | Créer une nouvelle équipe |      -     |
| `/joinTeam/`              | POST     | Rejoindre une équipe      |      -     |
| `/quitTeam/<int:team_id>` | POST     | Quitter une équipe        | `team_id ` |
| `/deleteTeam/`            | POST     | Supprimer une équipe      |      -     |
| `/listTeam/`              | GET      | Lister les équipes        |      -     |


## 💻 Technologies utilisées
    Django,HTML/CSS, Python 3.12, SQLite