Countries = {"USA":"washington DC","Italy":"Rome","England":"London"}
print("Dictionary",Countries)

print("Length of Dictonary[Countries]:",len(Countries))

#accessing dictionary items
print(Countries["USA"])
print(Countries.get("Italy"))

#change dictionary items

Countries["Italy"]="rome_"
print(Countries)

Countries["Germany"] = "Berlin"
print(Countries)

#remove dictionary items

del Countries["USA"]
print(Countries)


print(Countries.keys())

print(Countries.values())