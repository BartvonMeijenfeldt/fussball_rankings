# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Defense: 1785.8 
3. Bart Offense: 1692.5 
4. Job V Defense: 1686.7 
5. Yashin Defense: 1682.2 
6. Yashin Average: 1679.8 
7. Yashin Offense: 1677.4 
8. Bart Average: 1675.8 
9. Liveris Defense: 1668.5 
10. Koen Average: 1666.4 
11. Brian Average: 1661.6 
12. Bart Defense: 1659.2 
13. Bas Defense: 1657.6 
14. Job Offense: 1641.2 
15. Job Average: 1625.2 
16. Tim Offense: 1625.1 
17. Martin Offense: 1624.4 
18. Job V Offense: 1611.5 
19. Liveris Average: 1610.2 
20. Job Defense: 1609.2 
21. Bas Average: 1604.1 
22. Timo Offense: 1603.4 
23. Carl Offense: 1599.5 
24. Carl Average: 1584.1 
25. Philip Offense: 1583.5 
26. Oliver Offense: 1580.8 
27. Tim Average: 1571.6 
28. Carl Defense: 1568.7 
29. Philip  Defense: 1561.6 
30. Maarten Defense: 1554.2 
31. Oliver Average: 1554.2 
32. Liveris Offense: 1552.0 
33. Bas Offense: 1550.6 
34. Brian Offense: 1537.3 
35. Floris Offense: 1531.9 
36. Oliver Defense: 1527.6 
37. Mohammed Defense: 1526.9 
38. Boele Offense: 1526.6 
39. Jane Defense: 1525.0 
40. Martin Average: 1523.2 
41. Timo Average: 1522.1 
42. Tim Defense: 1518.0 
43. Philip Average: 1514.8 
44. Koen Defense: 1514.4 
45. Luka Defense: 1513.7 
46. Thomas Offense: 1511.1 
47. Loek Defense: 1508.6 
48. Mohammed Average: 1503.8 
49. Frenk  Defense: 1503.3 
50. Thomas Average: 1501.8 
51. Anna Defense: 1500.4 
52. Job  Defense: 1496.7 
53. Loek Average: 1494.6 
54. Floris Average: 1494.2 
55. Thomas Defense: 1492.5 
56. Rob Offense: 1490.0 
57. Irene Offense: 1481.4 
58. Mohammed Offense: 1480.8 
59. Loek Offense: 1480.7 
60. Daan Offense: 1477.7 
61. Kassandra Offense: 1473.3 
62. Lars Defense: 1470.1 
63. Anna Average: 1468.5 
64. Bruno Defense: 1468.1 
65. Jelle Offense: 1468.0 
66. Bruno Average: 1462.3 
67. Rob Average: 1461.4 
68. Irene Average: 1460.2 
69. Donnie Defense: 1459.2 
70. Arjen Offense: 1457.3 
71. Donnie Average: 1456.6 
72. Floris Defense: 1456.5 
73. Bruno Offense: 1456.5 
74. Maarten Average: 1454.3 
75. Donnie Offense: 1454.1 
76. Philip Defense: 1446.2 
77. Daan Ri Defense: 1445.4 
78. Vincent Offense: 1445.2 
79. Timo Defense: 1440.8 
80. Irene Defense: 1439.1 
81. Jay Offense: 1439.1 
82. Anna Offense: 1436.6 
83. Frenk Defense: 1434.7 
84. Rob Defense: 1432.9 
85. Wouter Offense: 1429.5 
86. Martin Defense: 1422.0 
87. Roy Defense: 1421.6 
88. Kristin Offense: 1418.2 
89. Kassandra Average: 1418.0 
90. Frenk Average: 1416.8 
91. Katherine Offense: 1416.7 
92. Daan Ri Offense: 1413.7 
93. Katherine Average: 1409.4 
94. Katherine Defense: 1402.0 
95. Dennis Offense: 1400.9 
96. Frenk Offense: 1399.0 
97. Wouter Average: 1395.2 
98. Laura Defense: 1393.8 
99. Kristin Average: 1390.3 
100. Dennis Average: 1386.2 
101. Laura Average: 1377.2 
102. Dennis Defense: 1371.4 
103. Kassandra Defense: 1362.7 
104. Kristin Defense: 1362.4 
105. Wouter Defense: 1360.9 
106. Laura Offense: 1360.6 
107. Maarten Offense: 1354.4 
108. Michiel Defense: 1349.4 
109. Michiel Average: 1318.8 
110. Roy Average: 1316.2 
111. Michiel Offense: 1288.2 
112. Roy Offense: 1210.8 

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