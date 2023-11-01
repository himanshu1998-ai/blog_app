# blog_app
Simple blog app backend using fastapi.
Implementing Clean Architecture.
Using sqlite as DB but YOu can use any sql database. 

---- Prerequisite----
1-Using Poetry to manage dependencies version-1.6.1 All the dependencies are in pyproject.toml file inside BLOG directory.
2-Using miniconda to manage virtual environments.
3- Python 3.9

----Poetry------
# pip install poetry

--conda environment----
conda create -n <"YOUR-ENVIRONMENT-NAME"> python=3.9
conda activate <"YOUR-ENVIRONMENT-NAME">

---Installing required packages-----
After activating your virtual ENVIRONMENT go inside blog_app/BLOG and run --> poetry install
above step will install all the packages in pyproject.toml inside your virtual ENVIRONMENT.

-----Start app------
1- got to  entrypoint and run app.py
2- got to localhost:5005/docs

