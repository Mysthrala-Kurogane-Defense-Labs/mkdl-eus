"""One-time, reviewed Basque landing migration from the upstream Spanish page."""
from html.parser import HTMLParser
from pathlib import Path
import html

root = Path(__file__).resolve().parents[1]
translations = '''MKDL | OT Check, industria-prozesu baten azterketa
Edukira joan
OT Check
Entregaren adibidea
Kontaktua
Zibersegurtasun-plan bat zure lantegiko prozesu baterako.
OT Check zerbitzuak industria-prozesu bat aztertzen du, zer hobetu eta hornitzaileei zer eskatu erabakitzen laguntzeko. Lehentasunen arabera antolatutako jarduketak, arduradun-proposamenak eta hobekuntza bakoitza amaitutzat emateko egiaztapenak jasoko dituzu.
Erosle batek ebidentziak eskatzen dituenean, berreskuratze bat prestatu behar duzunean edo mantentze-enpresa baten sarbidea koordinatu behar denean, arlo bakoitzaren ezagutza bildu eta eskaera zehatz bihurtu behar da.
OT Check zerbitzuari buruz galdetu
Entregaren adibide bat ikusi
Fikziozko entregaren adibidea (gaztelaniaz). 
Txostena eta ebidentziak irakurri (gaztelaniaz)
.
Zer aztertzen dugu zurekin?
Lantegi bateko prozesu bat eta hartu behar duzun erabaki bat adosten ditugu. Elkarrizketak, dokumentuak eta behaketak aztertzen ditugu, zuzendaritzako, informatikako, mantentze-lanetako eta hornitzaileetako pertsona egokiekin. Ondorio bakoitzean bereizten dira egiaztatutakoa eta argitzeke dagoena.
Entregak produkzioaren, kalitatearen, mantentze-lanen, informatikaren eta hornitzaileen informazioa lotzen du. Aurrekontu konparagarriak eskatzeko eta hobekuntza bakoitza onartzeko zer ebidentzia beharko den adosteko balio du. Azterketak ez zaitu ekipamendurik erostera edo gauzatzea MKDLrekin kontratatzera behartzen.
Txosten bat, matrize editagarriak eta emaitzak azaltzeko bilera bat jasoko dituzu. Sakontasuna, parte-hartzaileak, bisita, egutegia eta prezioa lana kontratatu aurretik zehazten dira. Entregak argibide-txanda bat barne hartzen du. Adostutako irismenarekiko akatsak kostu gehigarririk gabe zuzentzen dira.
OT Check zerbitzuak ez ditu barne hartzen aldaketak, inplementazioa, eskaneatzeak, sartze-probak edo leheneratzeak. Ezta operazioa, gorabeheren kudeaketa, etengabeko laguntza edo ziurtapena ere. Zuk baimendutako taldeak edo hornitzaileak gauzatzen ditu hobekuntzak. Prestakuntza osagarriak beste kontratazio bat behar du.
OT Check tamaina desberdinetako industria-enpresentzat eta taldeetako unitateentzat pentsatuta dago, profesional bakarrak bere gain hartzeko moduko irismenarekin. Euskaditik lan egiten dut, eta joan-etorriak aurrekontuan zehazten dira. Plangintzarako erreferentzia gisa, hamar lanegun proposatzen dira bisita egin eta iturri guztiak jaso ondoren; epea eta prezioa lan bakoitzerako adosten dira.
Nor dago MKDLren atzean?
Kalista naiz, Uni Eibar-Ermuan zibersegurtasunean espezializatua. Nik neuk egiten dut azterketa eta azaltzen dut entrega, prozesua ezagutzen dutenekin koordinatuta.
Nire taldeak, MKDLNULLek, bigarren postua lortu zuen CyberLehia 2026 lehiaketan, Lanbide Heziketako taldeen arteko zibersegurtasun-lehiaketan. 
Taldearen sailkapena kontsultatu
.
Jasoko zenukeenaren adibide bat
Fikziozko zelula honetan programen kopiak daude, baina ekipamendu bakoitzak prozesua berreraikitzeko zer behar duen zehaztu gabe dago. Bi fitxategik etiketa bera dute, baina eduki desberdina. Txostenak iturri horiek lotzen ditu, aktibo bakoitzeko katalogo bat proposatzen du eta mantentze-enpresarentzako lanak zehazten ditu. Ez dagokio benetako bezero bati. Adibidearen dokumentuak gaztelaniaz daude.
Txostena eta ebidentziak irakurri (gaztelaniaz)
PDF txostena deskargatu (gaztelaniaz)
Hainbat hornitzaile sartzen dira ekipamenduetara
Simulazio honetan, mantentze-lanetako eta informatikako arloek sarbideei buruzko informazioaren zati bana dute, baina ez dute esku-hartze bakoitza nork baimentzen duen jasotzen duen zerrenda partekaturik.
OT Check zerbitzuak prozesuaren dokumentazioa eta elkarrizketak alderatzen ditu. Sarbideen zerrenda, argitu beharreko baieztapenak eta arduradun-proposamenak ematen ditu, zer berrikuspen eskatu erabakitzeko. Ez du sarbiderik kentzen edo aldatzen.
Kopiak daude, baina zer berreskura daitekeen egiaztatu gabe dago
Simulazio honetan programen kopiak daude eta aurretik proba bat egin zela adierazten da, baina ez da haren erregistrorik aurkitzen.
OT Check zerbitzuak ezagutzen den estaldura, falta dena eta hori nork argitu dezakeen dokumentatzen du. Beste proba bat prestatzea komeni den eta zer baldintzatan erabakitzeko balio du. Azterketak ez du proba hori egiten, ezta berreskuratze-denborarik egiaztatzen ere.
Erosle batek segurtasunari buruzko informazioa eskatzen du
Simulazio honetan, prozesu bati buruzko erantzunak hainbat arloren esku daude eta batzuek ez dute dokumentu-euskarririk.
OT Check zerbitzuak irismenean sartutako galderak eskuragarri dauden ebidentziekin eta erantzuteke dauden galderekin lotzen ditu. Zer erantzun daitekeen eta aurretik zer baliozkotu behar den erabakitzen laguntzen du. Ez du homologazioa bermatzen, eta ez du berez enpresa-galdetegi oso bat barne hartzen.
Azaldu zer erabaki behar duzun
Kontsultaren arrazoia eta aztertu nahi duzun prozesua adieraztea nahikoa da. Ez bidali kredentzialik, konfiguraziorik edo informazio sentikorrik. Hogei minutuko elkarrizketa batek OT Check egokia den baloratzeko balio du.
MKDLri idatzi
mysthrala@mkdl.jp
Aholkularitza, dokumentazioa eta prestakuntza Euskaditik.
Lege-oharra (gaztelaniaz)
Pribatutasuna (gaztelaniaz)
Cookieak (gaztelaniaz)
Irisgarritasuna (gaztelaniaz)
Segurtasuna (gaztelaniaz)
© 2026 Mysthrala Kurogane Defense Labs'''.splitlines()

