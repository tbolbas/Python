"""Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая при этом, что при некоторых
значениях К слово «лет» надо заменить на слово «год» или «года»."""
for k in range(1,10):
    s = "Мне "+str(k);
    if k == 1:
        s += " год"
    elif 1 < k < 5:
        s += " года"
    else:
        s += " лет"
    print(s)
