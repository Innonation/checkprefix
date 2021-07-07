from .choices import PrefixStatus, Prefixes

def verify_prefix(country_code, prefix):
    """
    Dato in input il Country code relativo alla nazione e il prefisso che si vuole verificare,
    restituisce la validità del prefisso per quella nazione.
    :param country_code: codice identificativo della nazione da controllare
    :param prefix: prefisso da controllare
    :return: Oggetto di tipo PrefixStatus (Enum) che contiene i dettagli di stato
    """
    try:
        for row in Prefixes:
            if row.name == country_code:
                if row.value[1] == prefix:
                    return PrefixStatus.OK
                return PrefixStatus.NOT_VALID
        return PrefixStatus.NOT_FOUND
    except:
        return PrefixStatus.EXCEPT

def get_country_prefix(country_code):
    """
    Dato in input il Country code relativo alla nazione, restituisce il prefisso per quella nazione, se è presente.
    :param country_code: codice identificativo della nazione da controllare
    :return: Oggetto di tipo Prefixes (Enum) che contiene il prefisso oppure un oggetto di tipo PrefixStatus (Enum) che contiene i dettagli di stato
    """
    for row in Prefixes:
        if row.name == country_code:
            return row
    return None
