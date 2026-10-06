# Matrislösare jämförelse

Detta projekt är skapat som ett gymnasiearbete. Syftet med projektet är att jämföra olika metoder för att lösa linjära ekvationssystem och analysera hur många aritmetiska operationer varje metod kräver.

## Projektbeskrivning

Programmet genererar slumpmässiga inverterbara matriser och löser motsvarande ekvationssystem med tre olika metoder:

- Gausselimination
- Inversmatris-metoden
- Cramers regel

Skriptet räknar antalet aritmetiska operationer för varje metod och visualiserar resultaten i en graf. Det finns även en knapp i diagrammet som gör att användaren kan växla mellan logaritmisk och linjär skala.

## Varför är detta projekt intressant?

Detta projekt visar hur olika algoritmer kan lösa samma problem men med väldigt olika beräkningskostnader. Det är användbart för att förstå:

- algoritmisk effektivitet
- numeriska metoder
- komplexitet i lösning av linjära ekvationssystem
- hur matematik och programmering hänger ihop

## Funktioner

- Genererar slumpmässiga matriser med olika storlekar
- Kontrollerar att varje matris är inverterbar
- Räknar antalet operationer för varje lösningsmetod
- Plotter jämförelsen i ett diagram
- Gör det möjligt att växla mellan logaritmisk och linjär skala

## Teknologier som används

- Python
- NumPy
- Matplotlib

## Installation

Se till att Python är installerat och kör sedan:

```bash
pip install numpy matplotlib
