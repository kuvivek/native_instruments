The Code has been tested on Python 2.7.5

Steps:

1)Created a folder called native_instruments in the Desktop. Then using the `virtualenv`
  command create a virtual environment for this python based project. 

    [kuvivek@vivekcentos native_instruments]$ virtualenv rest_api

Note: `virtualenv` command is available by executing the following command 

    [kuvivek@vivekcentos native_instruments]$
    [kuvivek@vivekcentos native_instruments]$ sudo pip install virtualenv
    [kuvivek@vivekcentos native_instruments]$

2) Once the virtual environment is created it is required to activate the 
virtual environment. The command to activate the same is:

>     [kuvivek@vivekcentos native_instruments]$
>     [kuvivek@vivekcentos native_instruments]$ source rest_api/bin/activate
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ which python
>     ~/Desktop/native_instruments/rest_api/bin/python
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ python --version
>     Python 2.7.5
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

3) After developing the REST API Backend framework 

>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ ls
>     app.py  chores-collection.db  database_setup.py  database_setup.pyc  __init__.py  populate_db.py  populate_db.pyc  README.md resources.py  resources.pyc  rest_api
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 

The flask web based application server need to be started. The starting point of this application server is app.py. end Inorder to start the application server, so as to expose the sought REST API calls and support the Stanadard  HTTP Headers, following commands is used:

    (rest_api) [kuvivek@vivekcentos native_instruments]$
    (rest_api) [kuvivek@vivekcentos native_instruments]$ python app.py
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 113-909-490

4) Now run another terminal and execute the curl commands to verify all the Standard HTTP protocols.
Note: For getting errorcode, from any of the curl command, add -i option, as shown in HEAD request below.

Since there are no records initially, Hence reporting empty list.

    (rest_api) [kuvivek@vivekcentos native_instruments]$ 
    (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -X GET http://127.0.0.1:5000/keys
    []
    (rest_api) [kuvivek@vivekcentos native_instruments]$ 
    (rest_api) [kuvivek@vivekcentos native_instruments]$ 

5) Lets push some data using the POST command  

        (rest_api) [kuvivek@vivekcentos native_instruments]$ 
        (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -d '{"chore1": "Wake up at 6 in the morning"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/keys
        {
          "chore1": "Wake up at 6 in the morning"
        }
        (rest_api) [kuvivek@vivekcentos native_instruments]$

>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/keys -d '{"chore2":  "Prepare breakfast and lunch box for daughter before 7:00 A.M "}'
>         {
>           "chore2": "Prepare breakfast and lunch box for daughter before 7:00 A.M "
>         } 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

6) Try to post the data for the same key using POST header, which is not supported
But the same can be achieved via the PUT request.

>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/keys -d '{"chore2": "Go for morning walk from 7:30 A.M."}'
>     Chore title already exist.
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/keys/chore2 -d '{"chore2": "Go for morning walk from 7:30 A.M."}'
>     Updated the chore with id chore2
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

7) Now, Query for all the keys, the second one which was modified should be 
updated one, from the value what was added in Step 5)

>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl http://127.0.0.1:5000/keys
>     [
>       {
>         "chore1": "Wake up at 6 in the morning"
>       },
>       {
>         "chore2": "Go for morning walk from 7:30 A.M."
>       }
>     ]
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

8) Now lets add one more chore and then delete that chore.

>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/keys -d '{"chore3": "Eat breakfast by 8:30."}'
>     {
>       "chore3": "Eat breakfast by 8:30."
>     }
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl http://127.0.0.1:5000/keys
>     [
>       {
>         "chore1": "Wake up at 6 in the morning"
>       },
>       {
>         "chore2": "Go for morning walk from 7:30 A.M."
>       },
>       {
>         "chore3": "Eat breakfast by 8:30."
>       }
>     ]
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -X DELETE  http://127.0.0.1:5000/keys/chore3
>     Removed Chore with id chore3 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl http://127.0.0.1:5000/keys
>     [
>       {
>         "chore1": "Wake up at 6 in the morning"
>       },
>       {
>         "chore2": "Go for morning walk from 7:30 A.M."
>       }
>     ] (rest_api) [kuvivek@vivekcentos native_instruments]$


9) Verify whether a key exist or not using HEAD HTTP request. Since the REST API Service supported by the flask web application server gives json response in case of success and html error page with failure query. Attempting failure request first by looking for record which was deleted in the previous step. 

>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -X HEAD -i http://127.0.0.1:5000/keys/chore3
>     HTTP/1.0 200 OK
>     Content-Type: text/html; charset=utf-8
>     Content-Length: 21
>     Server: Werkzeug/0.15.5 Python/2.7.5
>     Date: Fri, 16 Aug 2019 06:53:07 GMT
>     
>     curl: (18) transfer closed with 21 bytes remaining to read
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

10) Trying the HEAD Request with actual record. Here the response type is application/json,
unlike previous previous response, wherein the response is an html error page.

>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -X HEAD -i http://127.0.0.1:5000/keys/chore2
>     HTTP/1.0 200 OK
>     Content-Type: application/json
>     Content-Length: 53
>     Server: Werkzeug/0.15.5 Python/2.7.5
>     Date: Fri, 16 Aug 2019 06:53:15 GMT
>     
>     curl: (18) transfer closed with 53 bytes remaining to read
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ 
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

 
11) Deleting all the keys.

>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl -X DELETE http://127.0.0.1:5000/keys
>     2 records deleted
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$ curl http://127.0.0.1:5000/keys
>     []
>     (rest_api) [kuvivek@vivekcentos native_instruments]$
>     (rest_api) [kuvivek@vivekcentos native_instruments]$

