import requests
import browsercookie

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def get_aanduidingstype(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    mapping = {
      "https://id.erfgoed.net/thesauri/aanduidingstypes/11": "Vastgestelde inventaris van de archeologische zones",
      "https://id.erfgoed.net/thesauri/aanduidingstypes/10": "Vastgestelde landschapsatlas",
	  "https://id.erfgoed.net/thesauri/aanduidingstypes/9": "Vastgestelde inventaris van het bouwkundig erfgoed",
      "https://id.erfgoed.net/thesauri/aanduidingstypes/12": "Vastgestelde inventaris van houtige beplantingen met erfgoedwaarde",
	  "https://id.erfgoed.net/thesauri/aanduidingstypes/13": "Vastgestelde inventaris van historische tuinen en parken"
    }
    return mapping[e_obj['type']['uri']]

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_titel_tekst(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['primaire_tekst']['tekst']

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_titel(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['omschrijving']

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_tekst(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return '<div>' + e_obj['primaire_tekst']['tekst'] + '</div>'
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_locatie(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['locatie']['provincie'] + ' - ' + e_obj['locatie']['gemeente']

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_provincie(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['locatie']['provincie']

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_gemeente(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['locatie']['gemeente']

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_korte_beschrijving(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['korte_beschrijving']
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_typologie_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'typologie' in e_obj and len(e_obj['typologie']) > 0:
        for naam in e_obj['typologie']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Typologie: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_datering_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'datering' in e_obj and len(e_obj['datering']) > 0:
        for naam in e_obj['datering']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Datering: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_soort_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'soort' in e_obj and len(e_obj['soort']) > 0:
        for naam in e_obj['soort']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Soort: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_materiaal_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'materiaal' in e_obj and len(e_obj['materiaal']) > 0:
        for naam in e_obj['materiaal']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Materiaal: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_context_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'context' in e_obj and len(e_obj['context']) > 0:
        for naam in e_obj['context']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Context: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_stijl_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'stijl' in e_obj and len(e_obj['stijl']) > 0:
        for naam in e_obj['stijl']:
            s.append(naam['naam'])
        htmlstring = '<p><b>Stijl of cultuur: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_waarden_html(url, feature, parent):
    id = 'bes_bescherming.' + url.rsplit('/', 1)[-1]
    url = 'https://inventaris.onroerenderfgoed.be/erfgoed/node/' + str(id) + '/waarden.json'
    cj = browsercookie.firefox()
    waarden = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    if 'waarden' in waarden:
        s = []
        for waarde in waarden['waarden']:
            for waardetype in waarde['waardetypes']:
                url = 'https://inventaris.onroerenderfgoed.be/thesaurus/waarde/' + str(waardetype) + '.json'
                label = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()['term']
                s.append(label)
        htmlstring = '<p>' + '<br>'.join(s) + '</p>'
        return htmlstring
    else:
        return ''
		
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_waarden_tekst_html(url, feature, parent):
    id = 'bes_bescherming.' + url.rsplit('/', 1)[-1]
    url = 'https://inventaris.onroerenderfgoed.be/erfgoed/node/' + str(id) + '/waarden.json'
    cj = browsercookie.firefox()
    waarden = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    if 'waarden' in waarden and len(waarden['waarden']) > 0:
        h = '<h4>Erfgoedwaarden</h4>'
        for waarde in waarden['waarden']:
            if waarde['uiteenzetting']:
                tekst = waarde["uiteenzetting"]
            else:
                tekst = ''
            for waardetype in waarde['waardetypes']:
                url = 'https://inventaris.onroerenderfgoed.be/thesaurus/waarde/' + str(waardetype) + '.json'
                label = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()['term']
                h =  h + '<p><b>' + label + '</b></p>'
            h = h + '<p>' + tekst + '</p>'
        return h
    else:
        return ''
        
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_url(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['relaties'][0]['links'][0]['href']
