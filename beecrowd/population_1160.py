"""Questão 1160 do beecrownd - Nivel 5"""

def growing_population(actual, grow):
    """
    Calcula o tamanho da população após 1 ano de acordo com a taxa de crescimento
    """
    new_population = int((actual * grow) // 100)
    new_population += actual
    return new_population

test_cases = int(input())
city_a = {'population': 0, 'growing': 0.0}
city_b = {'population': 0, 'growing': 0.0}
years = 0 # tempo para população de A ultrapassar de B


while test_cases > 0:
    (
        city_a['population'], city_b['population'], 
        city_a['growing'], city_b['growing']
    ) = map(float,input().split())

    while True:
        years += 1

        if years > 100:
            print("Mais de 1 seculo.")
            years = 0
            break

        city_a['population']= (
                growing_population(city_a['population'], city_a['growing'])
                )
        
        city_b['population'] = (
            growing_population(city_b['population'], city_b['growing'])
            )

        #Verifico se a população de A ultrapassou de B
        if(city_a['population'] > city_b['population']):
            print(f"{years} anos.")
            years = 0
            break

    test_cases -= 1
    

