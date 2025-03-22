Если ты хочешь запустить проект локально, то сперва

1 - Установи venv (виртуальное окружение)

py -m venv venv  - создание виртуального окружения.

venv/Scripts/Active - запускает виртуалку(в консоли venv загорится)

2 - Перейди в venv, запусти и в нем уже установи пакеты из файла requirements.txt

pip install -r .\requirements.txt
pip freeze > .\requirements.txt  - добавляет новые установленные библы в файл requirements

3 - Чтобы запустить лок хост то используем команду
uvicorn main:app --port "0000" --reload (main - это py файл, app - внутри переменная запуска FastAPI