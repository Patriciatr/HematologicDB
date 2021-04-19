#Select all disease that have fever as a symptom
SELECT Name ,ICD_10 FROM hematologicDB.Disease d, hematologicDB.Symptoms s 
where d.Symptoms_idSymptoms = s.idSymptoms AND s.Fever = 1;

#Select all disease that have Weight Loss as a symptom
SELECT Name ,ICD_10 FROM hematologicDB.Disease d, hematologicDB.Symptoms s 
where d.Symptoms_idSymptoms = s.idSymptoms AND s.Otros LIKE '%Weight Loss%';

#SELECT THE NAMES OF THE PROTEINS ON THESE CHROMOSOMES
SELECT Name,Proteome 
From hematologicDB.Protein 
WHERE Proteome IN ("Chromosome 3", "Chromosome 7","Chromosome X");

#Select the Name and proteome of the proteins with the symbol and type of the genes that correspond to them
SELECT p.Name, p.Proteome, g.Symbol, g.Type FROM hematologicDB.Protein p INNER JOIN hematologicDB.Genes g 
ON p.Genes_idGenes = g.idGenes
order by p.Proteome;

#Select the Name and ICD10 with their respective name and sequence of the protein 
SELECT d.Name, d.ICD_10, p.Name, p.Sequence  FROM hematologicDB.Disease d LEFT JOIN hematologicDB.Protein p 
ON d.idDisease = p.Disease_idDisease 
group by d.Name, d.ICD_10, p.Name, p.Sequence 
order by d.ICD_10;

# SELECT PROTEIN NAMES WITH MOLECULAR AND BIOLOGICAL FUNCTIONS FOR GENES "KMT2C","KMT2A","BCL6"
SELECT Name , Molec_function,Bio_proces
FROM hematologicDB.Protein 
WHERE Genes_idGenes IN (SELECT idGenes FROM hematologicDB.Genes WHERE Symbol IN ("KMT2C","KMT2A","BCL6"));

#SELECT THE PROTEINS WHICH DISEASE HAS THE CODE ICD10 C91 OR C92
SELECT Name , Proteome 
FROM hematologicDB.Protein
WHERE Disease_idDisease IN (SELECT idDisease FROM hematologicDB.Disease WHERE ICD_10=" C91" OR ICD_10="C92")





