Лабораторна робота № 1. Введення в Python

Мета: створення консольної програми-калькулятора за допомогою основних синтаксичних конструкцій Python, з іншим завданням на заміну тестуванню та валідації:
План роботи:
  Завдання 1: Введення користувача
  Створіть Python-програму, яка приймає введення користувача для двох чисел і оператора (наприклад, +, -, *, /).
  Завдання 2: Перевірка оператора
  Перевірте чи введений оператор є дійсним (тобто одним із +, -, *, /). Якщо ні, відобразіть повідомлення про помилку і попросіть користувача ввести дійсний оператор.
  Завдання 3: Обчислення
  Виконайте обчислення на основі введення користувача (наприклад, додавання, віднімання, множення, ділення) і відобразіть результат.
  Завдання 4: Повторення обчислень
  Запитайте користувача, чи він хоче виконати ще одне обчислення. Якщо так, дозвольте йому ввести нові числа і оператор. Якщо ні, вийдіть з програми.
  Завдання 5: Обробка помилок
  Реалізуйте обробку помилок для обробки ділення на нуль або інших потенційних помилок. Відобразіть відповідне повідомлення про помилку, якщо виникає помилка.
  Завдання 6: Десяткові числа
  Змініть калькулятор так, щоб він обробляв десяткові числа (плаваючу кому) для більш точних обчислень.
  Завдання 7: Додаткові операції
  Додайте підтримку додаткових операцій, таких як піднесення до степеня (^), квадратний корінь (√) і залишок від ділення (%).
  Завдання 8: Функція пам'яті
  Реалізуйте функцію пам'яті, яка дозволяє користувачам зберігати і відновлювати результати. Додайте можливості для зберігання та отримання значень з пам'яті.
  Завдання 9: Історія обчислень
  Створіть журнал, який зберігає історію попередніх обчислень, включаючи вираз і результат. Дозвольте користувачам переглядати історію своїх обчислень.
  Завдання 10: Налаштування користувача
  Надайте користувачам можливість налаштувати поведінку калькулятора, таку як зміну кількості десяткових розрядів, які відображаються, або налаштування функцій пам'яті.

Висновки. Виконавши ці завдання, ви створите простий консольний калькулятор на Python, який може виконувати арифметичні операції, обробляти помилки та надавати користувачу зручний інтерфейс. 
Цей проект допоможе вам вивчити основний синтаксис Python і концепції, такі як введення користувача, умовні оператори, цикли та обробка помилок.

Результати роботи мають бути представлені репозитаріі GitHub. Звіт про виконання лабораторної роботи має бути складений за загальними правилами, які прийняті в університеті

MC = Memory Clear встановлює пам’ять на 0 
MR = Memory Recall використовує номер у пам’яті, діє так, ніби ви самі ввели цей номер 
MS = Memory Store записує номер на дисплеї в пам’ять 
M+ = Memory Add приймає номер на дисплей, додає його до пам’яті та поміщає результат у пам’ять
Кнопки можуть бути зручними для повторних обчислень з одним числом. Наприклад, якщо ви хочете помножити кілька чисел на пі, ви можете ввести наступне:
3,14159.. MS (зберігає число) 4 x MR = (дає вам 4 помножені на пі) 25 x 25 x MR = (дає вам 25x25 помножити на пі)
Кнопка M+ може бути зручною для з’ясування складних виразів, якщо у вас немає наукового калькулятора. Наприклад, щоб обчислити (5 x 6) + (12 x 2) + (3 x 7), ви можете зробити наступне:
5 x 6 = (калькулятор каже 30) MS (зберігає 30 у пам’яті) 12 x 2 = (калькулятор каже 24) M+ (бере 24, додає його до 30, зберігає результат 54 у пам’яті) 3 x 7 = (21) M+ ( приймає 54, додає 21, зберігає результат 75) MR (відображає результат 75)
