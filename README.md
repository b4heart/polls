# polls
polls


## Creating a new project
* Make an empty folder on your PC. Let's call it as 'top'
* Example: C:\<user>\python\webapp\blog\
* Go to github.com and login
* Click on start a project. And name it. Click on initiate README. .gitignore -> select Python. Add license as MIT
* click on Code / Clone to copy the .git file link
* Now go to the empty folder on your PC and do a Git Clone.
* cd to the project folder that got created after cloning
* Update the readme file (README.md)
* Git Add, Git Commit, and Git Push


## Git Commands
* Git Clone
`>git clone https://github.com/<yourid>/<your project>.git`
* Git Add
`>git add *`
* Git Commit
`>git commit -m "Added initial readme file"`
* Git Push
`>git push`
* Git Change username:
`>git config --local credential.helper ""`
`>git push origin master`
*  Git pull
`>git pull`


## Creating a virtual environment
* Go to the 'top' folder (from your project folder type `>cd ..`)
* Create an env folder. `>virtualenv env`
* On Windows: `>env\Scripts\activate`
* On Linux/Ubuntu: `source env/bin/activate.csh`
* Install your packages. For Webapp Django projects, you can use: `>pip install Django`


## Coding Abstraction Levels (from Lowest level to high level)
1. Binary Code. It is all zeros and ones
2. Assembly Code. Example: JMP, GOTO, ...
3. Compiled code. Example: C, C++, ...
4. Interpreter/Script/Backend code. Example: Python 3.7, Go, .... In our case, this is our starting point.
5. Packages (libraries):  Example pygame, Django, ...

* Databases (mechanism to store the information): Relational (Example: SQLite(we will use SQLite), MYSQL, MSSQL), Non Relational (Nosql, ...)
* Front End code: html, css, javascript

## References
* https://docs.djangoproject.com/en/2.2/intro/
