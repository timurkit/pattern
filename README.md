# pattern
Без использования регулярных выражений! Ввести строку, содержащую произвольные символы (кроме символа «@»). Затем ввести строку-шаблон, которая может содержать символы '@'. Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде, кроме символов '@'; на месте '@' в исходной строке должен стоять ровно один произвольный символ. Вывести наименьшую позицию в строке, с которой начинается эта подстрока, или '-1', если её там нет. 

Input:
```
lorem ipsum, quia dolor sit, amet, consectetur
dolor @it,@@met
```
Output:
```
18
```

Input:
```
qwerwq er bababaobaber
ba@ba
```
Output:
```
14
```
