# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Offense: 1794.7 
3. Carl Offense: 1765.2 
4. Brian Defense: 1762.5 
5. Bart Average: 1760.2 
6. Brian Average: 1751.0 
7. Brian Offense: 1739.6 
8. Bart Defense: 1725.6 
9. Carl Average: 1707.2 
10. Job V Defense: 1686.7 
11. Yashin Defense: 1682.2 
12. Yashin Average: 1679.8 
13. Yashin Offense: 1677.4 
14. Liveris Defense: 1677.3 
15. Koen Average: 1666.4 
16. Bas Defense: 1653.1 
17. Carl Defense: 1649.1 
18. Liveris Average: 1648.7 
19. Loek Offense: 1628.1 
20. Tim Offense: 1625.1 
21. Liveris Offense: 1620.1 
22. Job V Offense: 1611.5 
23. Timo Offense: 1603.4 
24. Martin Offense: 1602.1 
25. Loek Average: 1598.6 
26. Wouter Offense: 1592.6 
27. Job Defense: 1589.9 
28. Philip Offense: 1583.5 
29. Oliver Offense: 1574.2 
30. Donnie Offense: 1572.0 
31. Tim Average: 1571.6 
32. Loek Defense: 1569.1 
33. Bas Average: 1564.4 
34. Philip  Defense: 1561.6 
35. Job Average: 1550.9 
36. Oliver Average: 1550.9 
37. Philip Average: 1540.0 
38. Floris Offense: 1531.9 
39. Martin Average: 1528.5 
40. Oliver Defense: 1527.6 
41. Mohammed Defense: 1526.9 
42. Jane Defense: 1525.0 
43. Timo Average: 1522.1 
44. Tim Defense: 1518.0 
45. Koen Defense: 1514.4 
46. Luka Defense: 1513.7 
47. Job Offense: 1511.9 
48. Roy Defense: 1510.6 
49. Rob Offense: 1505.5 
50. Mohammed Average: 1503.8 
51. Frenk  Defense: 1503.3 
52. Katherine Defense: 1502.4 
53. Donnie Average: 1500.6 
54. Job  Defense: 1496.7 
55. Philip Defense: 1496.4 
56. Floris Average: 1494.2 
57. Thomas Defense: 1492.5 
58. Thomas Average: 1482.3 
59. Irene Offense: 1481.4 
60. Mohammed Offense: 1480.8 
61. Wouter Average: 1480.6 
62. Maarten Defense: 1477.7 
63. Daan Offense: 1477.7 
64. Bas Offense: 1475.6 
65. Thomas Offense: 1472.1 
66. Lars Defense: 1470.1 
67. Bruno Defense: 1468.1 
68. Jelle Offense: 1468.0 
69. Rob Average: 1462.8 
70. Bruno Average: 1462.3 
71. Irene Average: 1460.2 
72. Arjen Offense: 1457.3 
73. Floris Defense: 1456.5 
74. Bruno Offense: 1456.5 
75. Martin Defense: 1454.9 
76. Dennis Defense: 1451.4 
77. Kassandra Defense: 1451.4 
78. Daan Ri Defense: 1445.4 
79. Vincent Offense: 1445.2 
80. Boele Defense: 1445.1 
81. Andreea Offense: 1443.6 
82. Katherine Average: 1443.6 
83. Timo Defense: 1440.8 
84. Irene Defense: 1439.1 
85. Jay Offense: 1439.1 
86. Kassandra Average: 1436.6 
87. Frenk Defense: 1434.7 
88. Donnie Defense: 1429.1 
89. Brenda Offense: 1427.3 
90. Boele Average: 1426.1 
91. Laura Defense: 1424.5 
92. Kassandra Offense: 1421.7 
93. Rob Defense: 1420.2 
94. Frenk Average: 1416.8 
95. Daan Ri Offense: 1413.7 
96. Boele Offense: 1407.1 
97. Kristin Offense: 1403.2 
98. Frenk Offense: 1399.0 
99. Michiel Defense: 1397.7 
100. Maarten Average: 1396.4 
101. Dennis Average: 1395.3 
102. Laura Average: 1393.4 
103. Anna Offense: 1384.9 
104. Katherine Offense: 1384.7 
105. Kristin Average: 1382.8 
106. Brenda Average: 1378.0 
107. Roy Average: 1376.4 
108. Wouter Defense: 1368.7 
109. Kristin Defense: 1362.4 
110. Laura Offense: 1362.2 
111. Anna Average: 1349.6 
112. Dennis Offense: 1339.2 
113. Timo2 Defense: 1334.6 
114. Michiel Average: 1331.8 
115. Brenda Defense: 1328.8 
116. Maarten Offense: 1315.0 
117. Anna Defense: 1314.2 
118. Timo2 Average: 1306.9 
119. Timo2 Offense: 1279.2 
120. Michiel Offense: 1266.0 
121. Roy Offense: 1242.2 

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