Запуск тестов по ключевому слову файла/теста
pytest -v -k   "ключевое слово/часть слова"

pytest -v -k "auth" --tb=no   (tb'Trace Back' = no)   не показывать сообщения с ошибками

pytest -v -k "auth or case" --tb=no     Запуск тестов содержащих слово auth или case

pytest -v --tb=no --maxfail=3  Запуск теста который остановиться после 3 провальных проверок

pytest --collect-only  Возвращяет список тест кейсов без их запуска

pytest -v --tb=no --lf  Запускает только последние проваленные проверки

pytest -v --tb=no --ff  Запускает прогон со всеми тестами, проваленные запускаются первыми




