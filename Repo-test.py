filnavn = "hei.txt"

with open(filnavn, "w", encoding="utf-8") as fil:
	fil.write("hei du")

print(f"Skrev hei til {filnavn}")
