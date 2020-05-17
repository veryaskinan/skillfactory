#!/usr/bin/env python
# coding: utf-8

# In[33]:


from __future__ import division
import numpy as np
import pandas as pd
from collections import Counter
import math
import itertools


# In[4]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[5]:


data.describe()


# # Предобработка

# In[39]:


answers = {} # создадим словарь для ответов

# profit
data['profit'] = data.revenue - data.budget


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[11]:


# в словарь вставляем номер вопроса и ваш ответ на него
# запишите свой вариант ответа
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650)' # +
# если ответили верно, можете добавить комментарий со значком "+"


# In[8]:


# тут пишем ваш код для решения данного вопроса:
def q1(data):
    slice = data[['imdb_id', 'original_title', 'budget']]

    # technique 1
    res_1 = slice.sort_values(by=['budget'], ascending=False).iloc[0]

    # technique 2
    res_2 = slice[slice.budget == slice.budget.max()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')
        
        
# q1(data)


# ВАРИАНТ 2

# In[ ]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[ ]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals (tt0279111)'  # +


# In[13]:


def q2(data):
    slice = data[['imdb_id', 'original_title', 'runtime']]

    # technique 1
    res_1 = slice.sort_values(by=['runtime'], ascending=False).iloc[0]

    # technique 2
    res_2 = slice[slice.runtime == slice.runtime.max()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q2(data)


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[31]:


answers['3'] = 'Winnie the Pooh (tt1449283)'  # +


# In[14]:


def q3(data):
    slice = data[['imdb_id', 'original_title', 'runtime']]

    # technique 1
    res_1 = slice.sort_values(by=['runtime']).iloc[0]

    # technique 2
    res_2 = slice[slice.runtime == slice.runtime.min()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q3(data)


# # 4. Какова средняя длительность фильмов?
# 

# In[30]:


answers['4'] = 110 # +


# In[29]:


def q4(data):
    slice = data[['runtime']]

    # technique 1
    res_1 = slice.runtime.mean()

    # technique 2
    res_2 = slice.runtime.sum() / data.runtime.count()

    # compare results
    compare = res_1 == res_2
    if compare:
        print(res_1)
    else:
        print('Results are not the same')


# q4(data)


# # 5. Каково медианное значение длительности фильмов? 

# In[38]:


answers['5'] = 107 # +


# In[37]:


def q5(data):
    slice = data[['runtime']]

    # technique 1
    res_1 = slice.runtime.median()

    # technique 2
    sorted = slice.sort_values(by='runtime')
    half_len = (sorted.runtime.count() + 1) / 2
    if half_len % 1 == 0:
        res_2 = sorted.iloc[int(math.floor(half_len - 1))].runtime
    else:
        left = sorted.iloc[int(math.floor(half_len - 1))].runtime
        right = sorted.iloc[int(math.ceil(half_len - 1))].runtime
        res_2 = (left + right) / 2

    # compare results
    compare = res_1 == res_2
    if compare:
        print(res_1)
    else:
        print('Results are not the same')


# q5(data)


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[ ]:


answers['6'] = 'Avatar (tt0499549)' # +


# In[40]:


def q6(data):
    slice = data.loc[:, ['imdb_id', 'original_title', 'profit']]

    # technique 1
    res_1 = slice.sort_values(by=['profit'], ascending=False).iloc[0]

    # technique 2
    res_2 = slice[slice.profit == slice.profit.max()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q6(data)


# # 7. Какой фильм самый убыточный? 

# In[ ]:


answers['7'] = 'The Lone Ranger (tt1210819)' # +


# In[56]:


def q7(data):
    slice = data.loc[:, ['imdb_id', 'original_title', 'profit']]

    # technique 1
    res_1 = slice.sort_values(by=['profit']).iloc[0]

    # technique 2
    res_2 = slice[slice.profit == slice.profit.min()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q7(data)


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[46]:


answers['8'] = 1478 # +


# In[55]:


def q8(data):
    slice = data.loc[:, ['budget', 'revenue', 'profit']]

    # technique 1
    res_1 = slice[slice.profit > 0].profit.count()

    # technique 2
    res_2 = slice[slice.revenue > slice.budget].revenue.count()

    # compare results
    compare = res_1 == res_2
    if compare:
        print(res_1)
    else:
        print('Results are not the same')


# q8(data)


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[ ]:


answers['9'] = 'The Dark Knight (tt0468569)' # +


# In[48]:


def q9(data):
    slice = data[data.release_year == 2008].loc[:, ['imdb_id', 'original_title', 'revenue']]

    # technique 1
    res_1 = slice.sort_values(by=['revenue'], ascending=False).iloc[0]

    # technique 2
    res_2 = slice[slice.revenue == slice.revenue.max()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q9(data)


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[51]:


answers['10'] = 'The Lone Ranger (tt1210819)' # +


# In[53]:


def q10(data):
    filtered = data[(data.release_year >= 2012) & (data.release_year <= 2014)]
    slice = filtered.loc[:, ['imdb_id', 'original_title', 'profit']]

    # technique 1
    res_1 = slice.sort_values(by=['profit']).iloc[0]

    # technique 2
    res_2 = slice[slice.profit == slice.profit.min()].iloc[0]

    # compare results
    compare = res_1 == res_2
    if compare.value_counts()[True] == len(slice.columns):
        print(res_1.original_title + ' (' + res_1.imdb_id + ')')
    else:
        print('Results are not the same')


# q10(data)


# # 11. Какого жанра фильмов больше всего?

# In[ ]:


answers['11'] = 'Drama' # +


# In[52]:


def q11(data):
    # technique 1
    genres_count = {}
    max = {
        'genre': 'unknown',
        'count': 0
    }
    value_counts = data.genres.value_counts()
    for genresString in value_counts.keys():
        genres = genresString.split('|')
        count = value_counts.loc[[genresString]]
        for genre in genres:
            if genre not in genres_count:
                genres_count[genre] = 0
            genres_count[genre] += count[genresString]
            if genres_count[genre] > max['count']:
                max['genre'] = genre
                max['count'] = genres_count[genre]
    res_1 = max['genre']

    # technique 2
    genres_list = data.genres.str.split('|').tolist()
    value_counts = pd.DataFrame(genres_list).stack().value_counts()
    res_2 = value_counts[value_counts == value_counts.max()].index[0]

    # compare results
    compare = res_1 == res_2
    if compare:
        print(res_1)
    else:
        print('Different ways results are not the same')


# q11(data)


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[ ]:


answers['12'] = 'Drama' # +


# In[ ]:


def q12(data):
    slice = data[data.revenue > data.budget]
    genres_list = slice.genres.str.split('|').tolist()
    value_counts = pd.DataFrame(genres_list).stack().value_counts()
    res = value_counts[value_counts == value_counts.max()].index[0]
    print('12. ', end ='')
    print(res)


# q12(data)


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[ ]:


answers['13'] = 'Peter Jackson' # +


# In[59]:


def q13(data):
    slice = data.loc[:, ['director', 'profit']]
    res = slice.groupby(['director'])['profit'].sum().sort_values().index[-1]
    print(res)


# q13(data)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[60]:


answers['14'] = 'Robert Rodriguez' # +


# In[71]:


def q14(data):
    slice = data.loc[:, ['director']]         [data.genres.str.lower().str.contains('action')]
    directors_list = slice.director.str.split('|').tolist()
    res = pd.DataFrame(directors_list).stack().value_counts()
    print(res.index[0])


# q14(data)


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[82]:


answers['15'] = 'Chris Hemsworth' # +


# In[81]:


def q15(data):
    slice = data[data.release_year == 2012].loc[:, ['cast', 'revenue']]
    slice = pd.DataFrame(
        slice.cast.str.split('|').tolist(), index=slice.revenue
    ) \
        .stack() \
        .reset_index([0, 'revenue'])

    slice.columns = ['revenue', 'actor']

    slice = slice.groupby(['actor'])         .revenue.sum().reset_index()         .sort_values(by='revenue', ascending=False).reset_index()

    res = slice.loc[0].actor
    print(res)


# q15(data)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[ ]:


answers['16'] = 'Matt Damon' # +


# In[79]:


def q16(data):
    slice = data[data.budget > data.budget.mean()].loc[:,['budget', 'cast']]
    actors_budget = pd.DataFrame(slice.cast.str.split('|').tolist(), index=slice.budget).stack()
    actors_budget = actors_budget.reset_index([0, 'budget'])
    actors_budget.columns = ['budget', 'actor']
    actors = actors_budget['actor']

    value_counts = actors.value_counts().reset_index()
    value_counts.columns = ['actor', 'count']
    value_counts.sort_values(by='count')
    res = value_counts.loc[0].actor

    print(res)


# q16(data)


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[ ]:


answers['17'] = 'Action' # +


# In[80]:


def q17(data):
    nicalas_genres = data[data.cast.str.find('Nicolas Cage') >= 0]          .loc[:,['genres', 'cast']]

    splited_genres = pd.DataFrame(
        nicalas_genres.genres.str.split('|').tolist()
    ) \
        .stack().reset_index()

    splited_genres.columns = ['drop', 'drop', 'genre']
    splited_genres = splited_genres.drop(columns=['drop'])

    value_counts = splited_genres.genre.value_counts().reset_index()
    value_counts.columns = ['genre', 'count']
    
    res = value_counts.loc[0].genre
    print(res)


# q17(data)


# # 18. Самый убыточный фильм от Paramount Pictures

# In[ ]:


answers['18'] = 'K-19: The Widowmaker (tt0267626)' # +


# In[88]:


def q18(data):
    slice = data[
        data.production_companies.str.lower().str.contains('paramount pictures')==True
    ] \
        .loc[:, ['original_title', 'imdb_id', 'profit']] \
        .sort_values(by=['profit']).reset_index() \
        .query('profit == profit.min()') \
        .loc[0]
    
    res = slice.original_title + ' (' + slice.imdb_id + ')'
    print(res)
    
    
# q18(data)


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[93]:


answers['19'] = '2015' # +


# In[92]:


def q19(data):
    slice = data.loc[:, ['release_year', 'profit']]         .groupby(['release_year']).profit.sum()         .sort_values(ascending=False).reset_index()         .query('profit == profit.max()')

    res = slice.loc[0].release_year
    print(res)


# q19(data)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[ ]:


answers['20'] = '2014' # +


# In[96]:


def q20(data):
    res = data[data.production_companies.str.lower().str.find('warner bros')>=0]         .loc[:, ['release_year', 'profit']]         .groupby(['release_year'])         .profit.sum()         .sort_values(ascending=False).reset_index()         .query('profit == profit.max()')         .loc[0]         .release_year

    print(res)


# q20(data)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[ ]:


answers['21'] = 'Сентябрь' # +


# In[98]:


def q21(data):
    slice = data         .loc[:, ['release_date']]         .release_date.str.split('/', expand=True)         .drop(columns=[1,2])

    slice.columns = ['month']

    slice = slice.month.value_counts().reset_index()
    slice.columns = ['month', 'amount']

    res = slice[slice.amount == slice.amount.max()].loc[0].month
    print(res)


# q21(data)


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[ ]:


answers['22'] = 450 # +


# In[99]:


def q22(data):
    slice = data         .loc[:, ['release_date']]         .release_date.str.split('/', expand=True)         .drop(columns=[1,2])

    slice.columns = ['month']

    slice = slice.month.value_counts().reset_index()

    slice.columns = ['month', 'amount']

    slice = slice[slice.month.isin(['6', '7', '8'])]

    res = slice.amount.sum()
    print(res)


# q22(data)


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[ ]:


answers['23'] = 'Peter Jackson' # +


# In[111]:


def q23_old(data):
    df = data.release_date.str.split('/', expand=True)
    df['director'] = data['director']
    df = df.drop(columns=[1,2])
    df.columns = ['month', 'director']
    df = df[df['month'].isin(['1', '12', '2'])]
    df = df['director'].value_counts().reset_index()
    df.columns = ['director', 'count']
    res = df.loc[0].director
    print(res)


# q23_old(data)


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[ ]:


answers['24'] = 'Four By Two Productions' # +


# In[102]:


def q24(data):
    df = data.loc[:, ['production_companies', 'original_title']]
    df.columns = ['companies', 'title']
    df = pd.DataFrame(df.companies.str.split('|').tolist(), index=df.title)        .stack().reset_index()        .drop(columns=['level_1'])

    df.columns = ['title', 'company']

    df['len'] = df.title.str.len()

    df = df.drop(columns=['title'])        .groupby(['company']).len.mean().reset_index()        .query('len == len.max()')

    res = df.company.to_string(index=False)
    print(res)


# q24(data)


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:


answers['25'] = 'Midnight Picture Show' # +


# In[103]:


def q25(data):
    df = data.loc[:, ['production_companies', 'overview']]
    df.columns = ['companies', 'overview']

    df = pd.DataFrame(df.companies.str.split('|').tolist(), index=df.overview)        .stack().reset_index()        .drop(columns=['level_1'])

    df.columns = ['overview', 'company']
    df['len'] = df.overview.str.split(' ').str.len()


    res = df        .drop(columns=['overview'])        .groupby(['company']).len.mean().reset_index()        .query('len == len.max()')        .company.to_string(index=False)
    print(res)


# q25(data)


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[ ]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave' # +


# In[108]:


def q26(data):
    df = data.loc[:, ['original_title', 'vote_average']]
    df.columns = ['title', 'rate']
    df = df.sort_values(['rate'], ascending=False)        .head(int(math.floor(df.title.count() * 0.01))).reset_index()

    res = df.title.tolist()
    print(res)


# q26(data)


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[ ]:


answers['27'] = 'Daniel Radcliffe & Rupert Grint' # +


# In[110]:


def q27(data):
    df = pd.DataFrame(
        data['cast']
        .str.split('|')
        .apply(lambda cast: list(itertools.combinations(cast, 2)))
        .tolist()
    )\
        .stack().reset_index()\
        [0].value_counts().reset_index()

    df.columns = ['actors', 'count']
    df = df.query('count == count.max()').actors
    
    print(df)


# q27(data)


# # Submission

# In[ ]:


# в конце можно посмотреть свои ответы к каждому вопросу
print(answers)


# In[ ]:


# и убедиться что ни чего не пропустил)
print(len(answers))


# In[ ]:





# In[ ]:




