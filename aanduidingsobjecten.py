import requests
import browsercookie

from qgis.core import *
from qgis.gui import *

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
    if 'typologie' in e_obj:
        for term in e_obj['typologie']:
            s.append(term['term'])
        htmlstring = '<p><b>Typologie: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_datering_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'datering' in e_obj:
        for term in e_obj['datering']:
            s.append(term['term'])
        htmlstring = '<p><b>Datering: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_soort_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'soort' in e_obj:
        for term in e_obj['soort']:
            s.append(term['term'])
        htmlstring = '<p><b>Soort: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_materiaal_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'materiaal' in e_obj:
        for term in e_obj['materiaal']:
            s.append(term['term'])
        htmlstring = '<p><b>Materiaal: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_context_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'context' in e_obj:
        for term in e_obj['context']:
            s.append(term['term'])
        htmlstring = '<p><b>Context: </b>' + ', '.join(s) + '</p>'
        return htmlstring
    else:
        return ''

@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_stijl_html(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    s = []
    if 'stijl' in e_obj:
        for term in e_obj['stijl']:
            s.append(term['term'])
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
        htmlstring = '<p>' + ''.join(s) + '</p>'
        return htmlstring
    else:
        return ''
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_type(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    htmlstring = '<p><b>Vastgestelde inventaris van ' + e_obj['type']['label'] + 's</b></p>'
    return htmlstring
    
@qgsfunction(args='auto', group='Custom')
def get_aanduidingsobject_url(url, feature, parent):
    cj = browsercookie.firefox()
    e_obj = requests.get(url, headers={'Accept': 'application/json'}, cookies=cj).json()
    return e_obj['relaties'][0]['links'][0]['href']
