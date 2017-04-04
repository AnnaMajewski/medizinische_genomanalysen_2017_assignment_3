#! /usr/bin/env python2

import vcf
import hgvs

__author__ = 'Anna Majewski'
## Damit das Programm funktioniert, musste der Interpreter auf 2.7. gestellt werden.


class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        ## Check if hgvs is installed
        print("HGVS version: %s" % hgvs.__version__)

        ## Dateinamen in Variablen fuer Vater und Mutter
        self.filename_mother = 'AmpliseqExome.20141120.NA24143.vcf'
        self.filename_father = 'AmpliseqExome.20141120.NA24149.vcf'
        self.filename_son = 'AmpliseqExome.20141120.NA24385.vcf'

        ## Oeffnen mit vcf.Reader
        self.file_mother = vcf.Reader(open(self.filename_mother, 'r'))
        self.file_father = vcf.Reader(open(self.filename_father, 'r'))
        self.file_son = vcf.Reader(open(self.filename_son, 'r'))
        

    def get_total_number_of_variants_mother(self):
        '''
        Return the total number of identified variants in the mother
        :return: total number of identified variants in the mother
        '''
        ## Oeffnen mit vcf.Reader
        self.file_mother = vcf.Reader(open(self.filename_mother, 'r'))
        anzahl = 0
        for record in self.file_mother:
            anzahl += 1
        return anzahl
        
        
    def get_total_number_of_variants_father(self):
        '''
        Return the total number of identified variants in the father
        :return: total number of identified variants in the father
        '''
        ## Oeffnen mit vcf.Reader
        self.file_father = vcf.Reader(open(self.filename_father, 'r'))
        anzahl = 0
        for record in self.file_father:
            anzahl += 1
        return anzahl
       
        
    def get_variants_shared_by_father_and_son(self):
        '''
        Return the number of identified variants shared by father and son
        :return: number of identified variants shared by father and son
        '''
        ## Oeffnen mit vcf.Reader
        self.file_father = vcf.Reader(open(self.filename_father, 'r'))
        self.file_son = vcf.Reader(open(self.filename_son, 'r'))

        anzahl = 0

        for record in self.file_father:
            if record in self.file_son:
                anzahl += 1

        return anzahl

        
        
    def get_variants_shared_by_mother_and_son(self):
        '''
        Return the number of identified variants shared by mother and son
        :return: 
        '''
        ## Oeffnen mit vcf.Reader
        self.file_mother = vcf.Reader(open(self.filename_mother, 'r'))
        self.file_son = vcf.Reader(open(self.filename_son, 'r'))

        anzahl = 0

        for record in self.file_mother:
            if record in self.file_son:
                anzahl += 1

        return anzahl
        
    def get_variants_shared_by_trio(self):
        '''
        Return the number of identified variants shared by father, mother and son
        :return: 
        '''
        ## Oeffnen mit vcf.Reader
        self.file_mother = vcf.Reader(open(self.filename_mother, 'r'))
        self.file_father = vcf.Reader(open(self.filename_father, 'r'))
        self.file_son = vcf.Reader(open(self.filename_son, 'r'))

        anzahl = 0

        for record in self.file_mother:
            if record in self.file_father:
                if record in self.file_son:
                    anzahl += 1

        return anzahl
        

    def merge_mother_father_son_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        ## class vcf.Writer(stream, template, lineterminator='n')[source]
        ## der Writer benoetigt ein template, aus dem die metadaten uebernommen werden
        ## ich habe mich fuer den Sohn entschieden
        ## ein Stream im Modus write wird geoeffnet
        trio_file = open("trio_file.vcf", "w")
        writer = vcf.Writer(trio_file, self.file_son, "\n")
        ## http://nullege.com/codes/search/vcf.utils.walk_together
        ## um mehrere vcf Files gleichzeitig zu bearbeiten kann man vcf.utils.walk_together benutzen
        # wie das genau geht, muss ich mich noch weiter informieren ...

        print("TODO")
        
        
    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return: 
        '''
        print("TODO")
        
    
    def print_summary(self):
        ## Hier werden alle Methoden aufgerufen und mit einem String versehen, der beschreibt was sie ausgeben.
        print("Total Number of Variants in the Mother: %s" % self.get_total_number_of_variants_mother())
        print("Total Number of Variants in the Father: %s" % self.get_total_number_of_variants_father())
        print("Total Number of Variants shared by Father and Son: %s" % self.get_variants_shared_by_father_and_son())
        print("Total Number of Variants shared by Mother and Son: %s" % self.get_variants_shared_by_mother_and_son())
        print("Total Number of Variants shared by all three: %s" % self.get_variants_shared_by_trio())
        #print(self.merge_mother_father_son_into_one_vcf())
    
        
if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()
    
    

