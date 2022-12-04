# goit_module2_week10


Set virtual environment using `pipenv`:
```
pipenv install
pipenv shell
```

**Part 1**
Start Redis server (you need to have Docker installed)
```
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```
run fibbonaci script to test caching via redis
```
python fibonnaci.py
```



**Part 2**

start working personal assistant using
```
python main.py
```
to get help with available commands use
```
help 
```
to exit from program use
```
exit
```


