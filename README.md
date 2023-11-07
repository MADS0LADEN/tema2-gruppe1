# tema2-gruppe1
Rover

## TODO

### Control Protocol
Der sendes beskeder til roveren via UDP på denne måde:
- Fremad 100% = "forward 100"
- Bagud 80% = "backward 80"
- Højre 50% = "right 50" 
- Venstre 25% = "left 25" 

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
