#Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. 

def pressure(KPA):
    PSI = KPA / 6.89475729
    print("Pressure in PSI: %.2f psi" % PSI)
    MMHG = KPA * (760 / 101.325)
    print("Pressure in MMHG: %.2f mmhg" % MMHG)
    ATM = KPA / 101.325
    print("Pressure in ATM: %.2f atm" % ATM)
pressure(12.35)

