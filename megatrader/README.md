# Пояснение
## Описание алгоритма
Классический метод 
[динамического программирования](https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5) 
с использованием таблицы мемоизации.
Считаем, что стоимость лота дискретна, минимлаьный шаг - 1 у.е.

Для каждого лота требуется посчитать:
* **profit** (какую выгоду мы с него 
получим) по формуле: `C*(1000-price*10) + C*1`
* **цена лота** (сколько стоит целиком) по формуле: `С*price*10`

где price - это цена лота в процентах, а С - количество облигаций в 
лоте.
При считывании оставляем только лоты с положительным профитом, т.к. лоты
с отрицатльным профитом нет смысла покупать 
(уменьшаем время работы алогоритма). 
### Составление таблицы мемоизации
Создаем таблицу из N+1 строк и S+1 столбцов, где N - количество лотов,
а S - сумма доступная трейдеру. Номер столбца - дискретное значение 
стоимости отличающиеся друг от друга на 1 у.е. Изначально таблица 
заполняется 0.
Первая строка и первый столбец остаются 0. Это случай, когда стоимость
равна 0 или количество выбранных лотов равно 0.

Далее построчно заполняем ячейки. 
Если можем купить лот(номер столбца больше, либо равен стоимости лота),
то выбираем максимальное из двух значений:
* Профит текущего лота и маскимального профита для предыдщего лота в 
колонке для стоимости меньшей на велечину стоимости текущего лота 
* Максимальный профит предыдущего лота для текущей стоимости

Это позволяет максимизировать суммарный профит лотов при одной и той же
суммарной стоимости.

### Восстановление списка лотов
Начиная с последнего элемента таблицы мемоизации \[N, S\]. Будем идти
в обратном порядке. Если значение профита в ячейке отличается от 
предыщего значения профита для предыщего лота той же цены, то 
1. записываем элемент
1. отнимаем стоимость от общей суммы доступной трейдеру на текущий 
момент
1. двигаемся дальше 

## Вычислительная сложность алгоритма
`O(NS)`, где - N количество лотов, S - сумма доступная трейдеру.
## Требования по памяти
Для вычисления требуется создать таблицу целочисленных элементов
размерностью N*S. `sys.getsizeof(int(1))` и `sys.getsizeof(int(100000))`
выдают значение в 28 байт. Значит, что память требуемя для вычисления
считается по формуле `28*N*S` (не считая памяти, которая требуется для 
хранения исходных подготовленных данных). 
## Ограничение на размер входных данных
Произведение количества лотов и доступных денежных средств трейдера
не должно превышать 12 500 000. Тогда время исполнение будет меньше 5 
секунд (может зависить от характеристик конкретной системы).  
## Субъективаная оценка сложности по 10ти балльной шкале
Моя субъективная оценка сложности **7**. 

Условие задачи достаточно запутано. Потребовалось время, чтобы понять 
его. 

Далее появилось желание решить задачу жадным методом, но достаточно 
быстро стало понятно, что решение не всегда будет оптимальным (придумал 
кейс). И стало ясно, что задача NP-полная. 

Т.к. для лота было выявлено 2 основных характеристики:
* профит от лота
* стоимость лота

Это сразу дало понимание, что данная задача представляет собой вариацию 
[задачи о рюкзаке](https://cutt.ly/IuG0agR).

Для решения этой задачи существуют уже готовые методы решения.
Был выбран вариант с мемоизацией. 


