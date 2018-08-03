# Staff It Up

Tietokantasovellus-kurssin harjoitustyönä toteutettava sovellus. 

[Heroku](http://staffitup.herokuapp.com)

[Tietokantakaavio](https://github.com/picada/Staff-It-Up/blob/master/documentation/Tsoha%20tietokantakaavio.jpg)

[User Stories](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)

## Kuvaus

Tarkoituksena on luoda keikkatyöalusta tapahtumatoimistolle. Sovelluksessa on eri käyttäjärooleja (alussa ylläpitäjä eli yrityksen työvuoroista vastaava henkilö sekä peruskäyttäjä eli keikkatyöntekijä), ja samalla käyttäjällä voi olla useampi käyttäjärooli. Sekä toiminnallisuudet että sovellusnäkymä riippuvat käyttäjäroolista, ja ylläpitäjällä on laajemmat oikeudet tietokannan hallintaan.

Ylläpitopuolella käyttäjä voi mm. lisätä uusia tapahtumia ja niihin liittyviä työtehtäviä, vahvistaa työvuoroja ilmoittautumisten perusteella sekä tarkastella eri tapahtumiin varattua henkilökuntaa. Myös uusien työnantajakäyttäjien luominen tapahtuu tätä kautta, uutta ylläpitotunnusta ei siis voi luoda itse. Ylläpidon kautta pystyy lisäämään myös uusia peruskäyttäjiä, ja ylläpitäjät pystyvät muokkaamaan sekä tapahtuma-, työtehtävä- että käyttäjäkohtaisia tietoja. Lisäksi sovellus toimii ylläpitopuolella henkilökunnan yhteystietorekisterinä. 

Kuka tahansa voi puolestaan rekisteröityä sovelluksessa peruskäyttäjäksi eli keikkatyöntekijäksi, ja käyttäjätunnuksen luonnin yhteydessä työntekijä syöttää tietokantaan myös yhteystietonsa. Tunnuksen luomisen jälkeen työntekijä voi tarkastella työnantajan ilmoittamia tapahtumia sekä niihin liittyviä työtehtäviä, ilmoittautua käytettävissä olevaksi haluamiinsa tehtäviin sekä perua jo tehtyjä ilmoittautumisia. Työntekijä voi myös tarkastella omia ilmoittautumisiaan ja vahvistettuja työvuoroja sekä muokata omia yhteystietojaan.

Jokaisella tapahtumalla on nimi/kuvaus, päivämäärä, arvio tapahtuman henkilömäärästä, tieto siitä onko tapahtumaan jo varattu tarpeeksi henkilökuntaa sekä erillinen info-osio, josta voi käydä ilmi esim. tapahtumapaikka ja -aika. Jokaista tapahtumaa kohden voi olla saatavilla useampi työtehtävä, joiden kesto ja rooli (esim. keikkavastaava / rastiohjaaja / juhla-avustaja) voivat vaihdella. Useampi työntekijä voi ilmoittautua saatavilla olevaksi samaan työtehtävään, ja työtehtävien/vuorojen vahvistus tapahtuu ylläpitopuolella. Eri työvuorojen määrää per tapahtuma ei ole ennalta määritelty, vaan ylläpito voi vahvistaa tapahtumaan tarpeelliseksi katsomansa määrän henkilökuntaa.

Sovellus pohjautuu toimintamalliin jota noudatetaan omassa työpaikassani, tällä hetkellä kaikki kuitenkin hoidetaan pääasiassa sähköpostin välityksellä.

### Toimintoja

Työnantaja:
* Kirjautuminen
* Uusien työntekijä- ja työnantajakäyttäjien lisääminen työnantajanäkymästä
* Käyttäjien poistaminen
* Tapahtumien luominen, muokkaaminen ja poistaminen
* Tapahtumakohtaisten työtehtävien luominen, muokkaaminen ja poistaminen
* Työvuorojen vahvistaminen ilmoittautumisten perusteella
* Varatun henkilökunnan tarkastelu tapahtumakohtaisesti
* Yhteystietojen tarkastelu

Työntekijä:
* Uuden käyttäjän luominen
* Kirjautuminen
* Omien tietojen muokkaus
* Saatavilla olevien työvuorojen haku ja listaus 
* Ilmoittautuminen tiettyyn työtehtävään
* Ilmoittautumisen peruminen
* Omien ilmoittautumisten ja vahvistettujen työvuorojen listaus ja tarkastelu
