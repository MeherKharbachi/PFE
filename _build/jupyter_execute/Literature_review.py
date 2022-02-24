#!/usr/bin/env python
# coding: utf-8

# # Literature review
# 
# Data analytics has been adopted by most industries, including football. However, the availability of football match data has increased in recent years, allowing anyone involved in football to gain hidden knowledge and predict outcomes.
# 
# In our literature review, we will concentrate on models that predict the outcomes of football matches based on various baselines. These baselines are statistical and machine learning approaches that rely on statistical machine learning based on historical data about individual teams.
# 

# ## Statistical approaches

# <br>The very first generation of football-related models focused on the distribution of the number of goals scored during a football game.
# <br>Starting by <cite id="3v4le"><a href="#zotero|11983139/Y23ZDDQG">(Maher, 1982)</a></cite> included a general model that uses an independent poisson distribution to approximate a team's scoring frequency. However, this model assumes that each team's home, away, attack, and defense parameters are constant.
# <br> <cite id="0tzsj"><a href="#zotero|11983139/C7ER7JJY">(Dixon &#38; Coles, 1997)</a></cite> claimed in their paper that the previous model has certain limitations, such as low score results (0-0, 1-0, 0-1, and 1-1) being inherently unreported and each team's scoring and defending abilities being regarded as constant over time.
# <br>They proposed a new model with some specific enhancements. This model is a <b>bivariate poisson distribution</b> with parameters based on past performance for the number of goals scored by each team. This implies that recent matches have a greater impact on strength estimates.
# <br>Unlike previous models that used a <b>Poisson distribution</b>, <cite id="57q3t"><a href="#zotero|11983139/RPMV87I5">(Boshnakov et al., 2017)</a></cite> proposed a new approach that uses an independent and identically distributed <b>Weibull distribution</b> for the number of goals scored by the home and away teams in a match. Furthermore, they allowed for dependence between the goals scored by the two teams by using a copula to generate a bivariate distribution with positive or negative dependence.
# They compared this <b>bivariate Weibull</b> model to the others and discovered that it provides a good fit to <b>English Premier League</b> data from 2006/2007 to 2015/2016 seasons and achieves positive betting returns.

# ## Bookmakers predictions

# Making bets on the outcome of football matches has a long history around the world, and typically entails selecting matches that are thought to be the most likely to end in a draw.
# Bookmakers provide odds on a match's various outcomes and the simplest version of this relies exclusively on the results which can be a win by either the team playing at home or the team playing away, or a draw. More complex bets on the score or the half-time and full-time results are also available.
# <br>Football match predictions is a very complex problem in which the outcome of the game is predicted based on the teams' previous performance and the relative abilities of the players in the teams. This implies that the team with the best players should win.
# <br>Bookmakers set their odds based on this challenge and employ sophisticated pricing models that assign "odds" to different outcomes in order to maximize their chances of profit.
# <br>According to <cite id="lkvq5"><a href="#zotero|11983139/KXPDVVLV">(Beal et al., 2019)</a></cite>, bookmakers' accuracy was around 67% for <b>American football</b>, 74% for <b>basketball</b>, 64% for <b>cricket</b>, 61% for <b>baseball</b>, and only 54% for <b>football</b> during the 2017/2018 season. This is due to the fact that the frequency of goals is far lower than the frequency of points scored in the other sports.

# ## Machine Learning approaches

