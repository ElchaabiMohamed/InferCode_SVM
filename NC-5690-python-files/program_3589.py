def doubleChiffre(nombre):
  ok=False
  elemPrec=nombre%10
  while nombre!=0 and not ok:
    nombre//=10
    elemAct=nombre%10
    if elemPrec==elemAct:
      ok=True
    elemPrec=nombre%10
  return ok