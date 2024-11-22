import csv

def generate_csv(filename, headers, data, delimiter=','):
    """
    Générateur de fichiers CSV général.

    :param filename: Nom du fichier CSV à créer (avec extension .csv).
    :param headers: Liste des en-têtes des colonnes.
    :param data: Liste de listes contenant les données.
    :param delimiter: Délimiteur utilisé dans le CSV (par défaut: ',').
    """
    try:
        # Ouverture du fichier en mode écriture
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=delimiter)

            # Écriture des en-têtes
            writer.writerow(headers)

            # Écriture des lignes de données
            writer.writerows(data)

        print(f"Fichier CSV généré avec succès : {filename}")

    except Exception as e:
        print(f"Erreur lors de la génération du fichier CSV : {e}")


if __name__ == "__main__":
    # Demander le nom du fichier
    print("Quel nom voulez-vous donner à votre fichier ? (par défaut: 'default.csv')")
    filename = input().strip()+".csv"

    if filename == ".csv":
        filename = "default"+".csv"

    # Demander le délimiteur
    print("Quel délimiteur voulez-vous utiliser ? (par défaut: ',')")
    delimiter = input().strip()
    if delimiter == "":
        delimiter = ','

    # Demander les en-têtes des colonnes
    print("Quels sont les en-têtes des colonnes ? (par défaut: 'Nom,Prénom,Âge,Email')")
    headers_input = input().strip()
    if  headers_input == "":
        headers = ["Nom", "Prénom", "Âge", "Email"]
    else:
        headers = headers_input.split(',')

    # Demander les données
    print("Voulez-vous ajouter des données personnalisées ? (par défaut: données d'exemple) [O/N]")
    response = input().strip().upper()
    if response == 'O':
        data = []
        print("Ajoutez vos données ligne par ligne au format 'valeur1,valeur2,valeur3,...'.")
        print(f"Nombre attendu de valeurs par ligne : {len(headers)}")
        print("Tapez 'STOP' pour arrêter l'ajout des données.")
        while True:
            row = input("Nouvelle ligne : ").strip()
            if row.upper() == 'STOP':
                break
            row_values = row.split(delimiter)
            if len(row_values) != len(headers):
                print(f"Erreur : Le nombre de valeurs ({len(row_values)}) ne correspond pas au nombre d'en-têtes ({len(headers)}). Réessayez.")
                continue
            data.append(row_values)
    else:
        # Données par défaut
        data = [
            ["Doe", "John", 28, "john.doe@example.com"],
            ["Smith", "Jane", 34, "jane.smith@example.com"],
            ["Brown", "Charlie", 45, "charlie.brown@example.com"]
        ]

    # Génération du fichier CSV
    generate_csv(filename, headers, data, delimiter)
