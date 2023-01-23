# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Yashin Offense: 1705.2 
3. Bart Defense: 1675.2 
4. Liveris Defense: 1673.6 
5. Liveris Average: 1669.5 
6. Koen Average: 1666.4 
7. Liveris Offense: 1665.4 
8. Yashin Average: 1660.2 
9. Loek Defense: 1652.8 
10. Job V Defense: 1639.2 
11. Yashin Defense: 1615.1 
12. Job V Offense: 1612.2 
13. Philip Offense: 1607.5 
14. Oliver Offense: 1580.8 
15. Bas Offense: 1577.9 
16. Carl Offense: 1566.4 
17. Martin Offense: 1564.4 
18. Bas Average: 1562.2 
19. Martin Average: 1556.6 
20. Job Offense: 1554.5 
21. Oliver Average: 1554.2 
22. Loek Average: 1554.2 
23. Carl Average: 1552.9 
24. Martin Defense: 1548.8 
25. Bas Defense: 1546.5 
26. Philip Average: 1544.8 
27. Carl Defense: 1539.4 
28. Bart Average: 1537.2 
29. Floris Offense: 1531.9 
30. Job Average: 1530.6 
31. Oliver Defense: 1527.6 
32. Mohammed Defense: 1526.9 
33. Jane Defense: 1525.0 
34. Maarten Defense: 1521.4 
35. Koen Defense: 1514.4 
36. Vincent Offense: 1511.8 
37. Job Defense: 1506.7 
38. Brian Offense: 1505.1 
39. Mohammed Average: 1503.8 
40. Frenk  Defense: 1503.3 
41. Job  Defense: 1496.7 
42. Floris Average: 1494.2 
43. Philip Defense: 1482.0 
44. Irene Offense: 1481.4 
45. Kassandra Defense: 1480.9 
46. Mohammed Offense: 1480.8 
47. Thomas Offense: 1476.3 
48. Frenk Offense: 1474.7 
49. Thomas Average: 1473.9 
50. Thomas Defense: 1471.5 
51. Frenk Average: 1469.6 
52. Maarten Average: 1468.5 
53. Bruno Defense: 1468.1 
54. Jelle Offense: 1468.0 
55. Frenk Defense: 1464.4 
56. Bruno Average: 1462.3 
57. Irene Average: 1460.2 
58. Floris Defense: 1456.5 
59. Bruno Offense: 1456.5 
60. Loek Offense: 1455.6 
61. Daan Ri Defense: 1445.4 
62. Irene Defense: 1439.1 
63. Jay Offense: 1439.1 
64. Wouter Offense: 1437.8 
65. Katherine Defense: 1434.9 
66. Daan Ri Offense: 1434.7 
67. Timo Defense: 1430.7 
68. Timo Average: 1428.1 
69. Timo Offense: 1425.5 
70. Dennis Offense: 1417.8 
71. Maarten Offense: 1415.6 
72. Kassandra Average: 1404.8 
73. Bart Offense: 1399.1 
74. Dennis Average: 1394.3 
75. Wouter Average: 1381.9 
76. Dennis Defense: 1370.8 
77. Donnie Defense: 1367.6 
78. Michiel Defense: 1349.4 
79. Donnie Average: 1343.0 
80. Kassandra Offense: 1328.8 
81. Wouter Defense: 1326.1 
82. Michiel Average: 1318.8 
83. Donnie Offense: 1318.5 
84. Michiel Offense: 1288.2 

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