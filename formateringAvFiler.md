## Info
- Dette er en gjennomgang av hvordan man skal skrive inn data for ulike formler  
- Dataene leses og tolkes automatisk av andre filer (om skrevet inn riktig)  
- Man kan legge sammen flere formler under samme fil  
- Hver fil som brukes må inkluderes i HTML filen  
- Funksjoner trenger ikke være i samme fil, siden de er globale for HTML DOM, men der blir mer oversiktlig om de er  
- Pytagoras' læresetning blir brukt som eksempel for å demonstrere hvordan dette burde gjøres  
- Følg stegene nedenfor for å riktig skrive inn dataene

----------------------------------------------------------------------------

## Finn en formel
Det første du må gjøre er å finne en formel som du vil legge til.  
Eks:
> Pytagoras' læresetning

## Bestem et rotnavn
Når du bestemmer et rotnavn er det viktig at dette rotnavnet ikke allerde eksisterer.  
Rotnavnet har noen kriterier:
- Må være mulig navn på en JavaScript funksjon
- Må være unikt
- Burde ha en tilknyttning til selve formelen

Eks:
> pytagoras

## Bestem formelen
Det kan være lurt å ha det klart for seg hvordan formelen er bygd opp.  
Ved å ha formlen forran seg er det lettere å fylle inn dataene.  
Eks:
> a^2 + b^2 = c^2

Eller for å vise hva som er hva litt bedre:
> h^2 = k1^2 + k2^2

## Leg til kommentarer for formlen
Det kan være lurt å legge til noen kommentarer over formel- og datafunksjonene.  
De burde innehole blant annet navn på formelen og selve formlen.

