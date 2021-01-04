cardPublicKey = 11562782
doorPublicKey = 18108497

def dayTwentyFive (card, door):
  cardPK = 1
  cardLoop = findCardLoop(card, cardPK)
  
  print("The encryption code is", findEncryptionKey(door, cardLoop))

def findCardLoop(card, cardPK):
  cardLoop = 0

  while cardPK != card:
    cardPK = (cardPK * 7) % 20201227
    cardLoop += 1

  return cardLoop

def findEncryptionKey(door, loop):
  encryptionKey = 1

  for i in range(loop):
    encryptionKey = (encryptionKey * door) % 20201227

  return encryptionKey

if __name__ == "__main__":
  dayTwentyFive(cardPublicKey, doorPublicKey)