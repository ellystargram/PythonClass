import toolkit as engine

originalString = ("날 잊어버린다 해도, 다시한번 너를 만나러 갈테니까. 따라 라라라따라")





quantomizedString = engine.quantomize(list(originalString))
print(quantomizedString)
dequantomizedString = engine.dequantomize(quantomizedString)
print(dequantomizedString)

key = 697442

print(engine.keyedQuantomize(list(originalString), key))
print(engine.keyedDequantomize(engine.keyedQuantomize(list(originalString), key), key))

print(engine.combinedQuantomize(list(originalString), key, 10))
print(engine.combinedDequantomize(engine.combinedQuantomize(list(originalString), key, 10), key, 10))

idols = ["징버거", "아이네", "릴파", "주르르", "비챤", "고세구"]
print(idols)
idols.sort()
print(idols)

for f in range(2, 10):
	for b in range(1, 10):
		print(f, "*", b, "=", f * b)
