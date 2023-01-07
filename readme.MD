# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Loek Defense: 1685.7 
3. Liveris Offense: 1666.2 
4. Liveris Defense: 1643.6 
5. Job V Defense: 1639.2 
6. Yashin Offense: 1635.4 
7. Yashin Defense: 1629.6 
8. Job V Offense: 1612.2 
9. Bart Defense: 1609.2 
10. Bas Offense: 1606.8 
11. Carl Offense: 1597.7 
12. Philip Offense: 1596.1 
13. Oliver Offense: 1580.8 
14. Martin Defense: 1572.9 
15. Job Offense: 1554.5 
16. Carl Defense: 1539.4 
17. Bas Defense: 1538.1 
18. Martin Offense: 1534.3 
19. Floris Offense: 1531.9 
20. Oliver Defense: 1527.6 
21. Mohammed Defense: 1526.9 
22. Jane Defense: 1525.0 
23. Koen Defense: 1514.4 
24. Vincent Offense: 1511.8 
25. Job Defense: 1506.7 
26. Frenk  Defense: 1503.3 
27. Job  Defense: 1496.7 
28. Brian Offense: 1489.3 
29. Philip Defense: 1485.9 
30. Thomas Offense: 1484.7 
31. Irene Offense: 1481.4 
32. Mohammed Offense: 1480.8 
33. Frenk Offense: 1474.7 
34. Timo Offense: 1473.3 
35. Thomas Defense: 1469.0 
36. Bruno Defense: 1468.1 
37. Jelle Offense: 1468.0 
38. Frenk Defense: 1464.4 
39. Maarten Offense: 1463.1 
40. Timo Defense: 1458.2 
41. Floris Defense: 1456.5 
42. Bruno Offense: 1456.5 
43. Kassandra Defense: 1455.9 
44. Loek Offense: 1455.6 
45. Wouter Offense: 1451.0 
46. Daan Ri Defense: 1445.4 
47. Irene Defense: 1439.1 
48. Jay Offense: 1439.1 
49. Daan Ri Offense: 1434.7 
50. Kathrine Defense: 1425.9 
51. Dennis Offense: 1417.8 
52. Donnie Defense: 1398.9 
53. Dennis Defense: 1379.0 
54. Bart Offense: 1354.0 
55. Michiel Defense: 1349.4 
56. Wouter Defense: 1346.0 
57. Donnie Offense: 1321.2 
58. Kassandra Offense: 1320.4 
59. Michiel Offense: 1288.2 

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
Every player has some rating mu, both for offense and defense (initialized at 1500), which is an estimation of the player's true level, S, with uncertainy sigma_s. When a player plays a game, they will not always play on their true level but we assume them to have good games and bad games. We model this with their game performance, P, which is a normal distribution with mean S and sigma_p. Now if two teams A and B are to play the skill of each team will be the sum of the ratings of the players in the team. Then the difference of the ratings between the teams determine the chance, p_c, of each player to win a contest. The whole game is then a Binomial distribution with N_c: the number of contests to be played, p_c the probability of team A to win a point, and x the number of contests won by team A. Additional subscripts show whether the terms refer to team A or B
- S ~ N(mu, sigma_s)
- P ~ N(S, sigma_p)
- p_c = 1 / (1 + exp(P_B - P_A) / B_p)
- G ~ B(N_c, x, p_c)

Using Bayesian statistic we determine the priors and after each single game we calculate the posterior for each true level difference between the teams. We then pick the true level difference which optimizes the posterior probability. This true level difference will then be split equally equally between the player. 

E.g. Team A consists out of a player 1 with 1400 rating and player 2 with 1500 rating, while team B consists out of player 3 with 1500 rating and player 4 with 1600 rating. The difference between the teams is then -100, meaning team 2 is expected to score more points. Let's say team 1 plays better than expected the posterior difference might be 80 instead of 100. Then we will update the players in team A with +5 points and in team B with -5 points making the posterior ratings: player 1 1405, player 2 1505, player 3 1495 and player 4 1595.