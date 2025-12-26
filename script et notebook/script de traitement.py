# script à reporter dans Machine Learning Studio
df['waiseline'] =df['waiseline'].fillna(df['waiseline'].mode()[0])
df['Pattern Type'] =df['Pattern Type'].fillna(df['Pattern Type'].mode()[0])
df['Price'] =df['Price'].fillna(df['Price'].mode()[0])
df['Season'] =df['Season'].fillna(df['Season'].mode()[0])
df['NeckLine'] =df['NeckLine'].fillna(df['NeckLine'].mode()[0])

df['SleeveLength'] =df['SleeveLength'].fillna(df['SleeveLength'].mode()[0])


df['FabricType'] =df['FabricType'].fillna(df['FabricType'].mode()[0])
df['Material'] =df['Material'].fillna(df['Material'].mode()[0])
df['Decoration'] =df['Decoration'].fillna(df['Decoration'].mode()[0])




# Standardisation des valeurs
df['Style'] = df['Style'].str.lower()
df['Price'] = df['Price'].str.lower()
df['Season'] = df['Season'].str.lower().replace({'automn': 'autumn'})
df['Size'] = df['Size'].str.lower().replace({'free': 'one-size'})
df['Size'] = df['Size'].str.lower().replace({'sexy': 'sexy'})
df['Style'] = df['Style'].str.lower().replace({'se xy': 'sexy', 'novelty': 'novelty'})  # Standardisation
df['Rating'] = df['Rating'].astype(str).str.replace(',', '.').astype(float)

# Correction des typos pour les colonnes textuelles
df['NeckLine'] = df['NeckLine'].str.replace('-', ' ').str.replace('collor', 'collar')
df['SleeveLength'] = df['SleeveLength'].str.replace('sleevless', 'sleeveless')


df = df.drop(columns=['Dress_ID'])




df['Price']=df['Price'].replace({'low':0, 'average':1, 'medium':2, 'high':3, 'very-high':4})

df['Size']=df['Size'].replace({

    's':0,        # 0 (le plus petit)
    'small':1,    # 1
    'm':2,        # 2 
    'l':3,        # 3
    'xl':4,       # 4 (le plus grand)
    'one-size':5
})


# Pour faire l'encodage par fréquence


valeur=df['Style'].value_counts()
df['Style']=df['Style'].map(valeur)

valeur=df['Season'].value_counts()
df['Season']=df['Season'].map(valeur)


valeur=df['NeckLine'].value_counts()
df['NeckLine']=df['NeckLine'].map(valeur)


valeur=df['SleeveLength'].value_counts()
df['SleeveLength']=df['SleeveLength'].map(valeur)


valeur=df['waiseline'].value_counts()
df['waiseline']=df['waiseline'].map(valeur)

valeur=df['Material'].value_counts()
df['Material']=df['Material'].map(valeur)


valeur=df['FabricType'].value_counts()
df['FabricType']=df['FabricType'].map(valeur)



valeur=df['Decoration'].value_counts()
df['Decoration']=df['Decoration'].map(valeur)

valeur=df['Pattern Type'].value_counts()
df['Pattern Type']=df['Pattern Type'].map(valeur)