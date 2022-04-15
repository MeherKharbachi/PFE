#!/usr/bin/env python
# coding: utf-8

# # Natural language processing Task

# To fill the gap between human communication and machine understanding, NLP (Natural Language Processing) contains a range of sciences, including computer science and computational linguistics. It is significant because it aids in the resolution of linguistic ambiguity and provides quantitative structure to data for a variety of real - world applications such as speech recognition and text analytics.
# <br>After completing our first task, which was to extract previews from the Guardian website, we began our second task, which was to reproduce the results of the <cite id="cfvjb"><a href="#zotero|11983139/J4T53NKQ">(Beal et al., 2021)</a></cite> article by processing and analyzing the texts that we had extracted.
# The article's authors proceeded as follows:
# 
# - <b> Information extraction</b>: they extracted the main features of each sentence in the article's text.
# 
# - <b>Allocation of Text Context</b>: each sentence is assigned to a team.
# 
# - <b>Text Vectorisation</b>: they converted the sentences into vectors using a Count Vectorizer technique to have a numerical representation of the words in a sentence.
# 
# - <b>Prediction</b>: Once the feature set for each game is formed, they trained a Random Forest model using historic 

# ## Information extraction

# Information Extraction (IE) is the process of extracting meaningful information from unstructured text data and presenting it in a structured format.
# <br>We can use information extraction to retrieve pre-defined information, such as a person's name, the location of an organisation, or the identification of a relationship between entities, and save it in a structured format, such as a database. This technique is called the Named Entity Recognition.

# ### Named Entity Recognition (NER)

# The task of identifying and categorizing key information in text is known as Named Entity Recognition (NER). It is also known as entity extraction or identification. Each detected entity is assigned to a predefined category.
# An NER model, for example, may detect the word "Mark" in a text and classify it as a "Person."

# <br>However, before the IE step, Data Preprocessing is required for any Machine Learning model. The model's performance is heavily influenced by how well the raw data has been cleaned and preprocessed. Similarly, in the case of NLP, the first step is text processing.
# <br>The various preprocessing steps are as follows:
# 
# * Lower Casing 
# * Tokenization
# * Punctuation Mark Removal
# * Stop Word Removal
# * Lemmatization

# ### Lower Casing

# When we get text input, such as a paragraph, we find both lower and upper case words.On the other hand, The computer considers the identical words typed in various cases to be separate entities.For example, The computer, considers 'football' and 'FOOTBALL' to be two distinct terms, despite the fact that they both imply the same thing.We must change all of the words to lower case in order to solve this problem. The text will be more consistent as a result of this. 

# ### Tokenization

# Tokenization is the next text preparation step. Tokenization is the act of dividing a paragraph into smaller parts like sentences or words. Each unit is then treated as a separate token. Tokenization's primary premise is to attempt to grasp the meaning of the text by studying the smaller components or tokens that comprise the paragraph.

# ### Punctuation Marks Removal

# Depending on the scenario, we may need to delete or keep punctuation from the text.

# ### Stop Words Removal

# Stop words are words that appear often in any language but do not contribute much sense to sentences. These are frequent terms that are part of any language's grammar. Stop words are unique to each language.For example, Stop words in English include "the," "he," "he," "his," "her," "herself," and so on. By removing stop words, we may successfully lower the dimensionality of our text collection without sacrificing any important information.

# ### Lemmatization

# Because there are many words in a text that have the same root and meaning, it is evident to normalise the text by applying the lemmatization technique, which helps to reduce a given term to its root word.

# ## Allocation of text context

# This section consists of assigning each sentence to the appropriate team. In a preview, for example, the journalist may discuss squad A or team B. As a result, we will have three columns: one for sentences about team A, another for sentences about team B, and a third for sentences about both teams at the same time.

# ## Text vectorisation

# When the text processing and allocation phases are completed, it is time to begin the modeling phase.
# <br>However, our model will not be able to understand these raw texts, so we must convert them into vectors, which are digital representations of these character strings.Here, the goal is to extract textual features so that the model can learn.
# <br>Among the vectorization techniques, we highlight the bag of words: it is a very simple technique that calculates the vectors of a text based on the frequency of vocabulary words.
# It is simple to interpret and only refers to the frequency of vocabulary words in a given document.
# <br>As a result, articles, prepositions, and conjunctions that do not contribute much to meaning are just as important as adjectives or verbs.
# <br>An example for the count vectorization technique:

# ![title](images/countvector.png)

# <br>In addition, there are other techniques that, in general, work better in machine learning models to address this issue such as TF-IDF: term frequency-inverse document frequency.
# <br>The idea behind the TF-IDF approach is that words that appear less frequently in all documents but more frequently in individual documents contribute more to classification.
# these terms can be calculated as follows:

# ![title](images/tfidf.png)

# ## Prediction

# There are various methods in machine learning for dealing with classification or regression problems that are highly fascinating to try.
# <br>In this work, we will use a random forest classifier that takes vectorized texts as input to predict the outcomes of football matches(Home win, Away win, Draw).

# ## Proof of concept

# ### Information Extraction

# #### Named Entity Recognition (NER)

# In our case, identifying the names of the teams in the previews is a critical task that will allow us to extract the main features in our text.
# <br>This operation is not possible with the standard spacy NER because of errors in entity detection; spacy can consider a team name to be a person and vice versa.
# <br>To address this issue, we decided to build a model that will allow us to detect our own entities.

# ##### Example

# ![title](images/ner.png)

# ![title](images/ner2.png)

# ##### Train a model to detect custom entities

# ![title](images/ner3.png)
# ![title](images/ner4.png)

# We test again:

# ![title](images/ner5.png)

# #### Entity ruler 

