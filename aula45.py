texto = 'Pedro'
iteratador = iter(texto)

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break