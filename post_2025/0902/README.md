### FastAPIのTemporary Redirectのデモコード  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/09/02/231908](https://fallpoke-tech.hatenadiary.jp/entry/2025/09/02/231908)

#### 実行コマンド
以下、1,2どちらでも可能です。 

- `endpoint.py` 
1. ```python endpoint.py```
2. ```uvicorn endpoint:app --reload --port 8000```  

#### 画面表示  
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)  

#### 参考サイト  
- [https://fastapi.tiangolo.com/advanced/events/](https://fastapi.tiangolo.com/advanced/events/)
- [https://openillumi.com/fastapi-app-state-lifespan-object-reuse/](https://openillumi.com/fastapi-app-state-lifespan-object-reuse/)