# To date, <b>probabilistic methods</b> have yielded limited results and appear to have reached a plateau in terms of accuracy because team performance is dependent not only on team abilities but also on a variety of dynamic factors such as team configurations, player health, match location, weather, team strategies, and other external factors.
# As a result predicting football match outcomes becomes a very complex computational problem.
# <br>Among the <b>machine learning</b> methods interested in football match predictions, we highlight <b>sentimental analysis</b> of social media platforms. These studies focus on opinion aggregation and underscore the importance of hidden information contained in the sentiment of fans publications.
# <br> True, fans tweets are unlikely to influence game outcomes, unless they are used to exceptionally motivate or demotivate a team. For example, supporters use social media platforms like <b>Twitter</b> to express their personal feelings, primarily about the team they are following and their next opponent's strengths, weaknesses, and prospects, and this can sometimes help establish betting odds.
# <br>This method is used by <cite id="ua7k3"><a href="#zotero|11983139/YREYVCH5">(Schumaker et al., 2016)</a></cite> to predict <b>English Premier League</b> matches by analyzing fans tweets during the final three months of the 2013–2014 from February 16 through May 11 2014. It achieved an accuracy of 50%,this system has only two possible outcomes: home team win or away team win. If the model's number of Home or Away tweets was zero, the match was not considered for that model. However, it was discovered that sentiment was unable to recognize a draw outcome, so this category was dropped.
# <br>As well as that, <cite id="nqba9"><a href="#zotero|11983139/HV42R7G5">(Baboota &#38; Kaur, 2019)</a></cite> investigates the application of machine learning techniques to predict football match outcomes and compares the results to bookmakers. They employ feature engineering and exploratory data analysis to identify the feature set that contains the most important factors for predicting match outcome. The authors put <b>Gaussian naive Bayes</b>, <b>SVM</b>, <b>Random forest</b>, and <b>Gradient boosting</b> to the test. They used training data from 2005 to 2014 in the <b>EPL</b> (English Premier League) and discovered that the <b>Gradient boosting</b> method performed the best with an accuracy of 56.7 %

# Moreover, to address weaknesses described above, recently, a new technique has emerged <cite id="0qktm"><a href="#zotero|11983139/J4T53NKQ">(Beal et al., 2020)</a></cite> that incorporates human expertise and judgment, such as media information, rather than just basic performance statistics, which has helped improve prediction accuracy.
# <br>These new baselines used a dataset of 6 seasons of <b>English Premier League</b> games from 2013/14 to 2018/19, including football match data, the <b>Guardian</b> previews and predictions from bookmakers odds for 1770 games, employing both statistical machine learning techniques and <b>Natural Language Processing</b>.
# <br>When <b>NLP</b> methods, <b>statistical approaches</b>, and <b>bookmakers predictions</b> were compared to the ensemble learning approach which combines the first three techniques and uses a <b>Random forest classifier</b>, the results revealed that these methods could be improved.
# <br>It achieved an accuracy of 63.2 %, a 10.8 % increase over <b>the bookmakers'</b> accuracy(52.43%), 4.1 % more than <cite id="ysqbf"><a href="#zotero|11983139/C7ER7JJY">(Dixon &#38; Coles, 1997)</a></cite> (59.11%) and a 13 % improvement over </b>the sentiment analysis</b> approach in <cite id="onivn"><a href="#zotero|11983139/YREYVCH5">(Schumaker et al., 2016)</a></cite>.
# <br>Experiments revealed that using the ensemble model increases the likelihood of predicting draws and longshot results. This is especially true when the text vectors model identifies more longshots (38.9 %) by taking into account human input, whereas the first three models are typically poor at predicting these events.

# ## Our contribution

