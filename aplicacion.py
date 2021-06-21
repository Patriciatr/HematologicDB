import pymysql

connection = pymysql.connect (host = 'localhost',
                             user = 'root',
                             password = '123456',
                             db = 'hematologicDB',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

print("Data Base Connected")


def guery1(conexion):
    cursor = conexion.cursor()
    guery = "SELECT Name ,ICD_10 " \
            "FROM hematologicDB.Disease d, hematologicDB.Symptoms s " \
            "where d.Symptoms_idSymptoms = s.idSymptoms AND s.Fever = 1;"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery2(conexion):
    cursor = conexion.cursor()
    guery = "SELECT Name ,ICD_10 " \
            "FROM hematologicDB.Disease d, hematologicDB.Symptoms s " \
            "where d.Symptoms_idSymptoms = s.idSymptoms AND s.Otros LIKE '%Weight Loss%';"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery3(conexion,chr):
    cursor = conexion.cursor()
    guery = "SELECT Name,Proteome " \
               "From hematologicDB.Protein " \
               "WHERE Proteome IN (" + chr + ");"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery4(conexion,genes):
    cursor = conexion.cursor()
    guery = "SELECT p.Name, p.Proteome, g.Symbol, g.Type " \
               "FROM hematologicDB.Protein p INNER JOIN hematologicDB.Genes g ON p.Genes_idGenes = g.idGenes" \
               " WHERE Symbol IN (" + genes + ") order by p.Proteome;"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery5(conexion):
    cursor = conexion.cursor()
    guery = "SELECT d.Name, d.ICD_10, p.Name, p.Sequence " \
               "FROM hematologicDB.Disease d LEFT JOIN hematologicDB.Protein p ON d.idDisease = p.Disease_idDisease" \
               " WHERE Molec_function LIKE '%histone%' " \
               "group by d.Name, d.ICD_10, p.Name, p.Sequence " \
               "order by d.ICD_10;"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery6(conexion, genes):
    cursor = conexion.cursor()
    guery = "SELECT Name , Molec_function,Bio_proces " \
            "FROM hematologicDB.Protein " \
            "WHERE Genes_idGenes IN (SELECT idGenes FROM hematologicDB.Genes WHERE Symbol IN ("+genes+"));"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def guery7(conexion, icd):
    cursor = conexion.cursor()
    guery = "SELECT Name , Proteome " \
            "FROM hematologicDB.Protein " \
            "WHERE Disease_idDisease IN " \
            "(SELECT idDisease FROM hematologicDB.Disease WHERE "+icd+")"
    cursor.execute(guery)
    for resultado in cursor:
        print(resultado)
    cursor.close()

def queryDisease(connection):
    print("1. Select all disease that have fever as a symptom")
    print("2. Select all disease that have Weight Loss as a symptom")
    print("3. Select the Name and ICD10 with their respective name and sequence of the protein relate to histone")
    print("4. Exit")
    opc = int(input("Select one of the options: "))
    while opc != 4:
        if opc == 1:
            guery1(connection)
        elif opc == 2:
            guery2(connection)
        elif opc == 3:
            guery5(connection)
        else:
            print("Error, invalid option")

        print("1. Select all disease that have fever as a symptom")
        print("2. Select all disease that have Weight Loss as a symptom")
        print("3. Select the Name and ICD10 with their respective name and sequence of the protein relate to histone")
        print("4. Exit")
        opc = int(input("Select one of the options: "))


def guery(connection):
    print("1. Select the names of the proteins on a given chromosomes")
    print("2. Select the Name and proteome of the proteins with the symbol and type of the genes")
    print("3. Select protein and names with molecular and biological functions for the desired genes")
    print("4. Select the proteins which disease with the given ICD10")
    print("5. Exit")
    opc = int(input("Select one of the options: "))
    while opc != 5:
        if opc == 1:
            chr = input("Enter the chromosomes: ")
            guery3(connection, chr)
        elif opc == 2:
            genes = input("Enter the genes: ")
            guery4(connection, genes)
        elif opc == 3:
            genes = input("Enter the genes: ")
            guery6(connection, genes)
        elif opc == 4:
            icd = input("Enter the ICD10: ")
            guery7(connection, icd)
        else:
            print("Error, invalid option")

        print("1. Select the names of the proteins on a given chromosomes")
        print("2. Select the Name and proteome of the proteins with the symbol and type of the genes")
        print("3. Select protein and names with molecular and biological functions for the desired genes")
        print("4. Select the proteins which disease with the given ICD10")
        print("5. Exit")
        opc = int(input("Select one of the options: "))

print("Welcome. These are the types of queries you can make")
print("1. About the disease")
print("2. About proteins or genes ")
print("3. Exit ")

opc = int(input("Select one of the options: "))
while opc != 3:
    if opc == 1:
        queryDisease(connection)
    elif opc == 2:
        guery(connection)
    else:
        print("Error, invalid option")

    print("1. About the disease")
    print("2. About proteins or genes ")
    print("3. Exit ")
    opc = int(input("Select one of the options: "))

connection.close()