# Using token-based rules or exact phrase matches, the entity ruler allows us to add spans to the Doc entities. It can be used in conjunction with the statistical EntityRecognizer to improve accuracy, or it can be used on its own to implement a rule-based entity recognition system.
# <br>We took advantage of the dataset that we have which contains the teams and their different names.
# In this sense we have linked each name or nickname of a team to its main entity

# ![title](images/ner6.png)

# For example the nickname Spurs is now detectable in the text that is linked to the Tottenham Hotspur entity

# ![title](images/ner7.png)

# #### Get the names of the coaches

# We also noticed that in most of the previews, we find the names of the managers but not the names of the teams,
# so to ensure the extraction of information, we used a database that we have that contains a history of managers for each team.<br>As a result, it is now easier to identify the section of the text that refers to one of the two teams.

# Example of the dataset:

# ![title](images/coach1.png)

# The final output: for each preview, we have the coaches of each team.
# 

# ![title](images/coach2.png)

# #### Previews Preprocessing

# First of all, beginning with the tokenization step, which is the task of chopping up texts into pieces in order to remove stop words such as (the,a,an,so,what..). We also removed all punctuation because it isn't important in the text, and then we used a lemmatization technique that allows for lexical processing, such as (runs, running,ran) returns run.

# ##### Example

# ![title](images/text1.png)

# ![title](images/token.png)

# We continue our normalization and move on to the next step, which is detecting the names of the two teams, the names of the coaches, and changing their names by hometeam, awayteam, homecoach, and awaycoach.The reason for this is so that our model's predictions can generalize.
# <br>We noticed that the words 'hosts,' 'home side,' and 'visitors,' which refer to the home team and away team, are frequently used in the previews, and they have been changed.

# We take the same example:

# ![title](images/text2.png)

# Preview after cleanning:

# ![title](images/preview.png)

# Preview after normalization:

# ![title](images/preview2.png)

# ### Text allocation

# After having cleaned and normalized the texts, obtaining the target values of each preview, we move on to the next step which consists of decomposing the texts of each preview and allocating each sentence to the corresponding team.
# for some previews, there are sentences that talk about the two teams, that's why we created 3 new columns for our dataset:
# - homeTeamText: this is the text that talks about home team
# - awayTeamText: this is the text that talks about away team
# - bothteamText: this is the text that speaks of the two teams
# 
# <br> Here we have worked with the pre-built entities to detect teams names in the text, but as we said , this is not always reliable that's why we have employed the teams and the coaches dataset which contains their different names to search it in each sentence.
# <br> If the home team name or the home coach name are included in the sentence , so it's very likely that it's related to the home team and it's the same scenario for away team.
# <br> We also noticed that the words ‘hosts’,‘home side’,'home crowd','these sides','these teams','both teams','two sides' and ‘visitors’ which refer to the home team and away team, are frequently used in the previews, so we changed these terms by 'bothteam' to detect sentences.

# ![title](images/vecttext.png)

# ### Text vectorisation

# It should be emphasized that for this work, we will utilize the count vectorizer approach to vectorize the preview texts.
# <br>This function comprises certain hyperparameters that must be fixed and find the best combinations in order to increase the quality of the vectors.
# <br>Among these hyperparameters, we can find:
# - stop_words: CountVectorizer provides a predefined set of stop words; in our case, we can specify 'english.' 
# - ngram_range: the number of word combinations to consider, for example (1,1) takes only tokens, whereas (1,2) specifies that we want to consider both unigrams (single words) and bigrams (combination of 2 words)
# - min_df:stands for minimum document frequency; it disregards words with a document frequency that is strictly lower than the specified threshold.

# ### Prediction

# #### Get target values

# To enable our model to train and make predictions, we must first provide the target values (the outputs of the matches).
# <br>We have set two target values:
# 
# - The outcome of a match: home win, away win, draw
#     
# - The goal difference: the difference in goals scored

# ![title](images/final_data.png)

# #### The proportions of the results

# It is worth noting that the class distribution of English Premier League games that we have from 2009 to 2022 is 45% home wins, draws 25% and away wins 30%.

# ![title](images/stats.png)

# #### Split data into train and test dataset

# Before setting up a machine learning model, we must divide our data into train and test data. the train dataset is used to train the machine learning model and the test dataset is to assess the fit, which is data that the model has never seen before. To accomplish this, we will take data from 2009 to 2018 for the train data and the rest from the 2019 until now for the test dataset. The reason of not applying a shuffle is to avoid distorting the temporal order of the matches.

# #### Random Forest Classifier

# A random forest's fundamental notion is to aggregate a large number of individual decision trees into a single model that function as an ensemble. All individual tree projections are pooled, and the class with the highest votes becomes our model's prediction.
# We have to note that each tree uses slightly different subsets of data, which means they may not contain the same columns and rows
# <br>In addition, we can experiment with several hyperparameters in the Random forest classifier to increase model performance, such as:
# - n_estimators: the number of trees that the classifier will consider.
# - max_depth: the longest path from the root node to the leaf node.
# - min_sample_split: the minimal amount of observations required to split any given node.
# - Criterion: a function that determines how good a split is. we can experiment with (gini,entropy) values.

# ## Reference

# <!-- BIBLIOGRAPHY START -->
# <div class="csl-bib-body">
#   <div class="csl-entry"><i id="zotero|11983139/J4T53NKQ"></i>Beal, R., Middleton, S. E., Norman, T. J., &#38; Ramchurn, S. D. (2021). Combining Machine Learning and Human Experts to Predict Match Outcomes in Football: A Baseline Model. <i>Proceedings of the AAAI Conference on Artificial Intelligence, 35(17), 15447-15451</i>.  https://ojs.aaai.org/index.php/AAAI/article/view/17815</div>
# </div>
# <!-- BIBLIOGRAPHY END -->
