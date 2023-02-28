# Internal Fussball ratings at Transavia
## Ratings
1. Koen: 1829.3 
2. Bart: 1761.5 
3. Job V: 1753.1 
4. Loek: 1688.7 
5. Liveris: 1653.5 
6. Yashin: 1634.1 
7. Oliver: 1609.1 
8. Bas: 1562.0 
9. Job: 1550.3 
10. Tim: 1532.0 
11. Philip: 1529.8 
12. Carl: 1525.9 
13. Frenk : 1509.9 
14. Jane: 1509.5 
15. Martin: 1503.6 
16. Timo: 1492.2 
17. Job : 1490.1 
18. Floris: 1486.0 
19. Brian: 1485.9 
20. Thomas: 1482.3 
21. Maarten: 1478.5 
22. Mohammed: 1478.1 
23. Frenk: 1475.9 
24. Jelle: 1461.8 
25. Donnie: 1445.7 
26. Jay: 1442.5 
27. Irene: 1435.5 
28. Vincent: 1429.9 
29. Kassandra: 1426.5 
30. Bruno: 1423.2 
31. Daan Ri: 1412.7 
32. Laura: 1393.6 
33. Roy: 1384.3 
34. Katherine: 1377.5 
35. Dennis: 1347.5 
36. Wouter: 1300.2 
37. Michiel: 1197.8 

## Barto Rating
Ratings are based on the rating system named Barto which I developed during my Master's thesis. This thesis is included as pdf in barto.pdf. It can be seen as an extension of the Elo rating for games consisting out of smaller sub-games (contests) such as Tennis (sub-game either Sets, Games, or single points) or Fussball (sub-game every single point/goal scored)
## Terminology
- G: a game between 2 opposing teams (possibly consisting out of 1 player each) which is composed of multiple contests
- c: a contest modelled as a Bernoullia trial with the outcomes team A winning or team B.
- S: true level of a player with respect to winning a contest.
- mu: estimation of true level of a player. Also referred to as rating
- sigma_s: std. dev. of estimation of true level
- P: game performance
- sigma_p: std. dev. of game performance
- p_c: probability of winning a contest.
- B_p: scaling parameter. To decide what difference in ratings means what win percentage.
## Methodology
Every player has some rating mu (initialized at 1500) which is an estimation of the player's true level, S, with uncertainy sigma_s. When a player plays a game, they will not always play on their true level but we assume them to have good games and bad games. We model this with their game performance, P, which is a normal distribution with mean S and sigma_p. Now if two teams A and B are to play the skill of each team will be the sum of the ratings of the players in the team. Then the difference of the ratings between the teams determine the chance, p_c, of each player to win a contest. The whole game is then a Binomial distribution with N_c: the number of contests to be played, p_c the probability of team A to win a point, and x the number of contests won by team A. Additional subscripts show whether the terms refer to team A or B
- S ~ N(mu, sigma_s)
- P ~ N(S, sigma_p)
- p_c = 1 / (1 + exp(P_B - P_A) / B_p)
- G ~ B(N_c, x, p_c)

Using Bayesian statistic we determine the priors and after each single game we calculate the posterior for each true level difference between the teams. We then pick the true level difference which optimizes the posterior probability. This true level difference will then be split equally equally between the player. 

E.g. Team A consists out of a player 1 with 1400 rating and player 2 with 1500 rating, while team B consists out of player 3 with 1500 rating and player 4 with 1600 rating. The difference between the teams is then -100, meaning team 2 is expected to score more points. Let's say team 1 plays better than expected the posterior difference might be 80 instead of 100. Then we will update the players in team A with +5 points and in team B with -5 points making the posterior ratings: player 1 1405, player 2 1505, player 3 1495 and player 4 1595.