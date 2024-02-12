def romanToInt(s) -> int:
      values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
      strLen = len(s)
      total = 0
      while len(s) > 0:
            if s[-2:] in values:
                  total += values[s[-2:]]
                  s = s[0:-2]
            else:
                  total += values[s[-1]]
                  s = s[0:-1]
            print(s)
      print(total)

t = 'MCMXCI'
s = 'IV'
romanToInt(t)