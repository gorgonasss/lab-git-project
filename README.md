# lab-git-project
a skill development project
# Создание нового репозитория на GitHub/GitLab:
Репозиторий был создан с именем “lab-git-project”
# Настройка локальной среды разработки:
Так как в предыдущих проектах я уже использовала Git, то при выполнении данного пункта задания я только дополнительно настроила глобальные параметры, а именно имя пользователя.  
git config --global user.name "Serafima"
# Создание структуры проекта:
git clone https://github.com/gorgonasss/lab-git-project.git  
cd lab-git-project  
mkdir src tests  
type nul > src/main.py  
type nul > src/utils.py  
type nul > tests/test_main.py  
type nul > README.md  
type nul > .gitignore  
type nul > requirements.txt  
Код добавленный в main.py:  
"# main.py  
if __name__ == "__main__":  
print("Hello from main.py!")"  
Код добавленный в utils.py:  
"# utils.py"  
# Инициализация репозитория и первый коммит:
git add .  
git commit -m "Initial project setup"  
git push origin main  
# Разработка новых функций/компонентов: 6 Работа с ветками:
git checkout -b feature/add-numbers  
git add .  
git commit -m "Add add_numbers function"  
git push --set-upstream origin feature/add-numbers  
git checkout main  
git checkout -b feature/multiply-numbers  
git add .  
git commit -m "Add multiply_numbers function"  
git push --set-upstream origin feature/multiply-numbers  
В ходе выполнения этих пунктов я добавила код в файлы main.py и utils.py и сохранила отдельно функции в двух новых ветках.  
# Создание pull request'ов:  8 Обработка конфликтов:
git checkout feature/add-numbers  
git add .  
git commit -m "Modify add_numbers"  
git push  
git checkout feature/multiply-numbers  
git add .  
git commit -m "Modify multiply_numbers "  
git push  
git add .  
git commit -m "Resolve merge conflict"  
С помощью данных команд я сохраняю изменения в ветках и соответственно решаю проблему слияния.  
# Работа с тегами:
git tag v1.0  
git push origin v1.0  
# Работа с stash:
git stash  
git stash apply  
# Работа с rebase:
git checkout -b feature/new-function  
git add .  
git commit -m "Add new_function"  
git add .  
git commit -m "Use new_function"  
git rebase main  
# Работа с cherry-pick:
git log --oneline  
git checkout main  
git cherry-pick <commit-hash>  
# Работа с .gitignore:
Были добавлен код по примеру из задания, после изменений были выполнены комманды:  
git add .  
git commit –m “”  
git push  
# История и восстановление изменений:
git log --oneline --graph --all  
git restore src/utils.py  
git reset --hard <commit-hash> //вместо <commit-hash> был выбран хэш коммита из ветки feature/multiply-numbers  
# Дополнительные задачи:
На сайте github.com я настроила GitHub Actions и подтянула изменения на локальный репозиторий с помощью команды git pull. После на сайте я создала issue.   
# Вывод
В данном описании проекта я постаралась прописать те комманды, что я использовала при работе с данной ПЗ.