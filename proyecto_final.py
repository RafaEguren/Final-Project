import pandas as pd

def acquire():
    data = pd.read_csv('./Sist_Rec.csv').set_index('Name')
    return data

def report(data):
    def get_5(df, col):
        return df[col].sort_values(ascending = False)[1:6]#.index
    while True:
        try:
            name = input("¿Que videojuego te gusta? ")
            games = get_5(data, name)
            break
        except KeyError:  
            print("Ese juego no lo tengo, prueba con otro")
    print ("Te recomiendo estos 5 juegos: " + str(games))
    
if __name__ == '__main__':
    data = acquire()
    print(report(data))