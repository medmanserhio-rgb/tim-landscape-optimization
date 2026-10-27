# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. ЗАГРУЗКА И ПОДГОТОВКА ДАННЫХ ИЗ ВКР
try:
    df = pd.read_excel('vkr_landscape_data.xlsx')
    print("Успех: Данные ВКР успешно загружены в Python!")
except FileNotFoundError:
    print("Запущен демонстрационный режим на сгенерированных ТИМ-данных.")
    data = {
        'coord_X': np.random.uniform(0, 100, 1000),
        'coord_Y': np.random.uniform(0, 100, 1000),
        'height': np.random.uniform(2, 25, 1000),
        'crown_diam': np.random.uniform(1.5, 12, 1000),
        'wind_coef': np.random.uniform(0.1, 0.8, 1000),
        'E_wind': np.random.uniform(10, 90, 1000)
    }
    df = pd.DataFrame(data)

# 2. РАЗДЕЛЕНИЕ НА ПРИЗНАКИ И ЦЕЛЕВУЮ ПЕРЕМЕННУЮ
features = ['coord_X', 'coord_Y', 'height', 'crown_diam', 'wind_coef']
X = df[features]
y = df['E_wind']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

# 3. ИНИЦИАЛИЗАЦИЯ И ОБУЧЕНИЕ МОДЕЛИ RANDOM FOREST
forest = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
forest.fit(X_train, y_train)

# 4. ПРОВЕРКА КАЧЕСТВА
y_pred = forest.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\nМЕТРИКИ КАЧЕСТВА ОБУЧЕННОЙ ИИ-МОДЕЛИ:")
print(f"Коэффициент детерминации R²: {r2:.2f}")
print(f"Средняя абсолютная ошибка MAE: {mae:.2f}%")
