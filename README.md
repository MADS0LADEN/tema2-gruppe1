# tema2-gruppe1
Rover

## TODO

### Control Protocol

Der skal laves en ny løsning som gør at vi kan styre begge motor i samme pakke

Der sendes beskeder til roveren via UDP på denne måde:
- "STOP"                    = "0"
- "Ligeud"                  = "100 100"
- "Bagud"                   = "-100 -100"
- "Ligeud lidt til højre"   = "100 80"
- "Ligeud lidt til venstre" = "80 100"
Første tal er venstre og andet er højre hjul

### Frontend / Client
Hjemmesiden til at sende styre input til roveren
##### Knapper
Fedest hvis vi kan få tastatur knapperne til at virke.
Ellers kan vi lave joysticks på hjemmesiden som man kunne styre fra en touchskærm
##### CLI Client
Hvis det er nemmere kan vi også se om vi kan lave et program der køres i console til at tage imod input fra tastaturet

### Backend / Server
Dette er koden som skal styre rover samt modtage kommandoer fra hjemmesiden man bruger som controller
##### Netværk
Finde en løsning til at modtage beskeder fra klienten som kan konverteres til styring af rover
##### Styring af motor
Finde en optimal løsning til at få roveren til at gøre som vi beder den om (køre ligeud hvis vi vil det)
