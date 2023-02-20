# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1753.3 
3. Liveris Offense: 1711.2 
4. Job V Defense: 1686.7 
5. Liveris Average: 1668.4 
6. Koen Average: 1666.4 
7. Loek Defense: 1663.2 
8. Bas Offense: 1635.2 
9. Yashin Defense: 1634.5 
10. Bart Average: 1630.0 
11. Liveris Defense: 1625.5 
12. Job V Offense: 1611.5 
13. Philip Offense: 1606.1 
14. Bas Average: 1604.4 
15. Yashin Average: 1601.0 
16. Oliver Offense: 1580.8 
17. Loek Average: 1576.6 
18. Bas Defense: 1573.7 
19. Yashin Offense: 1567.4 
20. Martin Offense: 1564.4 
21. Oliver Average: 1554.2 
22. Carl Offense: 1549.5 
23. Carl Average: 1544.4 
24. Martin Average: 1543.8 
25. Job Offense: 1541.4 
26. Maarten Defense: 1541.4 
27. Timo Offense: 1540.7 
28. Carl Defense: 1539.4 
29. Floris Offense: 1531.9 
30. Oliver Defense: 1527.6 
31. Philip Average: 1527.2 
32. Mohammed Defense: 1526.9 
33. Jane Defense: 1525.0 
34. Job Average: 1524.1 
35. Martin Defense: 1523.1 
36. Koen Defense: 1514.4 
37. Bart Offense: 1506.8 
38. Job Defense: 1506.7 
39. Mohammed Average: 1503.8 
40. Frenk  Defense: 1503.3 
41. Job  Defense: 1496.7 
42. Floris Average: 1494.2 
43. Timo Average: 1494.0 
44. Roy Defense: 1490.7 
45. Loek Offense: 1490.0 
46. Frenk Defense: 1488.6 
47. Frenk Average: 1481.6 
48. Irene Offense: 1481.4 
49. Mohammed Offense: 1480.8 
50. Vincent Offense: 1478.8 
51. Maarten Average: 1478.5 
52. Thomas Offense: 1476.3 
53. Frenk Offense: 1474.7 
54. Thomas Average: 1473.9 
55. Thomas Defense: 1471.5 
56. Katherine Offense: 1468.5 
57. Bruno Defense: 1468.1 
58. Jelle Offense: 1468.0 
59. Brian Offense: 1466.4 
60. Bruno Average: 1462.3 
61. Irene Average: 1460.2 
62. Floris Defense: 1456.5 
63. Bruno Offense: 1456.5 
64. Roy Average: 1454.8 
65. Laura Offense: 1450.4 
66. Philip Defense: 1448.3 
67. Timo Defense: 1447.3 
68. Daan Ri Defense: 1445.4 
69. Irene Defense: 1439.1 
70. Jay Offense: 1439.1 
71. Daan Ri Offense: 1434.7 
72. Katherine Average: 1430.9 
73. Roy Offense: 1418.8 
74. Maarten Offense: 1415.6 
75. Kassandra Defense: 1414.2 
76. Dennis Defense: 1402.6 
77. Dennis Average: 1401.8 
78. Dennis Offense: 1400.9 
79. Kassandra Average: 1396.8 
80. Katherine Defense: 1393.3 
81. Donnie Offense: 1386.3 
82. Wouter Offense: 1379.7 
83. Kassandra Offense: 1379.5 
84. Donnie Average: 1376.9 
85. Donnie Defense: 1367.6 
86. Michiel Defense: 1349.4 
87. Wouter Average: 1327.8 
88. Michiel Average: 1318.8 
89. Michiel Offense: 1288.2 
90. Wouter Defense: 1276.0 

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