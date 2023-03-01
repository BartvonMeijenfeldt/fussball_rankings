# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1808.9 
3. Liveris Offense: 1713.0 
4. Job V Defense: 1686.7 
5. Liveris Average: 1669.2 
6. Koen Average: 1666.4 
7. Bart Average: 1656.1 
8. Loek Defense: 1641.6 
9. Bas Offense: 1629.4 
10. Liveris Defense: 1625.5 
11. Philip Offense: 1624.7 
12. Yashin Defense: 1614.1 
13. Job V Offense: 1611.5 
14. Bas Average: 1599.9 
15. Martin Offense: 1589.3 
16. Yashin Average: 1589.1 
17. Carl Defense: 1588.3 
18. Oliver Offense: 1580.8 
19. Bas Defense: 1570.4 
20. Carl Average: 1568.9 
21. Yashin Offense: 1564.1 
22. Philip  Defense: 1561.6 
23. Loek Average: 1561.2 
24. Job Offense: 1556.4 
25. Oliver Average: 1554.2 
26. Carl Offense: 1549.5 
27. Philip Average: 1547.3 
28. Timo Offense: 1544.7 
29. Maarten Defense: 1541.4 
30. Floris Offense: 1531.9 
31. Job Average: 1531.6 
32. Oliver Defense: 1527.6 
33. Mohammed Defense: 1526.9 
34. Jane Defense: 1525.0 
35. Tim Offense: 1520.4 
36. Koen Defense: 1514.4 
37. Frenk Defense: 1510.3 
38. Job Defense: 1506.7 
39. Mohammed Average: 1503.8 
40. Bart Offense: 1503.3 
41. Frenk  Defense: 1503.3 
42. Timo Average: 1497.8 
43. Martin Average: 1497.5 
44. Job  Defense: 1496.7 
45. Floris Average: 1494.2 
46. Frenk Average: 1492.5 
47. Irene Offense: 1481.4 
48. Mohammed Offense: 1480.8 
49. Loek Offense: 1480.7 
50. Maarten Average: 1478.5 
51. Roy Defense: 1477.9 
52. Thomas Offense: 1476.3 
53. Frenk Offense: 1474.7 
54. Thomas Average: 1473.9 
55. Thomas Defense: 1471.5 
56. Philip Defense: 1469.9 
57. Katherine Offense: 1468.5 
58. Bruno Defense: 1468.1 
59. Jelle Offense: 1468.0 
60. Brian Offense: 1466.4 
61. Vincent Offense: 1463.8 
62. Bruno Average: 1462.3 
63. Irene Average: 1460.2 
64. Floris Defense: 1456.5 
65. Bruno Offense: 1456.5 
66. Timo Defense: 1450.9 
67. Daan Ri Defense: 1445.4 
68. Irene Defense: 1439.1 
69. Jay Offense: 1439.1 
70. Roy Average: 1437.5 
71. Daan Ri Offense: 1434.7 
72. Katherine Average: 1430.9 
73. Donnie Offense: 1416.1 
74. Maarten Offense: 1415.6 
75. Martin Defense: 1405.7 
76. Kassandra Defense: 1405.7 
77. Dennis Offense: 1400.9 
78. Laura Offense: 1398.1 
79. Roy Offense: 1397.1 
80. Donnie Average: 1394.5 
81. Katherine Defense: 1393.3 
82. Kassandra Average: 1392.6 
83. Dennis Average: 1384.6 
84. Kassandra Offense: 1379.5 
85. Wouter Offense: 1376.1 
86. Donnie Defense: 1372.9 
87. Dennis Defense: 1368.3 
88. Michiel Defense: 1349.4 
89. Wouter Average: 1326.0 
90. Michiel Average: 1318.8 
91. Michiel Offense: 1288.2 
92. Wouter Defense: 1276.0 

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