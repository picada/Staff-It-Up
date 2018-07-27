# Staff It Up

Tietokantasovellus-kurssin harjoitustyönä toteutettava sovellus. 

[Heroku](http://staffitup.herokuapp.com)

## Kuvaus

Tarkoituksena on luoda keikkatyöalusta tapahtumatoimistolle. Sovelluksessa on kaksi eri käyttäjäroolia, työnantaja ja työntekijä. Sekä toiminnallisuudet että sovellusnäkymä riippuvat käyttäjäroolista, ja työnantajalla on laajemmat oikeudet tietokannan hallintaan.

Työnantajapuolella käyttäjä voi mm. lisätä uusia tapahtumia ja niihin liittyviä työvuoroja, vahvistaa työvuoroja ilmoittautumisten perusteella sekä tarkastella eri tapahtumiin varattua henkilökuntaa. Lisäksi sovellus toimii henkilökunnan yhteystietorekisterinä. Myös uusien työnantajakäyttäjien luominen tapahtuu tätä kautta, uutta työnantajatunnusta ei siis voi luoda itse. 

Kuka tahansa voi puolestaan rekisteröityä sovelluksessa työntekijäksi, ja käyttäjätunnuksen luonnin yhteydessä työntekijä syöttää tietokantaan myös yhteystietonsa. Tunnuksen luomisen jälkeen työntekijä voi tarkastella työnantajan ilmoittamia tapahtumia sekä työvuoroja ja ilmoittautua käytettävissä olevaksi haluamiinsa vuoroihin. Työntekijä voi myös tarkastella omia ilmoittautumisiaan sekä vahvistettuja työvuoroja.

Työvuorot liittyvät aina johonkin tiettyyn tapahtumaan, ja jokaiselle tapahtumalla on päivämäärä, suunta-antavat kellonajat, arvio tapahtuman henkilömäärästä sekä nimi/kuvaus. Jokaista tapahtumaa kohden voi olla saatavilla useampi työvuoro, joiden kesto ja rooli (esim. keikkavastaava / rastiohjaaja / juhla-avustaja) voivat vaihdella. 

Sovellus pohjautuu toimintamalliin jota noudatetaan omassa työpaikassani, tällä hetkellä kaikki kuitenkin hoidetaan pääasiassa sähköpostin välityksellä.

### Toimintoja

Työnantaja:
* Kirjautuminen
* Uusien työntekijä- ja työnantajakäyttäjien lisääminen työnantajanäkymästä
* Käyttäjien poistaminen
* Uuden tapahtuman luominen
* Uuden työvuoron luominen
* Työvuorojen vahvistaminen ilmoittautumisten perusteella
* Varatun henkilökunnan tarkastelu tapahtumakohtaisesti
* Yhteystietojen tarkastelu

Työntekijä:
* Uuden käyttäjän luominen
* Kirjautuminen
* Omien tietojen muokkaus
* Saatavilla olevien työvuorojen haku ja listaus 
* Ilmoittautuminen tiettyyn työvuoroon
* Omien ilmoittautumisten ja vahvistettujen työvuorojen listaus
