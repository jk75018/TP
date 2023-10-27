from question import Question

questions = [
    Question("Quelle équipe a remporté la Coupe du Monde de la FIFA 2018 ?", ["a) Brésil", "b) France", "c) Allemagne"], "b"),
    Question("Qui est le meilleur buteur de tous les temps en Coupe du Monde ?", ["a) Cristiano Ronaldo", "b) Lionel Messi", "c) Miroslav Klose"], "c"),
    Question("Dans quel pays est né le légendaire joueur de football Pelé ?", ["a) Brésil", "b) Argentine", "c) Portugal"], "a"),
    Question("Quelle équipe est surnommée les 'Blues' en Premier League anglaise ?", ["a) Manchester United", "b) Arsenal", "c) Chelsea"], "c"),
    Question("Combien de joueurs y a-t-il dans une équipe de football en temps normal ?", ["a) 10", "b) 11", "c) 12"], "b"),
    Question("Quelle équipe de football est surnommée 'Les Merengues' ?", ["a) FC Barcelone", "b) Real Madrid", "c) FC Séville"], "b"),
    Question("Quel pays a remporté le plus de Coupes du Monde de la FIFA dans l'histoire ?", ["a) Allemagne", "b) Brésil", "c) Argentine"], "b"),
    Question("Dans quel stade se joue la finale de la Ligue des champions de l'UEFA chaque année ?", ["a) Wembley", "b) Camp Nou", "c) Stade Olympique de Kiev"], "a"),
    Question("Qui a remporté le Ballon d'Or 2020 ?", ["a) Cristiano Ronaldo", "b) Lionel Messi", "c) Robert Lewandowski"], "c"),
    Question("Quelle équipe est surnommée les 'Red Devils' en Premier League anglaise ?", ["a) Liverpool", "b) Manchester City", "c) Manchester United"], "c"),
]

for question in questions:
    question.shuffle_options()
