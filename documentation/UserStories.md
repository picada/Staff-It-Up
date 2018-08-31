# User Stories

Alla on kuvattuna sovellukselle olennaisia käyttäjätarinoita.

## Pääkäyttäjänä haluan...

* luoda uusia tapahtumia sekä lisätä jokaiseen tapahtumaan tarvittavat lisätiedot, jotta työntekijöiden on helppo hahmottaa millaisesta tilaisuudesta on kyse - toteutettu
* muokata jo luotujen tapahtumien tietoja, jos yksityiskohtiin tulee muutoksia - toteutettu
* lisätä jokaisen tapahtuman kohdalle saatavilla olevat työtehtävät ja niiden suuntaa-antavat kellonajat, jotta tapahtumiin saadaan varattua oikeanlaista henkilökuntaa - toteutettu
* Nähdä helposti yhdestä paikasta, mihin tuleviin, henkilökuntaa vaativiin tapahtumiin on olemassa vahvistamattomia ilmoittautumisia ja kuinka paljon
  ```
  SELECT event.id, event.type, event.date, COUNT(*) 
                    FROM event 
                    INNER JOIN assignment ON event.id = assignment.event_id 
                    INNER JOIN account_assignment ON account_assignment.assignment_id = assignment.id 
                    WHERE event.staffed = '0' 
                    AND event.date > CURRENT_DATE 
                    AND account_assignment.confirmed = '0' 
                    GROUP BY event.id 
                    HAVING COUNT(*) > 0 
                    ORDER BY event.date;
   ```
* nähdä ilmoittautumiset tapahtumakohtaisesti aikajärjestyksessä, jotta voin ottaa ilmoittautumisjärjestyksen halutessani huomioon vuoroja jakaessa - toteutettu
* vahvistaa tapahtumakohtaisia työvuoroja samasta näkymästä yhdellä klikkauksella - toteutettu
* pystyä merkitsemään tilaisuudet joissa on jo tapeeksi henkilökuntaa, jotta niihin ei tule enää turhia ilmoittautumisia - toteutettu 
* tarkastella vahvistettua henkilökuntaa tapahtumakohtaisesti, jotta näen helposti mihin tapahtumaan tarvitaan lisää työntekijöitä - toteutettu
  ```
  SELECT account.id, account.name, account.email, account.phone, assignment.id, assignment.role, assignment.starttime, assignment.endtime,       event.id 
                    FROM account, assignment, account_assignment, event 
                    WHERE event.id = :id 
                    AND assignment.event_id = event.id 
                    AND assignment.id = account_assignment.assignment_id 
                    AND account.id = account_assignment.account_id 
                    AND account_assignment.confirmed = '1' 
                    ORDER BY assignment.role;
  ```
* listata erikseen tapahtumat joihin tarvitaan vielä lisää työntekijöitä, jotta voin tarvittaessa huhuilla henkilökuntaa ko. tilaisuuksien osalta - toteutettu
* lisätä, muokata ja poistaa tapahtuma-, työtehtävä- ja käyttäjätietoja tarvittaessa, jotta tietokanta pysyy ajan tasalla - toteutettu

## Peruskäyttäjänä haluan...

* ilmoittautua niihin tapahtumiin ja työtehtäviin, jotka kulloinkin sopivat omiin aikatauluihin - toteutettu
* perua vahvistamattoman ilmoittautumisen, jos aikatauluihini tuleekin yllättäviä muutoksia - toteutettu
* tarkastella erikseen sekä menneitä että tulevia vavhvistettuja työvuoroja, jotta:  
  - nähdä, mihin tuleviin tapahtumiin minut on buukattu ja merkata ne kalenteriin 
  - voin tehdä työtunti-ilmoitukset helposti menneiden tapahtumien listan perusteella
  - Toteutettu - alla kysely joka toteuttaa ylemmän toiveen, alemman toiveen kysely lähes identtinen sillä erotuksella, että toisessa verrataan päivämäärää toisin päin:
  ```
SELECT assignment.role, assignment.starttime, assignment.endtime, event.type, event.date, event.id, assignment.id 
                    FROM account, assignment, account_assignment, event 
                    WHERE account.id = :id
                    AND account_assignment.account_id = account.id 
                    AND assignment.id = account_assignment.assignment_id 
                    AND event.id = assignment.event_id 
                    AND event.date > CURRENT_DATE 
                    AND account_assignment.confirmed = '1' 
                    ORDER BY event.date;
  ```
* muokata tarvittaessa omia yhteystietojani, jotta työnantaja saa minuun tarvittaessa yhteyttä - toteutettu
