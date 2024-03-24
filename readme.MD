# Internal Fussball ratings at Transavia
## Ratings
1. Bart Offense: 1879.8 
2. Koen Offense: 1818.5 
3. Bart Average: 1790.6 
4. Carl Offense: 1765.9 
5. Brian Defense: 1755.1 
6. Brian Average: 1751.2 
7. Brian Offense: 1747.3 
8. Loek Defense: 1725.9 
9. Liveris Offense: 1701.6 
10. Bart Defense: 1701.5 
11. Liveris Average: 1696.7 
12. Liveris Defense: 1691.8 
13. Yashin Offense: 1691.8 
14. Yashin Average: 1690.7 
15. Yashin Defense: 1689.6 
16. Job V Defense: 1686.7 
17. Carl Average: 1681.6 
18. Koen Average: 1666.4 
19. Bas Defense: 1653.1 
20. Loek Average: 1652.8 
21. Job Defense: 1646.2 
22. Job Average: 1635.1 
23. Wouter Offense: 1630.2 
24. Tim Offense: 1625.1 
25. Job Offense: 1623.9 
26. Job V Offense: 1611.5 
27. Timo Offense: 1603.4 
28. Martin Offense: 1602.1 
29. Carl Defense: 1597.2 
30. Philip Offense: 1583.5 
31. Loek Offense: 1579.6 
32. Oliver Offense: 1574.2 
33. Tim Average: 1571.6 
34. Bas Average: 1564.4 
35. Philip  Defense: 1561.6 
36. Wouter Average: 1551.6 
37. Oliver Average: 1550.9 
38. Philip Average: 1540.0 
39. Floris Offense: 1531.9 
40. Martin Average: 1528.5 
41. Oliver Defense: 1527.6 
42. Mohammed Defense: 1526.9 
43. Jane Defense: 1525.0 
44. Timo Average: 1522.1 
45. Tim Defense: 1518.0 
46. Koen Defense: 1514.4 
47. Luka Defense: 1513.7 
48. Mohammed Average: 1503.8 
49. Frenk  Defense: 1503.3 
50. Donnie Defense: 1501.8 
51. Donnie Average: 1498.3 
52. Job  Defense: 1496.7 
53. Philip Defense: 1496.4 
54. Donnie Offense: 1494.8 
55. Floris Average: 1494.2 
56. Katherine Defense: 1493.5 
57. Thomas Defense: 1492.5 
58. Daan Offense: 1492.2 
59. Kassandra Offense: 1484.9 
60. Maarten Defense: 1484.3 
61. Thomas Average: 1482.3 
62. Irene Offense: 1481.4 
63. Mohammed Offense: 1480.8 
64. Bas Offense: 1475.6 
65. Wouter Defense: 1472.9 
66. Thomas Offense: 1472.1 
67. Lars Defense: 1470.1 
68. Bruno Defense: 1468.1 
69. Jelle Offense: 1468.0 
70. Kassandra Average: 1464.4 
71. Bruno Average: 1462.3 
72. Irene Average: 1460.2 
73. Boele Defense: 1458.1 
74. Arjen Offense: 1457.3 
75. Floris Defense: 1456.5 
76. Bruno Offense: 1456.5 
77. Martin Defense: 1454.9 
78. Adrian Defense: 1452.8 
79. Dennis Defense: 1451.4 
80. Timo2 Offense: 1449.7 
81. Ivar Offense: 1447.2 
82. Daan Ri Defense: 1445.4 
83. Vincent Offense: 1445.2 
84. Kassandra Defense: 1444.0 
85. Timo Defense: 1440.8 
86. Irene Defense: 1439.1 
87. Jay Offense: 1439.1 
88. Frenk Defense: 1434.7 
89. Katherine Average: 1434.2 
90. Roy Defense: 1430.9 
91. Boele Average: 1428.9 
92. Rob Offense: 1424.9 
93. Ivar Average: 1418.2 
94. Rob Average: 1418.1 
95. Frenk Average: 1416.8 
96. Daan Ri Offense: 1413.7 
97. Rob Defense: 1411.2 
98. Kristin Offense: 1403.2 
99. Brenda Defense: 1402.5 
100. Maarten Average: 1402.2 
101. Boele Offense: 1399.7 
102. Frenk Offense: 1399.0 
103. Michiel Defense: 1397.7 
104. Dennis Average: 1395.3 
105. Ivar Defense: 1389.2 
106. Kristin Average: 1382.8 
107. Anna Offense: 1380.4 
108. Katherine Offense: 1375.0 
109. Timo2 Average: 1365.2 
110. Andreea Offense: 1365.0 
111. Kristin Defense: 1362.4 
112. Laura Defense: 1357.9 
113. Laura Average: 1357.2 
114. Laura Offense: 1356.4 
115. Dennis Offense: 1339.2 
116. Roy Average: 1336.6 
117. Michiel Average: 1331.8 
118. Anna Average: 1328.2 
119. Maarten Offense: 1320.2 
120. Brenda Average: 1301.2 
121. Timo2 Defense: 1280.6 
122. Anna Defense: 1276.0 
123. Michiel Offense: 1266.0 
124. Roy Offense: 1242.2 
125. Brenda Offense: 1200.0 

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