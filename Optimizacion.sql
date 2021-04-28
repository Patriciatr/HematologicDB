#Steps for the optimization:
#1- change the type of the column Name in the table disease from "LONGTEXT" to "VARCHAR(255)" to add Index to make the value a unique value
#2- change the type of the column Name in the table Protein from "LONGTEXT" to "VARCHAR(255)" to add Index for searching for atribut (proteome)
#3- make the Symbol of the gen in the Genes table a unique value


#Create index to make the Name a unique value in the table Disease
CREATE UNIQUE INDEX idx_name ON hematologicDB.Disease(Name);

#Create index to make the ICD10 a unique value in the table Disease
CREATE UNIQUE INDEX idx_icd10 ON  hematologicDB.Disease(ICD_10);

#Create index for the in which proteome we can finde it we can find it in the table Protein
CREATE INDEX idx_Protein ON  hematologicDB.Protein(Proteome);

#To drop and index
#DROP INDEX idx_Protein ON hematologicDB.Protein;

SELECT Name
FROM hematologicDB.Protein
WHERE Proteome="Chromosome 11";

#Create index to make the Symbol a unique value in the table Genes
CREATE UNIQUE INDEX idx_symbol ON hematologicDB.Genes(Symbol);

