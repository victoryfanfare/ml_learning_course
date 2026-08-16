# Установка окружения по операционным системам

Инструкция нужна один раз. Дальше вы работаете по разделу «Быстрый старт» в [README](../README.md).

---

## macOS

```bash
# Homebrew, если его нет
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install python@3.11 git
python3.11 --version
```

Дальше `python3.11 -m venv .venv` и по README.

---

## Windows

Мы работаем в **WSL2** - это Linux внутри Windows. Так у всех на потоке одинаковые команды, и не приходится разбираться, почему в PowerShell путь пишется иначе.

В PowerShell **от имени администратора**:

```powershell
wsl --install -d Ubuntu
```

Перезагрузиться, открыть приложение **Ubuntu**, задать логин и пароль. Дальше все команды курса выполняются в этом окне Ubuntu, а не в PowerShell:

```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv git
python3.11 --version
```

Проект держите внутри Linux-файловой системы (`~/projects/...`), а не в `/mnt/c/...` - иначе всё будет работать в разы медленнее.

VS Code / Cursor подключается к WSL расширением **WSL** (Remote): открываете папку прямо в Ubuntu.

Если WSL поставить не получается (корпоративный ноутбук, отключена виртуализация) - напишите куратору, разберём отдельно. Нативная установка на Windows возможна, но дальше вы будете чинить пути руками весь курс.

---

## Linux

```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv git
```

---

## Git: разовая настройка

```bash
git config --global user.name "Имя Фамилия"
git config --global user.email "почта@от.github"
```

Почта должна совпадать с той, что привязана к GitHub, иначе коммиты не свяжутся с вашим профилем.

Авторизация к GitHub - через [GitHub CLI](https://cli.github.com/), это проще, чем возиться с токенами:

```bash
gh auth login
```

---

## Если локально ничего не встало

Запасной вариант - **Google Colab**: ноутбук в браузере, ставить ничего не надо, плюс бесплатный GPU дальше по курсу.

Ограничение: Colab плохо дружит с git и с файлом `.env`. Поэтому первую домашку нужно сдать локально - её смысл именно в окружении и в git. Colab используем позже и как временное решение, а не как основной режим работы.