class Texts(HTMLParser):
    def __init__(self):
        super().__init__(); self.texts = []
    def handle_data(self, value):
        if value.strip(): self.texts.append(value)

source = (root / 'index.html').read_text(encoding='utf-8')
p = Texts(); p.feed(source)
assert len(p.texts) == len(translations), (len(p.texts), len(translations))
for old, new in zip(p.texts, translations):
    source = source.replace('>' + old + '<', '>' + html.escape(new, quote=False) + '<', 1)
source = source.replace('lang="es"', 'lang="eu"').replace('https://mkdl.jp/', 'https://mkdl.eus/').replace('es_ES', 'eu_ES')
replacements = {
 'MKDL, inicio': 'MKDL, hasiera', 'Navegación principal': 'Nabigazio nagusia',
 'Información legal': 'Lege-informazioa', 'Información pública en Markdown': 'Informazio publikoa Markdown formatuan',
 'Abrir las dos páginas de decisión y recursos del ejemplo ficticio': 'Fikziozko adibidearen erabaki eta baliabideen bi orriak ireki (gaztelaniaz)',
 'Página del ejemplo: cuatro encargos ordenados con responsable y condición de plazo. Abre el PDF para leerla completa.': 'Adibidearen orria: lau lan antolatuta, arduradunarekin eta epearen baldintzarekin. Ireki PDFa osorik irakurtzeko (gaztelaniaz).',
 'MKDL | OT Check, revisión de un proceso industrial': translations[0],
 'Revisión de un proceso industrial para entregar prioridades, responsables propuestos y comprobaciones con las que encargar mejoras de ciberseguridad.': 'Industria-prozesu baten azterketa: lehentasunak, arduradun-proposamenak eta zibersegurtasun-hobekuntzak eskatzeko egiaztapenak.',
 'OT Check: revisión de un proceso industrial y plan de actuaciones de ciberseguridad.': 'OT Check: industria-prozesu baten azterketa eta zibersegurtasun-jarduketen plana.',
 'Consulta%20sobre%20OT%20Check': 'OT%20Check%20zerbitzuari%20buruzko%20kontsulta',
}
for old, new in replacements.items(): source = source.replace(old, new)
source = source.replace('</head>', '<link rel="alternate" hreflang="es" href="https://mkdl.jp/" />\n<link rel="alternate" hreflang="eu" href="https://mkdl.eus/" />\n</head>')
source = source.replace('<a href="#servicio">OT Check</a>', '<a href="https://mkdl.jp/" lang="es" hreflang="es">Castellano</a><a href="#servicio">OT Check</a>')
(root / 'index.html').write_text(source, encoding='utf-8')
for name in ('CNAME', 'robots.txt', 'sitemap.xml', 'security.txt', '.well-known/security.txt'):
    path = root / name
    path.write_text(path.read_text(encoding='utf-8').replace('mkdl.jp', 'mkdl.eus').replace('mysthrala@mkdl.eus', 'mysthrala@mkdl.jp'), encoding='utf-8')
path = root / 'scripts/package-site.py'
path.write_text(path.read_text(encoding='utf-8').replace('mkdl.jp', 'mkdl.eus'), encoding='utf-8')
