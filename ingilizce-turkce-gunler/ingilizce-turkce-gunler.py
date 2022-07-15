
ingilizcegünler = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]
türkçegünler = [ "pazartesi", "Salı", "Çarşamba", "perşembe", "cuma", "cumartesi", "pazar" ]
gün = input("Enter The Day: ")

a = 0
if(gün in ingilizcegünler):
    gün1 = ingilizcegünler.index(gün)
    while a < len(ingilizcegünler):           
       print(ingilizcegünler[gün1], ":", türkçegünler[gün1])
       a += 1
       break
else:
    print("Yanlış İfade Girdiniz: ")
