python# Excel til Parquet

Dette prosjektet inneholder `TestParquet.py`, et Python-program som leser en Excel-fil, validerer innholdet og skriver resultatet til en Parquet-fil.

## Forutsetninger

- Python 3.10 eller nyere
- PowerShell i Windows

Kontroller at Python er tilgjengelig:

```powershell
python --version
```

## Opprett virtuelt miljø

Åpne prosjektmappen i PowerShell og opprett et virtuelt miljø med navnet `.venv`:

```powershell
cd "C:\Users\Ole Tom Vårdal\Lokal-struktr\Code-Python"
python -m venv .venv
```

Aktiver miljøet:

```powershell
.\.venv\Scripts\Activate.ps1
```

Når miljøet er aktivt, starter ledeteksten vanligvis med `(.venv)`.

Hvis PowerShell blokkerer aktiveringen, kjør denne kommandoen én gang for din bruker og prøv på nytt:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Installer avhengigheter

Oppgrader først `pip`, og installer deretter pakkene programmet trenger:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas pyarrow openpyxl
```

- `pandas` leser og behandler tabellen.
- `pyarrow` skriver og leser Parquet-formatet.
- `openpyxl` brukes av pandas til å lese `.xlsx`-filer.

## Kjør programmet

Programmet tar imot to argumenter: Excel-filen som skal leses, og navnet på Parquet-filen som skal opprettes.

```powershell
python TestParquet.py input.xlsx output.parquet
```

Eksempel:

```powershell
python TestParquet.py data.xlsx data.parquet
```

Programmet skriver status i terminalen og viser de fem første radene fra den ferdige Parquet-filen som kontroll.

## I VS Code

1. Åpne Command Palette med `Ctrl+Shift+P`.
2. Velg `Python: Select Interpreter`.
3. Velg tolken som ligger i `.venv`.
4. Åpne en ny terminal. VS Code skal da aktivere miljøet automatisk.

## Avslutt miljøet

Når du er ferdig i terminalen, avslutter du det virtuelle miljøet med:

```powershell
deactivate
```
