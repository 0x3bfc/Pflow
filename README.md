# pflow
simple power flow calculation using [pandapower](). 

### Topology 

It would be a load and a power generator of 0.02 MWs connected to the same bus bar, and an external connection to the grid (so essentially,the only modification to the example should be the addition of the power generator).

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
