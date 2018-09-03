
sugar = 400/48
butter = 320/48
chocolate = 500/48
egg = 2/48
flour = 460/48

amount_cookies = int(input("Hvor mange cookies ønsker du å bake? "))

print("Antall cookies:", amount_cookies)
print("sukker(g):", sugar * amount_cookies)
print("smør(g):", butter * amount_cookies)
print("sjokolade(g):", chocolate * amount_cookies)
print("egg:", egg * amount_cookies)
print("hvetemel(g):", flour * amount_cookies)

amount_cookies_0 = int(input("Hvor mange cookies vil du lage? "))
amount_cookies_1 = int(input("Hvor mange cookies vil du lage nå? "))
amount_cookies_2 = int(input("Hvor mange cookies vil du lage til slutt? "))

print("Antall cookies: \t", "sukker(g) \t", "sjokolade(g)")

sugar_str = str(round(sugar * amount_cookies_0,2))
sugar_str = sugar_str.rjust(30)
chocolate_str = str(round(chocolate * amount_cookies_0,2))
chocolate_str = chocolate_str.rjust(18)
print(amount_cookies_0, sugar_str, chocolate_str)

sugar_str = str(round(sugar * amount_cookies_1,2))
sugar_str = sugar_str.rjust(30)
chocolate_str = str(round(chocolate * amount_cookies_1,2))
chocolate_str = chocolate_str.rjust(18)
print(amount_cookies_1, sugar_str, chocolate_str)

sugar_str = str(round(sugar * amount_cookies_2,2))
sugar_str = sugar_str.rjust(30)
chocolate_str = str(round(chocolate * amount_cookies_2,2))
chocolate_str = chocolate_str.rjust(18)
print(amount_cookies_2, sugar_str, chocolate_str)
