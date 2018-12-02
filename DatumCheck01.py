import datetime

def DatumCheck(inputDate):  # routine DatumCheck definieren
    isValidDate = True

    for char in inputDate: # controleren welk format wordt gebruikt
        if char == "/":
            SplitChar = '/'
            break
        elif char == "-":
            SplitChar = '-'
            break

    try:
        dag, maand, jaar = inputDate.split(SplitChar) # de waarde voor dag, maand en jaar vullen
    except ValueError:      # als dit niet lukt dan execption
        isValidDate = False

    if (isValidDate):
        try:
            datetime.datetime(int(jaar), int(maand), int(dag))  # De waarden voor dag, maand, jaar in date formate laden
        except ValueError:      #als dit niet lukt dan is het geen geldige datum. Exception
            isValidDate = False
    if(isValidDate):
        print("Geldige datum")
    else:
        print("Mooi niet. Ongeldig")


inputDate = input('Geef datum: ') # om de datum vragen
DatumCheck(inputDate) # DatumCheck routine aanropen

