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
ALTER TABLE band ADD members INTEGER
UPDATE band SET members=4 WHERE id=1;
UPDATE band SET members=5 WHERE id=2;
UPDATE band SET members=9 WHERE id=3;
```

```sqlite
UPDATE band SET members=5 WHERE id=3;
```

```sqlite
DELETE FROM band WHERE id=2;
```

