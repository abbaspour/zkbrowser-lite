ZooKeeper Browser - Lite
========================

Required Modules
----------------
* zkpython 
* web.py

Installing
----------

    sudo easy_install web.py
    Install zkpython from contrib folder of zookeeper distribution.

or

    sudo aptitude install python-webpy
    sudo aptitude install python-zookeeper


Usage
-----
Open code.py and change zookeeper server address, here:

    zkc = ZooKepperConnection("192.168.0.71:2181")

Running
-------
Run project

    python code.py [port]


Now point your browser to http://localhost:[port]

Default port is 8080.

Screenshot
----------
![Sample Output](http://aminsblog.files.wordpress.com/2010/12/zkbrowser-lite.png)

