# projetServeur
Projet serveur 2025
Binome : Syrine BEN HASSINE / Jean-baptiste LARGERON
# Web Serveur - Documentation des Routes

## 🌐 Routes Principales
# explication architecture , page d'accueil : creer page , .. 
### Authentification
| URL | Méthode | Description | Authentification Requise |
|-----|---------|-------------|---------------------------|
| `/register/` | GET/POST | Inscription utilisateur | Non |
| `/login/` | GET/POST | Connexion | Oui |
| `/logout/` | GET | Déconnexion | Oui |

### Gestion des Tâches
| URL | Méthode | Description | Paramètres |
|-----|---------|-------------|------------|
| `/create/` | GET/POST | Créer une nouvelle tâche | - |
| `/list/` | GET | Lister toutes les tâches | - |
| `/update/<int:task_id>/` | GET/POST | Modifier une tâche existante | `task_id` |
| `/delete/<int:task_id>/` | POST | Supprimer une tâche | `task_id` |

### Gestion des Équipes
| URL | Méthode | Description | Paramètres |
|-----|---------|-------------|------------|
| `/createTeam/` | GET/POST | Créer une nouvelle équipe | - |
| `/joinTeam/` | POST | Rejoindre une équipe | - |
| `/quitTeam/<int:team_id>` | POST | Quitter une équipe | `team_id` |
| `/deleteTeam/` | POST | Supprimer une équipe | - |
| `/listTeam/` | GET | Lister les équipes | - |
