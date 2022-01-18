## Flask_magazyn - system accountant dostępny przez stronę www

Stwórz aplikację webową do zarządzania magazynem i księgowością.
Strona główna powinna wyświetlać obecny stan magazynowy, obecne saldo oraz zawierać **trzy formularze**:
1. **Formularz do zakupu**:
Z polami: nazwa produktu, cena jednostkowa, liczba sztuk
2. **Formularz do sprzedaży**:
Z polami: nazwa produktu, cena jednostkowa, liczba sztuk
Po wypełnieniu i przesłaniu danych z tych formularzy odśwież stronę bądź wydrukuj komunikat błędu, jeśli dane nie były prawidłowe i ponownie wyświetl stronę ze stanami magazynowymi.
3. **Formularz zmiany salda**:
Z polami: komentarz, wartość (tylko liczbowa)


Dodaj podstronę Historia, która będzie pobierać dwa opcjonalne parametry (od, do):
/historia/
/historia/<line_from>/<line_to>/
Jeśli nie podano parametrów, wyświetl całą historię, jeśli podano - wyświetl tylko dane z zakresu. Postępuj podobnie jak w przypadku polecenia przegląd.

Wykorzystaj kod piszący i czytający z pliku z zadania accountant.py
