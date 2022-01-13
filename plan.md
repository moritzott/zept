# Zeitrechner für Projekte - ZEPT

## Ein Arbeitszeitberechner

Primär eine Anwendung für mich selber, um zu schauen,
wie viel Zeit ich für dieses oder jenes Projekt investiert habe.
Nach und nach soll eine Anwendung entstehen,
die die Startzeit und Endzeit in eine Datenbank
überträgt und die bisherige Zeit, die
ich für ein Projekt
aufgewendet habe, mir ausgeben kann.
Schön wäre noch, dass man verschiedene Projekte
anlegen kann, bei dem eine Zeitmessung auf
Knopfdruck losgeht, bis man selbst wieder *Stop* drückt.
Vielleicht wäre auch eine graphische Abbildung schön,
bei der man in Säulendiagrammen die Projekte und
die jeweilige Summe der Arbeitszeiten auf der x-Achse anschauen kann.

## Grober Plan

### Version 1.0.0
* Sprache: Python mit tkinter
* man kann auf Start drücken -> setzt Zeitstempel
* man drückt auf Stop: Differenz wird ausgerechnet in Sekunden

### v1.1.0

* Zeitpunkte und Differenzen werden in einer SQLite3-Datenbank gespeichert


### v1.2.0

* man kann verschiedene Projekte anlegen
* für jedes Projekt gibt es eine Tabelle in 
der Datenbank mit den Start und Endzeiten (Datum)
plus die Differenz.

### v1.3.0
* man kann sich anzeigen lassen, wie lange man
schon an einem Projekt gearbeitet hat