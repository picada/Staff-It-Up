# Käyttöohje

Sovellus on käytettävissä osoitteessa (https://staffitup.herokuapp.com/). 

Sovelullusta voi käyttää myös paikallisesti osoitteessa (http://localhost:5000) asennuksen ja käynnistyksen jälkeen (ks. [asennusohje](https://github.com/picada/Staff-It-Up/blob/master/documentation/installation_guide.md)

## Päänäkymä

Avatessaan sovelluksen osoitteessa (https://staffitup.herokuapp.com/) käyttäjä saapuu palvelun pääsivulle, jonka navigaatiopalkin kautta
käyttäjä voi joko luoda uuden työntekijätunnuksen tai kirjautua sisään olemassaolevalla työntekijä- tai ylläpitäjätunnuksella.

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/front.jpg">

## Rekisteröityminen

Käyttäjä voi halutessaan luoda itselleen uuden työntekijätunnuksen navigaatiopalkin "Luo uusi käyttäjä" -linkin kautta. 

Käyttäjän tulee syöttää lomakkeeseen pyydetyt tiedot (nimi, käyttäjätunnus, salasana, sähköposti, puhelinnumero), jonka jälkeen uusi käyttäjä tallennetaan tietokantaan mikäli lomake on täytetty oikein ja
käyttäjätunnus ei ole jo varattu. Käyttäjätunnuksen luomisen jälkeen sovellus siirtyy automaattisesti kirjautumissivulle

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/newuser.jpg">

## Kirjautuminen

Käyttäjä voi kirjautua sisään joko työnantaja- tai työntekijätunnuksella siitymällä navigaatiopalkista haluamaansa kirjautumisnäkymään.

Sovellukseen on valmiiksi määritelty kaksi eri käyttäjää, jotka on luotu testausvaihetta varten:

| Käyttäjätunnus | Salasana  |  Rooli  |
| :-----| :-----|:-----|
| admin | admin | admin |
| test | testtest | user |

## Työntekijäkäyttäjän toiminnot

### Etusivu

Kirjauduttuaan sisään työntekijänä käyttäjä saapuu etusivulle, jossa on kootusti listattuna kaikki tulevat tapahtumat, joilta puuttuu tällä hetkellä henkilökuntaa.
Käyttäjä pääsee tarkastelemaan tarkempia tapahtumatietoja klikkaamalla haluaamansa tapahtumaa listasta

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/userindex.jpg">

### Tapahtumatietojen ja työvuorojen tarkastelu

Tietyn tapahtuman linkkiä klikkaamalla sovellus aukeaa näkymään, jossa käyttäjä voi tarkastella tapahtuman tarkempia tietoja sekä erilaisia työvuoroja, 
joita tapahtumaan on liitetty. (Saman näkymän kautta työntekijä voi myös ilmoittautua haluamiinsa työvuoroihinsa, mutta toiminnallisuuden hionta on vielä kesken). 

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/usereventview.jpg">

### Toistaiseksi puuttuvat toiminnallisuudet

Tässä vaiheessa suurin osa työntekijäkäyttäjään liittyvistä toiminnallisuuksista on vielä työn alla.

## Ylläpitäjäkäyttäjän toiminnot

### Etusivu

Sisäänkirjautumisen jälkeen ylläpitäjä saapuu etusivulle, jossa on kootusti listattuna kaikki tulevat tapahtumat, joilta puuttuu tällä hetkellä henkilökuntaa.
Käyttäjä pääsee tarkastelemaan tarkempia tapahtumatietoja klikkaamalla haluaamansa tapahtumaa listasta

### Tapahtumatien listaus

Navigaatiopalin Listaa tapahtumat -linkin kautta käyttäjä pääsee tarkastelemaan listaa kaikista tietokantaan syötetyistä tapahtumista. Saman näkymän kautta käyttäjä voi myös poistaa 
tapahtumia, merkata tapahtumia täydeksi tai avata uudestaan hakuun sekä siirtyä tarkastelemaan yksittäisten tapahtuminen tarkempia tietoja tapahtuman nimeä klikkaamalla.

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/listevents.jpg">

### Tapahtumatietojen ja työtehtävien tarkastelu

Tiettyä tapahtumaa klikkaamalla sovellus aukeaa näkymään, jossa käyttäjä voi tarkastella tapahtuman tarkempia tietoja. Käyttäjä voi myös luoda uusia 
tapahtumaan liittyviä työvuoroja täyttämällä sivun alareunasta löytyvän lomakkeen. 
(Saman näkymän kautta ylläpitäjä voi myös tulevaisuudessa vahvistaa henkilökuntaa työvuoroihin, mutta toiminnallisuuden hionta on vielä kesken). 

<img src="https://github.com/picada/documentation/manualimages/admineventview.jpg">

### Uuden tapahtuman luominen

Ylläpitäjä voi luoda tietokantaan uuden tapahtuman navigaatiopalkin Lisää uusi tapahtuma -linkin kautta. Lomakkeessa kysytään tiettyjä tapahtuman perustietoja, kuten tapahtuman nimi/tyyppi, päivämäärä, 
sekä alustava henkilömäärä. Lisätietoja-kenttä ei ole pakollinen, mutta usein erittäin hyödyllinen.

Päivämäärän valitsemisen pitäisi oletusarvoisesti onnistua kalenterinäkymän kautta, mutta mikäli selain ei jostain syystä tue tätä toiminnallisuutta tulee päivämäärä syöttää 
muodossa VVVV-kk-pp. 

<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/newevent.jpg">

### Toistaiseksi puuttuvat toiminnallisuudet

Tässä vaiheessa suuri osa työntekijäkäyttäjään liittyvistä toiminnallisuuksista on vielä työn alla.

## Ulsokirjautuminen

Käyttäjä voi kirjautua ulos oikean yläkulman Logout-painikkeesta
