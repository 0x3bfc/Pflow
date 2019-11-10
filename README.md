# pflow
simple power flow calculation using pandapower

### Build
```bash
docker build -t pflow .
```

### Run

```bash
docker run -d -p 8000:8000 pflow
```

## APIs

- load [http://127.0.0.1/load](http://127.0.0.1/load)
- generator [http://127.0.0.1/generator](http://127.0.0.1/generator)
- List all [http://127.0.0.1/](http://127.0.0.1/)