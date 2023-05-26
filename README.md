# FastAPI template

## ディレクトリ構成

```
.
├── Makefile
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   │   └── schemas.py
│   ├── config.py
│   ├── db
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── main.py
│   ├── services
│   │   ├── __init__.py
│   │   └── users.py
│   └── tests
│       ├── __init__.py
│       └── test_users.py
├── poetry.lock
└── pyproject.toml
```

### 環境構築

```sh
make init
```

### 開発環境での実行

```sh
make run
```

### テスト

```sh
make test
```
