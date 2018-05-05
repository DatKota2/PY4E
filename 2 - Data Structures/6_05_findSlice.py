text = "X-DSPAM-Confidence:    0.8475"
numStart = text.find('.')
fnString = text[numStart:]
fnFloat = float(fnString)
print(fnFloat)
