# Käyttöohje

Sovellus on käytettävissä osoitteessa (https://staffitup.herokuapp.com/). 

Sovellusta voi käyttää myös paikallisesti osoitteessa (http://localhost:5000) asennuksen ja käynnistyksen jälkeen (ks. [asennusohje](https://github.com/picada/Staff-It-Up/blob/master/documentation/installation_guide.md))

## Päänäkymä

Avatessaan sovelluksen osoitteessa (https://staffitup.herokuapp.com/) käyttäjä saapuu palvelun kirjautumissivulle.

## Rekisteröityminen

Käyttäjä voi halutessaan luoda itselleen uuden työntekijätunnuksen navigaatiopalkin "Luo uusi käyttäjä" -linkin kautta. 

Käyttäjän tulee syöttää lomakkeeseen pyydetyt tiedot (nimi, käyttäjätunnus, salasana, sähköposti, puhelinnumero), jonka jälkeen uusi käyttäjä tallennetaan tietokantaan mikäli lomake on täytetty oikein ja
käyttäjätunnus ei ole jo varattu. Käyttäjätunnuksen luomisen jälkeen sovellus siirtyy automaattisesti kirjautumissivulle


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/newuser.jpg">

## Kirjautuminen

Käyttäjä voi kirjautua sisään joko työnantaja- tai työntekijätunnuksella, sovellus ohjaa käyttäjän automaattisesti roolin mukaiseen näkymään.

Sovellukseen on valmiiksi määritelty kaksi eri käyttäjää, jotka on luotu testausvaihetta varten:

| Käyttäjätunnus | Salasana  |  Rooli  |
| :-----| :-----|:-----|
| admin | admin | admin |
| test | testtest | user |

## Työntekijäkäyttäjän toiminnot

### Etusivu

Kirjauduttuaan sisään työntekijänä käyttäjä saapuu etusivulle, joka tarjoaa seuraavat ajankohtaiset tiedot:
* Seuraavan kuukauden aikana toteutuvat tapahtumat, joihin tarvitaan henkilökuntaa
* Omat seuraavat vahvistetut työvuorot (max 5)

Käyttäjä pääsee tarkastelemaan tarkempia tapahtumatietoja klikkaamalla haluaamansa tapahtumaa listasta


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/userindex.jpg">


### Tapahtumatietojen ja työvuorojen tarkastelu

Tietyn tapahtuman linkkiä klikkaamalla sovellus aukeaa näkymään, jossa käyttäjä voi tarkastella tapahtuman tarkempia tietoja sekä erilaisia työvuoroja, joita tapahtumaan on liitetty. Saman näkymän kautta työntekijä voi myös ilmoittautua haluamiinsa työvuoroihin ja perua vahvistamattomia ilmoittautumisiaan.


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/usereventview.jpg">


### Omien tulevien ja menneiden työvuorojen sekä ilmoittautumisten listaus

Navigaatiopalkin työvuorot-valikon kautta käyttäjä voi siirtyä tarkastelemaan omia tulevia tai menneitä työvuorojaan tai vahvistamattomia ilmoittautumisiaan. 

### Tapahtumien listaus

Käyttäjä voi listata tulevat, työvoimaa tarvitsevat tapahtumat Listaa tapahtumat -linkin kautta.

### Omien tietojen muokkaus

Käyttäjä voi muokata kaikkia muita tietojaan paitsi käyttäjänimeä "Omien tietojen muokkaus" -linkin takaa aukeavan lomakkeen kautta. 

## Ylläpitäjäkäyttäjän toiminnot

### Etusivu

Kirjauduttuaan sisään työntekijänä käyttäjä saapuu etusivulle, joka tarjoaa seuraavat ajankohtaiset tiedot:
* Seuraavan kuukauden aikana toteutuvat tapahtumat, joihin tarvitaan henkilökuntaa
* Tapahtumat, joissa on vahvistamattomia ilmoittautumisia ja kuinka monta

### Tapahtumatien listaus

Navigaatiopalin Listaa tapahtumat -valikon kautta käyttäjä pääsee tarkastelemaan listaa tietokannan tapahtumista. Käyttäjä voi listata joko vain tulevat tapahtumat joihin tarvitaan henkilökuntaa, kaikki tulevat tapahtumat tai kaikki menneet tapahtumat. Saman näkymän kautta käyttäjä voi myös poistaa tapahtumia, merkata tapahtumia täydeksi tai avata uudestaan hakuun sekä siirtyä tarkastelemaan yksittäisten tapahtuminen tarkempia tietoja tapahtuman nimeä klikkaamalla.


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/listevents admin.jpg">


### Tapahtumatietojen ja työtehtävien tarkastelu

Tiettyä tapahtumaa klikkaamalla sovellus aukeaa näkymään, jossa käyttäjä voi tarkastella tapahtuman tarkempia tietoja. Käyttäjä voi myös luoda uusia tapahtumaan liittyviä työvuoroja täyttämällä sivun alareunasta löytyvän lomakkeen. Saman näkymän kautta käyttäjä pääsee tarkastelemaan tapahtumaan liittyviä työvuoroja ja ilmoittautumisia.

Käyttäjä voi myös muokata tapahtuman henkilömäärää ja info-kentää "Muokkaa tapahtuman tietoja" -linkin kautta.


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/admineventview.jpg">


### Uuden tapahtuman luominen

Ylläpitäjä voi luoda tietokantaan uuden tapahtuman navigaatiopalkin Lisää uusi tapahtuma -linkin kautta. Lomakkeessa kysytään tiettyjä tapahtuman perustietoja, kuten tapahtuman nimi/tyyppi, päivämäärä, 
sekä alustava henkilömäärä. Lisätietoja-kenttä ei ole pakollinen, mutta usein erittäin hyödyllinen.

Päivämäärän valitsemisen pitäisi oletusarvoisesti onnistua kalenterinäkymän kautta, mutta mikäli selain ei jostain syystä tue tätä toiminnallisuutta tulee päivämäärä syöttää 
muodossa VVVV-kk-pp. 


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/newevent.jpg">


### Työvuorojen ja ilmoittautumisten tarkastelu

Käyttäjä pääsee joko tapahtumalistaukseta tai tapahtuman tiedoista näkymään, jossa käyttäjä voi tarkastella vahvistettua henkilökuntaa, perua vahvistettuja vuoroja sekä vahvistaa työntekijöiden ilmoittauutmisia.


<img src="https://github.com/picada/Staff-It-Up/blob/master/documentation/manualimages/registrationview admin.jpg">


### Käyttäjien hallinnointi

Ylläpitäjä voi luoda uusia työntekijä- tai ylläpitäjäkäyttäjiä Hallinnoi käyttäjiä -valikon "Luo uusi käyttäjä" -linkin kautta. Käyttäjä voi myös tarkastella kaikkia käyttäjiä sekä muokata käyttäjätietoja "Listaa käyttäjät" -näkymästä

## Ulsokirjautuminen

Käyttäjä voi kirjautua ulos oikean yläkulman Logout-painikkeesta
