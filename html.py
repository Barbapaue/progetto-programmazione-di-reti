def header():
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Azienda Ospedaliera</title></head><body>'


def footer():
    return '</body></html>'


def hospitalFeatureTitle():
    return '<h1>Ospedale Santa Maria degli Angeli di Pordenone</h1><h3>Servizi erogati</h3>'


list_item = [("Home", "https://asfo.sanita.fvg.it/it/presidi-ospedalieri/ospedale-santa-maria-degli-angeli-pordenone/", ""),
             ("112", "https://asfo.sanita.fvg.it/it/servizi/112.html", ""),
             ("Continuità Assistenziale", "https://asfo.sanita.fvg.it/it/servizi/guardia_medica.html", ""),
             ("Scarica PDF per maggiori info", "https://virtuale.unibo.it/pluginfile.php/828762/mod_resource/content"
                                               "/1/tracce%20Progetti%20di%20fine%20corso%202020_2021.pdf", "download")]


def hospitalFeature():
    return '<ul>'+''.join(map(lambda item: '<li><a href="' + item[1] + '" ' + item[2] + '>' + item[0] + '</a></li>', list_item)) + '<ul>'


