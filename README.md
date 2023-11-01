# blog_app
Simple blog app backend using fastapi.
Implementing Clean Architecture.
Using sqlite as DB but YOu can use any sql database. 

---- Prerequisite----
1-Using Poetry to manage dependencies version-1.6.1 All the dependencies are in pyproject.toml file inside BLOG directory.
2-Using miniconda to manage virtual enviornments.
3- Pyhton 3.9

----Poetry------
# pip install poetry

--conda enviornment----
conda create -n <"YOUR-ENVIORNMENT-NAME"> python=3.9 
conda actibvate <"YOUR-ENVIORNMENT-NAME">

---Installing required packages-----
After activating your virtual enviornment go inside blog_app/BLOG and run --> poetry install
above step will install all the packages in pyproject.toml inside your virtual enviornment.

-----Start app------
1- got to  entrypoint and run app.py
2- got to localhost:5005/docs
