```sqlite
CREATE TABLE bands (id INTEGER, name TEXT, debut INTEGER)
INSERT INTO bands(name, debut)
VALUES ("Queen", 1973);
INSERT INTO bands(name, debut)
VALUES ("Coldplay", 1998);
INSERT INTO bands(name, debut)
VALUES ("MCR", 2001);

```

```sqlite
SELECT id, name FROM bands;
```

```sqlite
SELECT name FROM bands WHERE debut<=2000;
```

