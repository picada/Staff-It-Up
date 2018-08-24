# Asennusohje

Ohjeet on kirjoitettu macOS-käyttöjärjestelmälle.

## Sovelluksen asentaminen paikallisesti

### 1. Esitietovaatimukset

Ohjelman käyttö edellyttää, että tietokoneessa on asennettuna sekä sqlite3 että tuki Python-kielisten ohjelmien suorittamiseen, 
vähintään Pythonin versio 3.5. Käytössä tulee myös olla sekä Pythonin pip että venv-kirjasto, joista molemmat kuuluvat oletuksena uusimpiin
Python-versioihin.

### 2. Sovelluksen lataaminen omalle koneelle

Lataa sovellus ZIP-tiedostona osoitteesta [GitHubista](https://github.com/picada/Staff-It-Up) Clone or download -linkin kautta ja pura
tiedosto haluamaasi kansioon.

Voit myös kloonata projektin valitsemaasi kansioon suoraan terminaalin kautta

```$ git clone git@github.com:picada/Staff-It-Up.git```

### 3. Virtuaaliympäristön luominen ja riippuvuuksien lataaminen

Varmista, että olet komentorivillä projektin juurikansiossa. Luo ja ota käyttöön Pythonin virtuaaliympäristö:

```$ python3 -m venv venv
$ source venv/bin/activate```

Tämän jälkeen asenna sovelluksen vaatimat riippuuvuudet, jotka on määritelty requirements.txt-tiedostossa:

```$ pip install -r requirements.txt```

### 4. Ensimmäiset käyttäjät

Sovelluksen mukana tulee staffitup.db -tietokanta, josta tulisi löytyä valmiina sekä admin-rooli että yksi admin-käyttäjä (käyttäjätunnus 
= admin, salasana = admin). Jos käyttäjä tai roolit jostain syystä kuitenkin puuttuvat, voit lisätä tarvittavat tietokohteet terminaalin kautta
(voit halutessasi vaihtaa nimen, käyttäjätunnuksen ja salasanan mieleiseksisi):

```
$ sqlite3 application/staffitup.db 
sqlite> INSERT INTO account (name, username, password) VALUES ('Admin', 'admin', 'admin');
sqlite> INSERT INTO role (name) VALUES ('admin');
sqlite> INSERT INTO account_role (account_id, role_ide) VALUES (1, 1);
```

User-oikeuksilla varustettuja käyttäjiä voi luoda suoraan sovelluksen kautta. 
HUOM! Yllä olevat komennot tulee suorittaa ennen ensimmäisten user-käyttäjien luomista, jotta tiedot tallentuvat oikein.

### 5. Sovelluksen käynnistäminen

Sovelluksen käynnistäminen taphatuu komennolla

```$ python3 run.py```

Käynnistämisen jälkeen voit käyttää sovellusta paikallisesti selaimessa osoitteessa (http://localhost:5000/)
