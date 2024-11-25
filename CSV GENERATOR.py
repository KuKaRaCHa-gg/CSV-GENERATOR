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
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=delimiter)

            # Écriture des en-têtes
            writer.writerow(headers)

            # Écriture des lignes de données
            writer.writerows(data)

        print(f"✅ Fichier CSV généré avec succès : {filename}")

    except Exception as e:
        print(f"❌ Erreur lors de la génération du fichier CSV : {e}")


def get_filename():
    """
    Demande à l'utilisateur de fournir un nom de fichier.
    Renvoie le nom du fichier avec extension .csv.
    """
    filename = input("Quel nom voulez-vous donner à votre fichier ? (par défaut: 'default.csv')\n").strip()
    if not filename:
        filename = "default.csv"
    elif not filename.endswith(".csv"):
        filename += ".csv"
    return filename


def get_delimiter():
    """
    Demande à l'utilisateur de fournir un délimiteur.
    Renvoie le délimiteur choisi.
    """
    delimiter = input("Quel délimiteur voulez-vous utiliser ? (par défaut: ',')\n").strip()
    return delimiter if delimiter else ','


def get_headers():
    """
    Demande à l'utilisateur de fournir les en-têtes des colonnes.
    Renvoie une liste des en-têtes.
    """
    headers_input = input("Quels sont les en-têtes des colonnes ? (par défaut: 'Nom,Prénom,Âge,Email')\n").strip()
    if not headers_input:
        return ["Nom", "Prénom", "Âge", "Email"]
    return headers_input.split(',')


def get_data(headers, delimiter):
    """
    Demande à l'utilisateur d'ajouter des données ligne par ligne.
    Renvoie une liste de listes contenant les données.
    """
    print("Voulez-vous ajouter des données personnalisées ? [O/N] (par défaut: données d'exemple)")
    response = input().strip().upper()
    if response == 'O':
        data = []
        print(f"Ajoutez vos données ligne par ligne au format 'valeur1{delimiter}valeur2{delimiter}valeur3,...'.")
        print(f"Nombre attendu de valeurs par ligne : {len(headers)}")
        print("Tapez 'STOP' pour arrêter l'ajout des données.")
        while True:
            row = input("Nouvelle ligne : ").strip()
            if row.upper() == 'STOP':
                break
            row_values = row.split(delimiter)
            if len(row_values) != len(headers):
                print(f"⚠️ Erreur : Le nombre de valeurs ({len(row_values)}) ne correspond pas au nombre d'en-têtes ({len(headers)}). Réessayez.")
                continue
            data.append(row_values)
        return data
    else:
        # Données par défaut
        return [
            ["Doe", "John", 28, "john.doe@example.com"],
            ["Smith", "Jane", 34, "jane.smith@example.com"],
            ["Brown", "Charlie", 45, "charlie.brown@example.com"]
        ]


if __name__ == "__main__":
    print("=== Générateur de fichier CSV ===")
    filename = get_filename()
    delimiter = get_delimiter()
    headers = get_headers()
    data = get_data(headers, delimiter)

    generate_csv(filename, headers, data, delimiter)
