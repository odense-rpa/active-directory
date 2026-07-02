# active-directory

En simpel Python-klient til at søge i Active Directory via LDAP, bygget ovenpå `ldap3`.

> Denne klient er ikke officielt støttet eller godkendt af Microsoft. Brug på eget ansvar.

## Installation

```bash
uv add git+https://github.com/odense-rpa/active-directory
```

## Forudsætninger

- Python ≥ 3.13
- Adgang til et Active Directory-miljø via LDAP

## Brug

Opret en `ActiveDirectoryClient` med server-URL, port, base DN, brugernavn og adgangskode. Klienten binder automatisk til LDAP-serveren ved instantiering.

```python
from active_directory import ActiveDirectoryClient

client = ActiveDirectoryClient(
    server="ldap.example.com",
    port=389,
    base_dn="DC=example,DC=com",
    username="CN=serviceaccount,DC=example,DC=com",
    password="hemmeligt",
)

resultater = client.søg(
    ldap_filter="(sAMAccountName=jdoe)",
    attributes=["cn", "mail", "employeeID"],
)
```

`søg()` tager et LDAP-filter og en liste af attributter og returnerer de matchende AD-objekter.

## Afhængigheder

| Pakke | Formål |
|---|---|
| `ldap3` | LDAP-klient til at forbinde og forespørge Active Directory |

## GDPR og sikkerhed

Søgeresultater kan indeholde personoplysninger afhængigt af de LDAP-attributter, der forespørges (f.eks. navne, e-mailadresser, medarbejder-ID'er). Håndter returnerede data i overensstemmelse med organisationens databehandlingspolitik. Brugernavn og adgangskode til AD-kontoen bør opbevares sikkert og aldrig gemmes i koden.

## Licens

MIT