12) Dockerizing the application.
Create a Dockerfile and docker-compose.yml file for this flask web application Install docker engine and docker-compose binary and modify the app.py to expose the 5000 and allow connection from outside container. For this instead of first parameter 127.0.0.1 in the app.run() 
function, change it to 0.0.0.0. So that it is accessible from outside world.

Executing the following command, builds the image and launches the Web application container, and all the behaviours can be tested locally using the curl command.

    [kuvivek@vivekcentos native_instruments]$
    [kuvivek@vivekcentos native_instruments]$ sudo /usr/local/bin/docker-compose up
    Building web
    Step 1/6 : FROM python:2.7
    2.7: Pulling from library/python
    4ae16bd47783: Pull complete
    bbab4ec87ac4: Pull complete
    2ea1f7804402: Pull complete
    96465440c208: Pull complete
    6ac892e64b94: Pull complete
    6f7ce750b843: Pull complete
    886c714e5c8c: Pull complete
    11129766a052: Pull complete
    4a086c8425c2: Pull complete
    Digest: sha256:42b8afcfec99c9d2aa2410ab680d53fdcea328d38ca876e2bd3dad089cb0ed0c
    Status: Downloaded newer image for python:2.7
     ---> d75b4eed9ada
    Step 2/6 : MAINTAINER Vivek Kumar, vivekkumar.bitsindri@gmail.com
     ---> Running in b1708cdc88d6
    Removing intermediate container b1708cdc88d6
     ---> ff1b311cbbcf
    Step 3/6 : COPY ./requirements.txt /code/requirements.txt
     ---> a699d2eb625d
    Step 4/6 : WORKDIR /code
     ---> Running in b0e10164648e
    Removing intermediate container b0e10164648e
     ---> 508eeae87a53
    Step 5/6 : RUN pip install -r requirements.txt
     ---> Running in 257771b5f7a9
    DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 wouldn't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
    Collecting Click==7.0 (from -r requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
    Collecting Flask==1.1.1 (from -r requirements.txt (line 2))
      Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    Collecting Flask-Caching==1.7.2 (from -r requirements.txt (line 3))
      Downloading https://files.pythonhosted.org/packages/bd/4e/c701bdcd566f26187398cf058ad2ca14c8b2f50b17a17f9076794ae2f8db/Flask_Caching-1.7.2-py2.py3-none-any.whl
    Collecting itsdangerous==1.1.0 (from -r requirements.txt (line 4))
      Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
    Collecting Jinja2==2.10.1 (from -r requirements.txt (line 5))
      Downloading https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl (124kB)
    Collecting MarkupSafe==1.1.1 (from -r requirements.txt (line 6))
      Downloading https://files.pythonhosted.org/packages/fb/40/f3adb7cf24a8012813c5edb20329eb22d5d8e2a0ecf73d21d6b85865da11/MarkupSafe-1.1.1-cp27-cp27mu-manylinux1_x86_64.whl
    Collecting SQLAlchemy==1.3.6 (from -r requirements.txt (line 7))
      Downloading https://files.pythonhosted.org/packages/55/98/56b7155bab287cd0c78dee26258835db36e91f2efef41f125ed6f6f1f334/SQLAlchemy-1.3.6.tar.gz (5.9MB)
    Collecting Werkzeug==0.15.5 (from -r requirements.txt (line 8))
      Downloading https://files.pythonhosted.org/packages/d1/ab/d3bed6b92042622d24decc7aadc8877badf18aeca1571045840ad4956d3f/Werkzeug-0.15.5-py2.py3-none-any.whl (328kB)
    Building wheels for collected packages: SQLAlchemy
      Building wheel for SQLAlchemy (setup.py): started
      Building wheel for SQLAlchemy (setup.py): finished with status 'done'
      Created wheel for SQLAlchemy: filename=SQLAlchemy-1.3.6-cp27-cp27mu-linux_x86_64.whl size=1183929 sha256=b2fb9155f55ad95988c4dc555da49cb1c85c21f491210f3ef365bbd7735d6669
      Stored in directory: /root/.cache/pip/wheels/f2/ec/e0/d7deb0c981557e373edf7370574b7001690892afe5fea30c3c
    Successfully built SQLAlchemy
    Installing collected packages: Click, Werkzeug, itsdangerous, MarkupSafe, Jinja2, Flask, Flask-Caching, SQLAlchemy
    Successfully installed Click-7.0 Flask-1.1.1 Flask-Caching-1.7.2 Jinja2-2.10.1 MarkupSafe-1.1.1 SQLAlchemy-1.3.6 Werkzeug-0.15.5 itsdangerous-1.1.0
    Removing intermediate container 257771b5f7a9
     ---> 438bdb5bbbbc
    Step 6/6 : CMD python app.py
     ---> Running in 6abfc47fcb0b
    Removing intermediate container 6abfc47fcb0b
     ---> 960b38b1cb55
    Successfully built 960b38b1cb55
    Successfully tagged native_instruments_web:latest
    WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
    Creating native_instruments_web_1_8dbcce0886c3 ... done
    Attaching to native_instruments_web_1_d4e0dc6eb82b
    web_1_d4e0dc6eb82b |  * Serving Flask app "app" (lazy loading)
    web_1_d4e0dc6eb82b |  * Environment: production
    web_1_d4e0dc6eb82b |    WARNING: This is a development server. Do not use it in a production deployment.
    web_1_d4e0dc6eb82b |    Use a production WSGI server instead.
    web_1_d4e0dc6eb82b |  * Debug mode: on
    web_1_d4e0dc6eb82b |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    web_1_d4e0dc6eb82b |  * Restarting with stat
    web_1_d4e0dc6eb82b |  * Debugger is active!
    web_1_d4e0dc6eb82b |  * Debugger PIN: 203-920-586