# In most <b>machine learning</b> situations, we are only concerned with one problem at a time. Whatever the task, the problem is typically outlined as using data to solve or optimize a single metric at a time. However, this approach will eventually reach a performance limit, which is often due to the size of the dataset or the model's ability to derive meaningful representations from it.
# <br>On the other hand, <b>multitasking learning</b> is a machine learning approach in which we attempt to learn multiple tasks at the same time while optimizing multiple loss functions.Instead of training separate models for each task, we expect a single model to learn how to perform all tasks simultaneously.<br> The model uses all of the data available in the various tasks to learn generalized representations of the data that are useful in multiple contexts during this process.
# <br>Our contribution to this project is to extend the methodology described in <cite id="od7fx"><a href="#zotero|11983139/J4T53NKQ">(Beal et al., 2020)</a></cite> which consists of developing a model that ensembles three separate models trained separately and to build a <b>multi-head</b>, <b>multi-task</b> deep learning network <cite id="s8i0w"><a href="#zotero|11983139/6ZJ7BSPZ">(Vafaeikia et al., 2020)</a></cite> capable of capturing the game environment as well as more standard time series tabular data. This dataset includes, until now, 3880 <b>English Premier League</b> match previews from 2009 to the present.
# <br>The findings will be compared to traditional and machine learning approaches described in the literature, and the following question will be addressed: <br><b>Do football experts' human analysis influence the predictions of football matches?</b>

# ## References

# <!-- BIBLIOGRAPHY START -->
# <div class="csl-bib-body">
#   <div class="csl-entry"><i id="zotero|11983139/HV42R7G5"></i>Baboota, R., &#38; Kaur, H. (2019). Predictive analysis and modelling football results using machine learning approach for English Premier League. <i>International Journal of Forecasting</i>, <i>35</i>(2), 741–755. https://doi.org/10.1016/j.ijforecast.2018.01.003</div>
#   <div class="csl-entry"><i id="zotero|11983139/J4T53NKQ"></i>Beal, R., Middleton, S. E., Norman, T. J., &#38; Ramchurn, S. D. (2020). Combining Machine Learning and Human Experts to Predict Match Outcomes in Football: A Baseline Model. <i>arXiv:2012.04380 [Cs]</i>. http://arxiv.org/abs/2012.04380</div>
#   <div class="csl-entry"><i id="zotero|11983139/KXPDVVLV"></i>Beal, R., Norman, T. J., &#38; Ramchurn, S. D. (2019). Artificial intelligence for team sports: a survey. <i>The Knowledge Engineering Review</i>, <i>34</i>. https://doi.org/10.1017/S0269888919000225</div>
#   <div class="csl-entry"><i id="zotero|11983139/RPMV87I5"></i>Boshnakov, G., Kharrat, T., &#38; McHale, I. G. (2017). A bivariate Weibull count model for forecasting association football scores. <i>International Journal of Forecasting</i>, <i>33</i>(2), 458–466. https://doi.org/10.1016/j.ijforecast.2016.11.006</div>
#   <div class="csl-entry"><i id="zotero|11983139/C7ER7JJY"></i>Dixon, M. J., &#38; Coles, S. G. (1997). Modelling Association Football Scores and Inefficiencies in the Football Betting Market. <i>Journal of the Royal Statistical Society: Series C (Applied Statistics)</i>, <i>46</i>(2), 265–280. https://doi.org/10.1111/1467-9876.00065</div>
#   <div class="csl-entry"><i id="zotero|11983139/Y23ZDDQG"></i>Maher, M. J. (1982). Modelling association football scores. <i>Statistica Neerlandica</i>, <i>36</i>(3), 109–118. https://doi.org/10.1111/j.1467-9574.1982.tb00782.x</div>
#   <div class="csl-entry"><i id="zotero|11983139/YREYVCH5"></i>Schumaker, R. P., Jarmoszko, A. T., &#38; Labedz, C. S. (2016). Predicting wins and spread in the Premier League using a sentiment analysis of twitter. <i>Decision Support Systems</i>, <i>88</i>, 76–84. https://doi.org/10.1016/j.dss.2016.05.010</div>
#   <div class="csl-entry"><i id="zotero|11983139/6ZJ7BSPZ"></i>Vafaeikia, P., Namdar, K., &#38; Khalvati, F. (2020). A Brief Review of Deep Multi-task Learning and Auxiliary Task Learning. <i>arXiv:2007.01126 [Cs, Stat]</i>. http://arxiv.org/abs/2007.01126</div>
# </div>
# <!-- BIBLIOGRAPHY END -->
