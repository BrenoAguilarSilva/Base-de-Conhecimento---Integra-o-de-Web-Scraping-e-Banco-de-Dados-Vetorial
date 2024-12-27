import re
import unicodedata

import re

# Função para limpar o texto
def cleanText(text):
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)  
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)   
    text = re.sub(r'<.*?>', '', text) 
     
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '', text)
    
    text = re.sub(r'[@#*]', '', text)
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    licensingRegex = r"This work is licensed under CC BY 4.0.*?attribution"
    eventsRegex = r"Events.*?View All Events"
    certificacoesRegex = r"Certifications.*?View All"
    additionalInformationRegex = r"Additional Information.*?Framework Overview"
    informationFooterRegex = r"© FinOps Foundation.*?Technical Charter"
    unwantedHeaderRegex = r"close.*?scopes"
    unwantedMenusRegex = r"finops assets.*?scopes"
    languageRegex = r"download finops framework poster.*?日本語"
    unwantedFooterRegex = r"what's new in the finops framework.*?of finops project a series of lf projects, llc, please see the technical charter ."
    unwantedAlternativeFooterRegex = r"×.*?of finops project a series of lf projects, llc, please see the technical charter ."
    removeMakeASuggestionRegex = r"make suggestion"

    text = re.sub(licensingRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(eventsRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(certificacoesRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(additionalInformationRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(informationFooterRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(unwantedHeaderRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(unwantedMenusRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(languageRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(unwantedFooterRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(unwantedAlternativeFooterRegex, "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(removeMakeASuggestionRegex, "", text, flags=re.IGNORECASE)

    return text



def normalizeCharacters(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text

