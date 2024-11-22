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

# Exemple d'utilisation
if __name__ == "__main__":
    # Nom du fichier de sortie
    filename = "example"+".csv"

    # En-têtes des colonnes
    headers = ["Nom", "Prénom", "Âge", "Email"]

    # Données d'exemple
    data = [
        ["Doe", "John", 28, "john.doe@example.com"],
        ["Smith", "Jane", 34, "jane.smith@example.com"],
        ["Brown", "Charlie", 45, "charlie.brown@example.com"]
    ]

    # Générer un fichier CSV avec le délimiteur par défaut (',')
    generate_csv(filename, headers, data)
