# Internal Fussball ratings at Transavia
## Ratings
1. Koen Offense: 1818.5 
2. Bart Defense: 1738.8 
3. Liveris Offense: 1711.2 
4. Liveris Average: 1708.5 
5. Liveris Defense: 1705.8 
6. Koen Average: 1666.4 
7. Yashin Offense: 1659.4 
8. Loek Defense: 1652.8 
9. Yashin Average: 1643.5 
10. Job V Defense: 1639.2 
11. Yashin Defense: 1627.6 
12. Job V Offense: 1612.2 
13. Bart Average: 1585.0 
14. Oliver Offense: 1580.8 
15. Bas Offense: 1577.9 
16. Carl Offense: 1566.4 
17. Martin Offense: 1564.4 
18. Bas Average: 1562.2 
19. Martin Average: 1556.6 
20. Oliver Average: 1554.2 
21. Loek Average: 1554.2 
22. Carl Average: 1552.9 
23. Martin Defense: 1548.8 
24. Bas Defense: 1546.5 
25. Job Offense: 1541.4 
26. Philip Offense: 1541.0 
27. Carl Defense: 1539.4 
28. Floris Offense: 1531.9 
29. Oliver Defense: 1527.6 
30. Mohammed Defense: 1526.9 
31. Jane Defense: 1525.0 
32. Job Average: 1524.1 
33. Philip Average: 1522.4 
34. Maarten Defense: 1521.4 
35. Koen Defense: 1514.4 
36. Vincent Offense: 1511.8 
37. Job Defense: 1506.7 
38. Brian Offense: 1505.1 
39. Philip Defense: 1503.8 
40. Mohammed Average: 1503.8 
41. Frenk  Defense: 1503.3 
42. Job  Defense: 1496.7 
43. Floris Average: 1494.2 
44. Katherine Offense: 1483.6 
45. Irene Offense: 1481.4 
46. Mohammed Offense: 1480.8 
47. Timo Offense: 1480.6 
48. Thomas Offense: 1476.3 
49. Frenk Offense: 1474.7 
50. Thomas Average: 1473.9 
51. Thomas Defense: 1471.5 
52. Frenk Average: 1469.6 
53. Maarten Average: 1468.5 
54. Bruno Defense: 1468.1 
55. Jelle Offense: 1468.0 
56. Frenk Defense: 1464.4 
57. Bruno Average: 1462.3 
58. Irene Average: 1460.2 
59. Floris Defense: 1456.5 
60. Bruno Offense: 1456.5 
61. Loek Offense: 1455.6 
62. Timo Average: 1446.8 
63. Daan Ri Defense: 1445.4 
64. Irene Defense: 1439.1 
65. Jay Offense: 1439.1 
66. Katherine Average: 1436.4 
67. Daan Ri Offense: 1434.7 
68. Bart Offense: 1431.3 
69. Dennis Offense: 1417.8 
70. Maarten Offense: 1415.6 
71. Kassandra Defense: 1414.4 
72. Wouter Offense: 1413.6 
73. Timo Defense: 1412.9 
74. Kassandra Average: 1397.0 
75. Dennis Average: 1394.3 
76. Katherine Defense: 1389.1 
77. Kassandra Offense: 1379.5 
78. Dennis Defense: 1370.8 
79. Wouter Average: 1369.8 
80. Donnie Defense: 1367.6 
81. Michiel Defense: 1349.4 
82. Donnie Average: 1334.2 
83. Wouter Defense: 1326.1 
84. Michiel Average: 1318.8 
85. Donnie Offense: 1300.7 
86. Michiel Offense: 1288.2 

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