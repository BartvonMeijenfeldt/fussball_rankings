# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Loek Defense: 1689.6 
3. Bart Defense: 1688.4 
4. Liveris Offense: 1680.7 
5. Yashin Offense: 1642.3 
6. Job V Defense: 1639.2 
7. Yashin Defense: 1613.6 
8. Job V Offense: 1612.2 
9. Liveris Defense: 1608.3 
10. Philip Offense: 1607.5 
11. Oliver Offense: 1580.8 
12. Bas Offense: 1577.9 
13. Carl Offense: 1566.4 
14. Martin Offense: 1564.4 
15. Job Offense: 1554.5 
16. Martin Defense: 1548.8 
17. Bas Defense: 1546.5 
18. Carl Defense: 1539.4 
19. Floris Offense: 1531.9 
20. Oliver Defense: 1527.6 
21. Mohammed Defense: 1526.9 
22. Maarten Defense: 1525.3 
23. Jane Defense: 1525.0 
24. Koen Defense: 1514.4 
25. Vincent Offense: 1511.8 
26. Job Defense: 1506.7 
27. Brian Offense: 1505.1 
28. Frenk  Defense: 1503.3 
29. Job  Defense: 1496.7 
30. Philip Defense: 1482.0 
31. Irene Offense: 1481.4 
32. Kassandra Defense: 1480.9 
33. Mohammed Offense: 1480.8 
34. Thomas Offense: 1476.3 
35. Frenk Offense: 1474.7 
36. Thomas Defense: 1471.5 
37. Bruno Defense: 1468.1 
38. Jelle Offense: 1468.0 
39. Frenk Defense: 1464.4 
40. Floris Defense: 1456.5 
41. Bruno Offense: 1456.5 
42. Loek Offense: 1455.6 
43. Wouter Offense: 1451.0 
44. Katherine Defense: 1450.2 
45. Daan Ri Defense: 1445.4 
46. Irene Defense: 1439.1 
47. Jay Offense: 1439.1 
48. Bart Offense: 1435.0 
49. Daan Ri Offense: 1434.7 
50. Timo Defense: 1428.3 
51. Timo Offense: 1424.0 
52. Dennis Offense: 1417.8 
53. Maarten Offense: 1415.6 
54. Dennis Defense: 1370.8 
55. Donnie Defense: 1367.6 
56. Michiel Defense: 1349.4 
57. Kassandra Offense: 1328.8 
58. Wouter Defense: 1326.1 
59. Donnie Offense: 1318.5 
60. Michiel Offense: 1288.2 

## Barto Rating
The Barto rating system extends the Elo rating system by taking the score into account. This results in more accurate estimation of strengths of players. Another interesting property is that if a heavy-favorite team or player plays against a weaker opponent, they are expected to score the majority of points. So if the favorite only wins a narrow victory the weaker team performed better than expected and will win rating and can therefore be seen as the winner. The ratings are based on the rating system named Barto which I developed during my Master's thesis which is included in pdf-form (see barto.pdf).
## Terminology
- G: a game between 2 opposing teams (possibly consisting out of 1 player each) which is composed of multiple contests.
- c: a contest (e.g. point in Fussball) modelled as a Bernoullia trial with the outcomes team A winning or team B.
- S: true level of a player with respect to winning a contest.
- mu: estimation of true level of a player. Also referred to as rating.
- sigma_s: std. dev. of estimation of true level.
- P: game performance.
- sigma_p: std. dev. of game performance.
- p_c: probability of winning a contest.
- B_p: scaling parameter. To decide what difference in ratings means what win percentage.
## Methodology
Every player has some rating mu both for offense and defense (initialized at 1500). These ratings are estimations of the player's true level, S, with uncertainy sigma_s. When a player plays a game, they will not always play on their true level but we assume them to have good games and bad games. We model this with their game performance, P, which is a normal distribution with mean S and sigma_p. Now if two teams A and B are to play the skill of each team will be the sum of the ratings of the players in the team (taking into account whether they are defense or offense). The difference of the ratings between the teams determine the chance, p_c, of each player to win a contest. The whole game is then a Binomial distribution with N_c: the number of contests to be played, p_c the probability of team A to win a point, and x the number of contests won by team A. Additional subscripts show whether the terms refer to team A or B
- S ~ N(mu, sigma_s)
- P ~ N(S, sigma_p)
- p_c = 1 / (1 + exp(P_B - P_A) / B_p)
- G ~ B(N_c, x, p_c)

Using Bayesian statistic we determine the priors and after each single game we calculate the posterior for each true level difference between the teams. The new rating difference is the true level difference for which the posterior probability is maximized. This difference will then be split equally equally between the player. 

E.g. Team A consists out of a player 1 with 1400 defense rating and player 2 with 1500 offense rating, while team B consists out of player 3 with 1500 defense rating and player 4 with offense 1600 rating. The difference between the teams is then -100, meaning team 2 is expected to score more points. Let's say team 1 plays better than expected the posterior difference might be 80 instead of 100. Then we will update the players in team A with +5 points and in team B with -5 points making the posterior ratings: player 1 1405, player 2 1505, player 3 1495 and player 4 1595.