Det finnes 2 former for kommentarer i JavaScript:
- Enkeltlinjekommentar, innledet med dobbel skråstrek (//), går over en linje og dekker hele linjen
- Blokkommentar, innledet med en skråstrek fulgt av en asterisk (/\*), og avsluttet med en asterisk fulgt av en skråstrek (/\*), starter fra innledning og ender ved avsluttning, kan gå over flere linjer

Som du vil se i eksemplene så er enkeltlinjekommentarene ofte lettere å lese.  
Eks:
```
// Pytagoras' læresetning
/* h^2 = k1^2 + k2^2 */
```

## Bestem variablene i formelen
Det å bestemme og å definere variablene blir en viktig del av innskrivingen slik at dataen skal bli lest riktig.  
Bare lag degselv en liste over variablene, det trenger ikke være kommentert i filen.  
Eks:
> h, k1, k2

## Utregningsfunksjonene
Navnet på funksjonen starter med rotnavnet som du bestemte deg for å bruke tidligere, fulgt av understrek (_) og deretter navnet på variablen som settes hensyn på, for eksempel:
> pytagoras_h

Funksjonen trenger også argumenter, argumentene er variablene som defineres når du bruker formlen, altså informasjonen du oppgir i parantesene som følger funksjonsnavnet.  
Argumentene må inneholde alle de andre variablene som urtregningen skal bruke, gjerne opprit i rekkefølge ettersom hvor de er plassert i listen med variabler for funksjonen.  
Argumentene kan ikke bare plasseres rett inn i parantesene, men må legges inn i en array.
> ([k1, k2])

Deretter kan du fylle inn formlen med utregningen.  
Den letteste måten å gjøre dette på er å bare returnere selve utregningen.  
Da slipper man å skrive noe som "svar = utregning":
```
return (k1**2 + k2**2)
```

Den første funksjonen for pytagoras vil bli seende slik ut:
```
function pytagoras_h ([k1, k2]) {
    return (k1**2 + k2**2)**0.5
}
```

Deretter gjenstår det å skrive inn funskonene for utregning av de andre omformuleringene av formelen med samme metode.

# Datafunksjonen

## Generelt
Datafunksjonen er den funsjonen som inneholder all dataen som leses, tolkes og brukes til å vise formlene.  
Den er en funksjon som returnerer et objekt som inneholder ulike nøkler med gitte verdier.

Navnet på formelen må være "data_" etterfult av rotnavnet som ble bestemt tidligere.  
Eks:
> data_pytagoras

funksjonen ser nå slik ut:
```
function data_pytagoras () {}
```

Inne i klammeparantesene kan vi innlede med "return".  
Det vi vil returnere er et objekt med all dataen.  
Et objekt defineres med klammeparanteser:
```
return {}
```

## Enkel data
Inne i klammeparantesene kan vi begynne å fylle inn data.  
Det er noen av dataene vi allerede har definert, vi må bare fylle de inn:
- Navn på formel, dette er navnet som vises over formelen i formelseksjonen av nettsiden:
- Rotnavnet brukt for funksjonene

Funksjonen blir slik:
```
function data_pytagoras () {
    return {
        navn:"Pytagoras' læresetning",
        rotnavn:"pytagoras"
}
```

## Beskrivelse
Formelen får tillagt en beskrivelse så folk bedre kan forstå den.  
Beskrivelsen kan inneholde grunner til at vi bruker kakurat denne formelen og kanskje noe om hvordan eller hvorfor den virker.  
Dette putter vi inn i objektet med "beskrivelse" som nøkkel:
```
berskrivelse:`Formel beskrivelse.`
```
Grunnen til at vi bruker backtick istedet for anførselstegn er at teksten da kan splittes opp på flere linjer og blir dermed lettere å lese i filen.  
Når det er en ny linje blir det behandlet akkurat som et mellomrom.  
En fin regel er at man lager en ny linje etter hvert punktum.  
Bruk slik:
```
beskrivelse:`Dette er bare et eksempel.
Ikke skriv akkurat dette i datafunksjonen.`
```

## Avanserte verdier
Nå gjenstår de mer tekniske verdiene.  
Det er tre ulike nøkler som mangler:
- variabler
- display
- argumenter

## Variabel definisjoner
Det er best å starte me variabler, siden de to andre behøver definerte variabler.  
Variablene legges inn under nøkkelen "variabler":
```
variabler:{}
```
Her bruker vi enda et objekt, siden det skal være flere variabler.  
Inne i det nye objektet lager vi nøkkelnavn for alle de ulike variablene, disse navnene blir brukt som variabel-ID-er.  
Verdiene til variablene er det som vises i plass av variablen.  
Som eksempel ville variablen h i pytagoras bare vises som h, og dermed:
```
h:"h"
```

Sånn innlastingsfunksjonen er lagd, gir den mulighet for å bruke subscript og superscript:
- Supscript; teksten vises under linjen, brukt for eksempel for å nummerere variabler med samme navn.
- Superscript; teksten vises over linjen, brukt for eksempel i vising av potenser.

Disse er 'elementer' og settes inn i mindre enn og større enn (<>):
> <\\sub tekst>  
> <\\sup tekst>

Det finnes også en tredje variant; var.  
Denne brukes når man skal vise variabler.  
Om man skriver "<\\var variabel-ID>" vil det referere til variablen og teksten som vises hentes fra tekst verdien til variablen i verditabellen til variabel nøkkelen (Den du skriver nå).  
Det er ikke noe bruk for variabel elementet enda, men det må bli brukt senere.

For pytagoras vil variabellista bli slik:
```
variabler: {
    h:"h",
    k1:"k<sub 1>",
    k2:"k<sub 2>"
}
```
## Formelvisning (display)
Display nøkkelen er det som faktisk sier hva formelen skal vise.  
Den er bygd opp på samme måte som variabel nøkkelen, ved at det er et objekt som er verdien.  
Inne i objektet skrives de ulike variablene som nøkler, når dataen hentes blir nøkklene brukt for å vise til hvilken av verdiene vi prøver å finne.  
I Pytagoras' læresetning, om vi skal løse for hypotenusen (h), vil nøkklen være variabel-ID-en til hypotenusen, altså 'h'.  
Standardverdien, den som vises når brukeren først klikken inn på formelen, er displayverdien som er definert øverst.  

Verdien til de ulike nøkklene blir selve utregningen, men med bruk av sub, sup og var elementene.  
Om du vil bruke en variabel skriver du "<\\var variabel-ID>".  
Variablene vil automatisk byttes ut med inndatafelt hvor så brukeren kan skrive inn verdier der det trengs, ellers viser den verdien som variablen-ID-en er tillagt.

Noe som skal opphøyest legges inn med sup element via "<\\sup verdi>".  
Verdien kan entern være ett nytt element eller bare vanlig tekst.  
Det samme gjelder sub variablen om den skal brukes.

Om vi følger denne oppskriften for Pytagoras' læresetning vil vi få dette om vi løser for h:
```
h:"√(<var k1><sup 2> + <var k2><sup 2>)"
```
Dette gjøres for alle utregningene.

## Argumenter matet til utregningsfunksjon
Det siste punktet er "argumenter".  
Dette punktet er ganske rett frem;  
Samme oppbygging som de to forrige punktene:
```
argumenter:{
    variabel-ID:"verdi"
}
```
Variabel-ID-en viser igjen til hvilken verdi som løses for.
Dette vil kallefunksjonen ved navn:
> rotnavn_variabel-ID

Verdiene til nøkklene er variablene som skal mates til funksjonen.  
De må oppgis med riktig navn og riktig rekkefølge.  
Om du ser tilbake på utregningsfunksjonene du laget, kan du ta en titt på argumentene:
```
function rotnavn_variabel-ID ([argumenter]) {utregning}
```
Hvis du har brukt variabel-ID-er som argumenter er det lett å bare kopiere de ned til verdiene i argumentlista.  
Her er det veldig nøye å få riktig rekkefølge på variablene.  
De skal ikke splittes opp med komma, bare et enkelt mellomrom.  
Eks:
```
function pytagoras_h ([k1, k2]) {utregning}
```
Dermed:
```
h:"k1 k2"
```

# Dobbelskjekking
Det kan være lurt å gå over alle verdiene for å passe på at alt stemmer overens.  
Det er fort å gjøre småfeil, noe som også fører til at programmet ikke vil gjøre riktig ting og kanskje feile.  
Derfor er det viktig å dobbel- og kanskje trippelskjekke alt før det blir tatt i bruk.

# Gratulerer
Du har laget en ny formel, det gjenstår fortsatt å legge den til i resten av systemet, men den virker ihvertfall!

# Eksempel
Her er et eksempel av hvordan filen nå burde se ut.  
Som eksempel er det brukt Pytagoras' læresetning:
```
// Pytagoras' læresetning
// h^2 = k1^2 + k2^2
function pytagoras_h ([k1, k2]) {
    return (k1\*\*2 + k2\*\*2)\*\*0.5
}
function pytagoras_k1 ([k2, h]) {
    return (h\*\*2 - k2\*\*2)\*\*0.5
}
function pytagoras_k2 ([k1, h]) {
    return (h\*\*2 - k1\*\*2)\*\*0.5
}
function data_pytagoras () {
    return {
        navn:"Pytagoras' læresetning",
        rotnavn:"pytagoras",
        beskrivelse:`Formel beskrivelse.`,
        variabler:{
            h:"h",
            k1:"k<sub 1>",
            k2:"k<sub 2>"
        },
        display:{
            h:"√(<var k1><sup 2> + <var k2><sup 2>)",
            k1:"√(<var h><sup 2> - <var k2><sup 2>)",
            k2:"√(<var h><sup 2> - <var k1><sup 2>)"
        },
        argumenter:{
            h:"k1 k2",
            k1:"k2 h",
            k2:"k1 h"
        }
    }
}
```