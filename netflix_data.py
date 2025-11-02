import pandas as pd

df = pd.read_csv('netflix_titles.csv')

# Фильтрация данных
movie = df[df['type'] == 'Movie']
tv_show = df[df['type'] == 'TV Show']

# Группировка по годам
movie_count = movie.groupby('release_year').count()
tv_show_count = tv_show.groupby('release_year').count()

# Ваши задания для практики:
# 1. Посмотрите на данные: df.head(), df.info(), df.describe()
# 2. Посчитайте сколько фильмов и сериалов
# 3. Найдите топ-5 лет по количеству фильмов
# 4. Проанализируйте рейтинги
# 5. Создайте графики (matplotlib)
