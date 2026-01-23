travel_log = {
	"France" : ["Paris", "Lille", "Dijon"],
	"Germany" : ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])

lista_aninhada = ["A", "B", ["C","D"]]
print(lista_aninhada[2][1])

travel_log2 = {
	"France" : {
		"Cities_visited" :
			["Paris" "Lille", "Dijon"],
			"Total_visits" : 12
	},
	"Germany" : {
		"Cities_visited" :
			["Berlin", "Hamburg", "Stuttgart"],
			"Total_visits" : 5
	}
}

print(travel_log2["Germany"]["Cities_visited"][2])