import toolkit

candidate = ["Apple", "samsung", "LG", "Xiaomi", "Huawei", "Oppo", "Vivo", "Oneplus", "Google", "Sony", "Nokia",
			 "Blackberry", "HTC", "Motorola", "Lenovo", "ZTE", "Asus", "Acer", "HP", "Dell", "Toshiba", "Fujitsu",
			 "Panasonic", "Sharp", "TCL", "Alcatel", "Meizu", "Coolpad", "Gionee", "LeEco", "Micromax", "Lava",
			 "Karbonn", "Intex", "iBall", "Xolo", "Spice", "Celkon", "Zen", "Fly", "Maxx", "iBerry", "Swipe",
			 "Videocon", "Wickedleak", "Obi", "Jolla", "Yota", "Yu", "Zopo", "Zync", "ZUK", "Umi"]

search = input("Enter the name of the brand: ").strip().lower()

print(toolkit.stringSuggestionV2(search, candidate, False))

print(toolkit.stringSuggestionV3(search, candidate, False, "*"))
