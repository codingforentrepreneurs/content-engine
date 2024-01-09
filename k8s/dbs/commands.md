
Path: `postgres://username@pgpassword:db.default.svc.cluster.local/dbname`

Using kubectl port-forward
```bash
kubectl port-forward svc/db 5432:5432
PGPASSWORD=pgpassword psql -h localhost -p 5432 -U username -d dbname

```
Using Twingate
```bash
PGPASSWORD=pgpassword psql -h db.default.svc.cluster.local -p 5432 -U username -d dbname
```