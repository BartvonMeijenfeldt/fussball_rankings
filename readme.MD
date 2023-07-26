# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Brian Defense: 1715.7 
3. Brian Average: 1710.2 
4. Brian Offense: 1704.6 
5. Job V Defense: 1686.7 
6. Yashin Defense: 1682.2 
7. Yashin Average: 1679.8 
8. Yashin Offense: 1677.4 
9. Carl Offense: 1675.8 
10. Koen Average: 1666.4 
11. Carl Average: 1660.8 
12. Bas Defense: 1653.1 
13. Job Offense: 1651.2 
14. Bart Offense: 1646.1 
15. Carl Defense: 1645.7 
16. Liveris Defense: 1644.4 
17. Bart Average: 1637.4 
18. Bart Defense: 1628.8 
19. Tim Offense: 1625.1 
20. Job V Offense: 1611.5 
21. Liveris Average: 1606.6 
22. Timo Offense: 1603.4 
23. Martin Offense: 1602.1 
24. Loek Offense: 1593.1 
25. Philip Offense: 1583.5 
26. Oliver Offense: 1580.8 
27. Tim Average: 1571.6 
28. Liveris Offense: 1568.9 
29. Bas Average: 1564.4 
30. Job Average: 1563.6 
31. Philip  Defense: 1561.6 
32. Maarten Defense: 1554.2 
33. Oliver Average: 1554.2 
34. Loek Average: 1550.2 
35. Roy Defense: 1544.9 
36. Philip Average: 1540.0 
37. Floris Offense: 1531.9 
38. Martin Average: 1528.5 
39. Oliver Defense: 1527.6 
40. Mohammed Defense: 1526.9 
41. Jane Defense: 1525.0 
42. Timo Average: 1522.1 
43. Donnie Offense: 1520.0 
44. Tim Defense: 1518.0 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Thomas Offense: 1511.1 
48. Loek Defense: 1507.3 
49. Mohammed Average: 1503.8 
50. Frenk  Defense: 1503.3 
51. Thomas Average: 1501.8 
52. Donnie Average: 1499.0 
53. Job  Defense: 1496.7 
54. Philip Defense: 1496.4 
55. Floris Average: 1494.2 
56. Thomas Defense: 1492.5 
57. Brenda Defense: 1488.0 
58. Irene Offense: 1481.4 
59. Mohammed Offense: 1480.8 
60. Donnie Defense: 1477.9 
61. Daan Offense: 1477.7 
62. Job Defense: 1476.0 
63. Bas Offense: 1475.6 
64. Lars Defense: 1470.1 
65. Boele Offense: 1468.5 
66. Bruno Defense: 1468.1 
67. Jelle Offense: 1468.0 
68. Dennis Defense: 1464.6 
69. Bruno Average: 1462.3 
70. Irene Average: 1460.2 
71. Boele Average: 1459.5 
72. Arjen Offense: 1457.3 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Martin Defense: 1454.9 
76. Rob Offense: 1454.0 
77. Katherine Defense: 1452.9 
78. Kassandra Defense: 1451.4 
79. Boele Defense: 1450.5 
80. Daan Ri Defense: 1445.4 
81. Vincent Offense: 1445.2 
82. Andreea Offense: 1443.6 
83. Timo Defense: 1440.8 
84. Irene Defense: 1439.1 
85. Jay Offense: 1439.1 
86. Katherine Average: 1434.8 
87. Frenk Defense: 1434.7 
88. Maarten Average: 1434.6 
89. Dennis Average: 1432.6 
90. Wouter Offense: 1424.5 
91. Kassandra Average: 1422.2 
92. Anna Offense: 1421.9 
93. Frenk Average: 1416.8 
94. Katherine Offense: 1416.7 
95. Daan Ri Offense: 1413.7 
96. Rob Average: 1405.5 
97. Kristin Offense: 1403.2 
98. Dennis Offense: 1400.7 
99. Frenk Offense: 1399.0 
100. Wouter Average: 1398.2 
101. Laura Defense: 1394.0 
102. Kassandra Offense: 1393.0 
103. Anna Average: 1388.6 
104. Kristin Average: 1382.8 
105. Roy Average: 1377.8 
106. Laura Average: 1377.3 
107. Wouter Defense: 1372.0 
108. Kristin Defense: 1362.4 
109. Laura Offense: 1360.6 
110. Rob Defense: 1357.0 
111. Anna Defense: 1355.2 
112. Michiel Defense: 1349.4 
113. Michiel Average: 1318.8 
114. Maarten Offense: 1315.0 
115. Michiel Offense: 1288.2 
116. Roy Offense: 1210.8 

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