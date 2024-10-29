rept = {"python": "питон",
 "anaconda": "анаконда",
 "tortoize": "черепаха"}

rept["snake"] = "змея"

rept["tortoise"] = rept.pop("tortoize")

for k, v in rept.items():
    print(f"{v.capitalize()} по-английски будет {k}.")