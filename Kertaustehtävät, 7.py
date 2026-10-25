sanat = ["omena", "banaani", "auto", "tietokone", "koira"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli viiden kirjaimen sanoja on", maara)