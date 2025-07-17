### FastAPIのTemporary Redirectのデモコード  

### 記事
[]()

#### 実行コマンド
以下、1,2どちらでも可能です。 

- `endpoint_1.py` 
1. ```python endpoint_1.py```
2. ```uvicorn endpoint_1:app --reload --port 8000```

- `endpoint_2.py` 
1. ```python endpoint_2.py```
2. ```uvicorn endpoint_2:app --reload --port 8080```

テストする場合は`endpoint_1.py`と`endpoint_2.py`を両方立ち上げてください。  

#### 画面表示  
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)  

#### 参考サイト  
- [https://fastapi.tiangolo.com/ja/advanced/custom-response/#redirectresponse](https://fastapi.tiangolo.com/ja/advanced/custom-response/#redirectresponse)
- [https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/307](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/307)  
- [https://qiita.com/naka_kyon/items/6afe6c1ead871977a15a](https://qiita.com/naka_kyon/items/6afe6c1ead871977a15a)  
