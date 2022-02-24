#!/usr/bin/env python
# coding: utf-8

# # Literature review
# 
# Data analytics has been adopted by most industries, including football. However, the availability of football match data has increased in recent years, allowing anyone involved in football to gain hidden knowledge and predict outcomes.
# 
# In our literature review, we will concentrate on models that predict the outcomes of football matches based on various baselines. These baselines are statistical and machine learning approaches that rely on statistical machine learning based on historical data about individual teams.
# 

# ## Statistical methods

# <br>The very first generation of football-related models focused on the distribution of the number of goals scored during a football game.
# <br>Starting by <b>(Maher 1982)</b> included a general model that uses an independent poisson distribution to approximate a team's scoring frequency. However, this model assumes that each team's home, away, attack, and defense parameters are constant.
# <br> <b>Mark Dixon and Stuart Coles</b> claimed in their 1997 paper that <b>Maher's</b> model has certain limitations, such as low score results (0-0, 1-0, 0-1, and 1-1) being inherently unreported and each team's scoring and defending abilities being regarded as constant over time.
# <br>They proposed a new model with some specific enhancements. This model is a bivariate poisson distribution with parameters based on past performance for the number of goals scored by each team. This implies that recent matches have a greater impact on strength estimates.
# <br>In addition, <b>(Baboota and Kaur 2018)</b> investigates the application of machine learning techniques to football match outcomes and compares the results to bookmakers. They employ feature engineering and exploratory data analysis to identify the feature set that contains the most important factors for predicting match outcome. The authors put Gaussian naive Bayes, SVM, Random forest, and Gradient boosting to the test. They used training data from 2005 to 2014 in the EPL(English Premier League) and discovered that the Gradient boosting method performed the best with an accuracy of 56.7 %

# ## Bookmakers predictions

# Making bets on the outcome of football matches has a long history around the world, and typically entails selecting matches that are thought to be the most likely to end in a draw.
# Bookmakers provide odds on a match's various outcomes and the simplest version of this relies exclusively on the results which can be a win by either the team playing at home or the team playing away, or a draw. More complex bets on the score or the half-time and full-time results are also available.
# <br>Football match predictions is a very complex problem in which the outcome of the game is predicted based on the teams' previous performance and the relative abilities of the players in the teams. This implies that the team with the best players should win.
# <br>Bookmakers set their odds based on this challenge and employ sophisticated pricing models that assign "odds" to different outcomes in order to maximize their chances of profit.
# <br>According to <b>(Beal, Norman, and Ramchurn 2019)</b>, bookmakers' accuracy was around 67% for American football, 74% for basketball, 64% for cricket, 61% for baseball, and only 54% for football during the 2017/2018 season. This is due to the fact that the frequency of goals is far lower than the frequency of points scored in the other sports.

# ## Sentiment analysis predictions

# Among the methods interested in football match predictions, we highlight sentimental analysis of social media platforms. These studies underscore the importance of hidden information contained in the sentiment of publications. However, these approaches focus on opinion aggregation rather than attempting to extract potential indicators for teams from human experts previews
# <br> True, fans tweets are unlikely to influence game outcomes, unless they are used to exceptionally motivate or demotivate a team. Fans use Twitter to express their personal feelings, primarily about the team they are following and their next opponent's strengths, weaknesses, and prospects, and this can sometimes help establish betting odds.
# <br>This method is used by <b>(Schumaker, Jarmoszko, and Labedz 2016)</b> to predict English Premier League matches by analyzing fans tweets during the final three months of the 2013–2014 from February 16 through May 11 2014. It achieved an accuracy of 50%,this system has only two possible outcomes: home team win or away team win. If the model's number of Home or Away tweets was zero, the match was not considered for that model. However, it was discovered that sentiment was unable to recognize a draw outcome, so this category was dropped.
# <br>And <b>(Sinha et al. 2013)</b> demonstrate the use of similar analysis for american football results,during the 2010–2012 seasons, with an accuracy of 56%.

# ## Predictions based on human inputs

# To date, probabilistic methods have yielded limited results and appear to have reached a plateau in terms of accuracy because team performance is dependent not only on team abilities but also on a variety of dynamic factors such as team configurations, player health, match location, weather, team strategies, and other external factors.
# As a result predicting football match outcomes becomes a very complex computational problem.
# <br>To address these weaknesses, a new technique has emerged <b>(Beal,Middleton,Norman and Ramchurn 2020)</b> that incorporates human expertise and judgment, such as media information, rather than just basic performance statistics, which has helped improve prediction accuracy.

# These new baselines used a dataset of 6 seasons of English Premier League games from 2013/14 to 2018/19, including football match data, Guardian previews and predictions from bookmakers odds for 1770 games, employing both statistical machine learning techniques and <b>Natural Language Processing</b>.
# <br>When <b>NLP</b> methods, <b>statistical approaches</b>, and <b>bookmakers predictions</b> were compared to the ensemble learning approach which combines the first three techniques, the results revealed that these methods could be improved. It achieved an accuracy of 63.2 %, a 10.8 % increase over <b>the bookmakers'</b> accuracy(52.43%), 4.1 % more than <b>(Dixon and Coles 1997) (59.11%)</b> and a 13 % improvement over the sentiment analysis approach in <b>(Schumaker, Jarmoszko, and Labedz Jr 2016)</b>.
# <br>Experiments revealed that using the ensemble model increases the likelihood of predicting draws and longshot results. This is especially true when the text vectors model identifies more longshots (38.9 %) by taking into account human input, whereas the first three models are typically poor at predicting these events.
# <br> In addition, the final predictions are based on a Random forest classifier.

#  

# ## Our contribution

# In most machine learning situations, we are only concerned with one problem at a time. Whatever the task, the problem is typically outlined as using data to solve or optimize a single metric at a time. However, this approach will eventually reach a performance limit, which is often due to the size of the dataset or the model's ability to derive meaningful representations from it.
# <br>On the other hand, multitasking learning is a machine learning approach in which we attempt to learn multiple tasks at the same time while optimizing multiple loss functions.Instead of training separate models for each task, we expect a single model to learn how to perform all tasks simultaneously.<br> The model uses all of the data available in the various tasks to learn generalized representations of the data that are useful in multiple contexts during this process.
# <br>Our contribution to this project is to extend the methodology described in <b>(Beal,Middleton,Norman, and Ramchurn 2020)</b> which consists of developing a model that ensembles three separate models trained separately and to build a multi-head, multi-task deep learning network <b>(Vafaeikia, Namdar, and Khalvati 2020)</b> capable of capturing the game environment as well as more standard time series tabular data. This dataset includes 3880 English Premier League match previews from 2009 to the present.
# <br>The findings will be compared to traditional and machine learning approaches described in the literature, and the following question will be addressed: <br>Do football experts' human analysis influence the predictions of football matches?
