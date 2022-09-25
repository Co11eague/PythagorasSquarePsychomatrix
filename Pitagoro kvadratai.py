import textwrap
from collections import Counter
from functools import partial
from random import *
from time import *
from tkinter import *
from tkinter import messagebox


def skaiciavimai(b, a):
    print(b)
    global phito
    naujas = Toplevel(pg, relief=RAISED, bd=5)
    naujas.geometry("%dx%d%+d%+d" % (800, 300, ilgis / 4, plotis / 4))
    naujas.resizable(False, False)
    naujas.overrideredirect()
    naujas.config(bg="khaki")
    du = Button(naujas, text="X", bg="red", font=("Arial", "17", "bold"), command=naujas.destroy)
    du.pack(side=RIGHT, padx=5)
    a1 = Frame(naujas, bd=5, relief=RIDGE, bg="#F6F6F6");
    a1.pack(side=LEFT, fill=X, expand=True, padx=10)
    Label(a1, bg="#F6F6F6", text=Pitagoras1[b], font=("Times", "30", "bold underline italic")).pack(fill=X)
    Label(a1, bg="#F6F6F6", text=skaiciukai[b], font=("Times", "25", "bold")).pack(fill=X)
    if skaiciukai[b] > 6:
        Label(a1, bg="#F6F6F6", text=viskas[b][6], font=("Times", "15",)).pack(fill=X)
    else:
        Label(a1, bg="#F6F6F6", text=viskas[b][skaiciukai[b]], font=("Times", "15",)).pack(fill=X)


def isejimas():
    ats = messagebox.askyesno("Išėjimas", "Ar norite išeiti iš šios programos?")
    if ats == True:
        pg.destroy()


def kasvyksta():
    global phito
    naujas = Toplevel(pg, relief=RAISED, bd=5)
    naujas.geometry("%dx%d%+d%+d" % (800, 300, ilgis / 4, plotis / 4))
    naujas.resizable(False, False)
    naujas.overrideredirect(True)
    naujas.config(bg="khaki")
    du = Button(naujas, text="X", bg="red", font=("Arial", "17", "bold"), command=naujas.destroy)
    du.pack(side=RIGHT, padx=5)
    a1 = Frame(naujas, bd=5, relief=RIDGE, bg="#F6F6F6");
    a1.pack(side=LEFT, fill=X, expand=True, padx=10)
    Label(a1, bg="#F6F6F6", text="Kaip naudotis?", font=("Times", "30", "bold underline")).pack(fill=X)
    Label(a1, bg="#F6F6F6", font=("Times", "25", "bold"), justify=LEFT,
          text="Norint pasinaudoti Pitagoro išmintimi\nreikia sekti šias instrukcijas:").pack(fill=X)
    Label(a1, bg="#F6F6F6", font=("Times", "20"), justify=LEFT,
          text="> Po Pitagoro akimi - gimimo metai;\n> Pitagoro akies kairėje - gimimo mėnesis;\n> Pitagoro akies dešinėje - gimimo diena;\n> Tik paspaudus Pitagoro akį jis pasinaudos savo išmintimi.").pack()


def tikrinuimas(*args):
    if str(a5.get()).isnumeric() == False:
        a5.set("")


def dirbame():
    global af
    global skaiciukai
    global skaiciukai1
    skaiciukai1 = []
    Pitagoromasyvas.append(a1.get() // 10)
    Pitagoromasyvas.append(a1.get() % 10)
    Pitagoromasyvas.append(a2.get() // 10)
    Pitagoromasyvas.append(a2.get() % 10)
    Pitagoromasyvas.append(int(a5.get()) // 1000)
    Pitagoromasyvas.append((int(a5.get()) % 1000) // 100)
    Pitagoromasyvas.append((int(a5.get()) % 100) // 10)
    Pitagoromasyvas.append(int(a5.get()) % 10)
    a = sum(Pitagoromasyvas)
    Pitagoromasyvas.append(a // 10)
    Pitagoromasyvas.append(a % 10)
    Pitagoromasyvas.append((Pitagoromasyvas[8] + Pitagoromasyvas[9]) // 10)
    Pitagoromasyvas.append((Pitagoromasyvas[8] + Pitagoromasyvas[9]) % 10)
    if Pitagoromasyvas[0] == 0:
        Pitagoromasyvas.append(abs(a - Pitagoromasyvas[1] * 2) // 10)
        Pitagoromasyvas.append(abs(a - Pitagoromasyvas[1] * 2) % 10)
    else:
        Pitagoromasyvas.append(abs(a - Pitagoromasyvas[0] * 2) // 10)
        Pitagoromasyvas.append(abs(a - Pitagoromasyvas[0] * 2) % 10)
    Pitagoromasyvas.append((Pitagoromasyvas[12] + Pitagoromasyvas[13]) // 10)
    Pitagoromasyvas.append((Pitagoromasyvas[12] + Pitagoromasyvas[13]) % 10)
    print(Pitagoromasyvas)
    alo = Counter(Pitagoromasyvas)
    print(alo)
    drobe.delete(button1_window)
    for x in range(100):
        drobe.move(button2_window, 0, -(plotis / 2 / 100))
        drobe.move(entry_window, 0, (plotis / 2 / 100))
        drobe.move(option_window, -(ilgis / 2 / 100), 0)
        drobe.move(option_window1, (ilgis / 2 / 100), 0)
        sleep(0.005)
        pg.update()
    for y in range(4):
        for x in range(4):
            drobe.tag_bind(namespace['Kvadratas_%d' % ((x + 1) + y * 4)], "<Button-1>",
                           partial(skaiciavimai, (x * 4 + y)))
            drobe.tag_bind(namespace['Tekstas_%d' % ((x + 1) + y * 4)], "<Button-1>",
                           partial(skaiciavimai, (x * 4 + y)))

            drobe.pack()
            x1 = drobe.coords(namespace['Kvadratas_%d' % ((x + 1) + y * 4)])[0]
            y1 = drobe.coords(namespace['Kvadratas_%d' % ((x + 1) + y * 4)])[1]
            x2 = drobe.coords(namespace['Tekstas_%d' % ((x + 1) + y * 4)])[0]
            y2 = drobe.coords(namespace['Tekstas_%d' % ((x + 1) + y * 4)])[1]
            for m in range(100):
                drobe.move(namespace['Tekstas_%d' % ((x + 1) + y * 4)], ((ilgis / 2.65 + x * dydis * 3) - x1) / 100,
                           ((plotis / 5 + y * dydis * 3) - y1) / 100)
                drobe.move(namespace['Kvadratas_%d' % ((x + 1) + y * 4)], ((ilgis / 2.65 + x * dydis * 3) - x1) / 100,
                           ((plotis / 5 + y * dydis * 3) - y1) / 100)
                pg.update()
                sleep(0.001)
    for ol in range(3):
        o = 0 if alo.get(1 + 3 * ol) == None else alo.get(1 + 3 * ol)
        skaiciukai.append(o)
        drobe.itemconfig(namespace['Tekstas_%d' % (ol + 1)], text=Pitagoras[ol] + "\n" + str(o))
        o = 0 if alo.get(2 + 3 * ol) == None else alo.get(2 + 3 * ol)
        skaiciukai.append(o)
        drobe.itemconfig(namespace['Tekstas_%d' % (ol + 5)], text=Pitagoras[ol + 4] + "\n" + str(o))
        o = 0 if alo.get(3 + 3 * ol) == None else alo.get(3 + 3 * ol)
        skaiciukai.append(o)
        drobe.itemconfig(namespace['Tekstas_%d' % (ol + 9)], text=Pitagoras[ol + 8] + "\n" + str(o))
    for lol in range(3):
        print('Tekstas_%d' % (4 + lol * 4), 'Tekstas_%d' % (lol + 13))
        o = skaiciukai[lol] + skaiciukai[lol + 3] + skaiciukai[lol + 6]
        o1 = skaiciukai[lol * 3] + skaiciukai[lol * 3 + 1] + skaiciukai[lol * 3 + 2]
        skaiciukai1.append(o)
        skaiciukai1.append(o1)
        drobe.itemconfig(namespace['Tekstas_%d' % (4 + lol * 4)], text=Pitagoras[3 + 4 * lol] + "\n" + str(o))
        drobe.itemconfig(namespace['Tekstas_%d' % (lol + 13)], text=Pitagoras[lol + 12] + "\n" + str(o1))
    skaiciukai1.append(skaiciukai[0] + skaiciukai[4] + skaiciukai[8])
    drobe.itemconfig(Tekstas_16, text=Pitagoras[15] + "\n" + str(skaiciukai1[-1]))
    for x in range(3):
        skaiciukai.insert(x * 4 + 3, skaiciukai1[x * 2 + 1])
        skaiciukai.insert(x + 12, skaiciukai1[x * 2])
    skaiciukai.append(skaiciukai1[-1])
    af = False
    print(skaiciukai)
    so = skaiciukai[2] + skaiciukai[5] + skaiciukai[8]
    if skaiciukai[-1] == so:
        Dvasingumas[skaiciukai[-1]] += "\nDvasinis ir meterialus gyvenimas subalansuoti."
    elif skaiciukai[-1] > so:  # Lape rašo kad tokiu atveju turėtų būti linkės į materialų, bet tas yra nelogiška.
        Dvasingumas[skaiciukai[-1]] += "\nLinkęs į dvasinį gyvenimą."
    else:
        Dvasingumas[skaiciukai[-1]] += "\nLinkęs į materialų gyvenimą."


skaiciukai = []
wrapper = textwrap.TextWrapper(width=80)
Charakteris = ["Egoistas tik „aš turiu gyventi“",
               "Labai minkštas charakteris, labai mėgsta būti giriamas ir bet kokias būdais tai stengiasi pasiekti",
               "Nuoširdus, nusileidžiantis – „auksinis viduriukas“, kas iš karto jį išskiria iš kitų. Suranda su bet kokiu žmogumi bendrą kalbą",
               "Labai valingas ir stiprus charakteris. Mėgsta ir moka sau pastatyti tikslus. Tai lyderio charakteris, kuris visada nori būti geresnis už kitus",
               "Maksimaliai išreikštas valdžios troškimas. Visada įsitikinęs savo tiesa, labai mažai įsiklauso į kitų nuomonę ir patarimus",
               "Žmogus pradeda bijoti savo stipraus noro vadovauti ir slepia šį norą. Labai retais atvejais gali būti labai žiaurus, dažniausiai pakenčiamas, ramus, emocijų pliūpsnis pasireiškia po ilgo nuoskaudų kaupimo",
               "Žmogus pradeda bijoti savo stipraus noro vadovauti ir slepia šį norą. Labai retais atvejais gali būti labai žiaurus, dažniausiai pakenčiamas, ramus, emocijų pliūpsnis pasireiškia po ilgo nuoskaudų kaupimo"]
Energija = [
    "Labai silpna energija. Pasižymi darbuose ir mokymuose tingumu, nepamatuotu blaškymusi, konfliktų bijojimu. Stengiasi nesivelti į ginčus ir pykčius bet labai mėgsta būti jų liudininku",
    "Žmogui energijos deficitas. Labai dažnai toks žmogus tampa nenuorama, tinginiauja pasirinkdamas tinginio zonas, kuriose jis gali atsipalaiduoti ir pailsėti. Vengia konfliktų, kadangi nemėgsta naudoti energiją tokiems dalykams",
    "Tai norma, kuri reikalinga kiekvienam žmogui. Labai gera energetika, kuri palanki bet kokiam kontaktui su žmonėmis ir darbui. Bendraujantis, kontaktuojantis, labai geras pasakotojas, lektorius ir oratorius. Pagal savo energiją – gydytojas",
    "Savybės: uždaras, nenoras dalytis su kitais savo problemomis, spaudžiant iš išorės emocijų pliūpsniai, sugebėjimas esant būtinybei padėti kitam žmogui. Kadangi labai intensyviai sugeria kitų energiją, labai dažnai stengiasi kompanijoje būti centrine kompanijos figūra",
    "Žmogus turi perteklių energijos ir gali sau leisti ją naudoti pagal savo nuožiūrą – tai „donoras‘. Geriausiai savo jėgas išbandyti sporte, medicinoje, pedagogikoje, fizinėje veikloje",
    "Žmogus turi perteklių energijos ir gali sau leisti ją naudoti pagal savo nuožiūrą – tai „donoras‘. Geriausiai savo jėgas išbandyti sporte, medicinoje, pedagogikoje, fizinėje veikloje",
    "Žmogus turi perteklių energijos ir gali sau leisti ją naudoti pagal savo nuožiūrą – tai „donoras‘. Geriausiai savo jėgas išbandyti sporte, medicinoje, pedagogikoje, fizinėje veikloje"]
Mokslai = [
    "Polinkis humanitariniams, filosofiniams, meno mokslams. Techniką priima paviršutiniškai pagal išorinį vaizdą – pagal principą gražu, dailu",
    "Žmogus turi tokią nuostatą – noriu – darau, nenoriu – nedarau. Gali užsiimti bet kokias mokslais, kadangi nuo humanitarinių nenutolo, o prie tiksliųjų mokslų dar neprisišliejo. Gali surasti optimalų variantą ir užsiimti mokslais, kurie yra tarp šių žinių sričių; (ekonomika, teisė, gamtos mokslai)",
    "Sugebėjimai tiksliesiems mokslams (matematika, fizika, chemija) ir technikai",
    "Labai charakteringas pedantiškumas, tvarkingumas. Optimaliausios tos žinių sritys, kurios naudojasi tiksliaisiais mokslais, tačiau yra ant susiliejimo su kitais mokslais : matematinė lingvistika, kompiuterinė technika, bionika",
    "Turi labai stiprų susidomėjimą mokslais ir technika. Galima pasakyti, kad žmogus gimęs būti konstruktoriumi, išradėju",
    "Turi labai stiprų susidomėjimą mokslais ir technika. Galima pasakyti, kad žmogus gimęs būti konstruktoriumi, išradėju",
    "Turi labai stiprų susidomėjimą mokslais ir technika. Galima pasakyti, kad žmogus gimęs būti konstruktoriumi, išradėju"]
Sveikata = ["Labai silpna sveikata. Visai neturi potraukio fiziniam darbui",
            "Sveikata nebloga, tačiau nepakankamai stipri, kad nebūtų kalbama apie jos stiprinimą ir profilaktiką",
            "Sveikata nebloga, gražus, stiprus kūnas, sangviniko temperamentas. Gali drąsiai užsiimti sportu, net profesionaliai. Fizinis darbas taip pat nepamaišys",
            "Labai gerai sveikata, geri fiziniai duomenys. Linkęs ginčus spręsti jėga",
            "Labai gerai sveikata, geri fiziniai duomenys. Linkęs ginčus spręsti jėga",
            "Labai gerai sveikata, geri fiziniai duomenys. Linkęs ginčus spręsti jėga",
            "Labai gerai sveikata, geri fiziniai duomenys. Linkęs ginčus spręsti jėga"]
Logika = [
    "Nesinaudoja logika, svajotojas, pastoviai skraido padebesiais. Patartina pasirinkti humanitarinę veiklą arba dailę, tačiau ne techniką ar tiksliuosius mokslus. Nesiginčykite su jais, nes įžeisite, tačiau neįtikinsite",
    "Logika yra, tačiau ji labai silpna. Žmogus – svajoklis",
    "Gerai išvystyta intuicija (geri tyrėjai, juristai), stipri logika, polinkis tiksliesiems mokslams ir technikai. Labai gerai planuoja ateitį",
    "Kai kuriais atvejais gali pasireikšti aiškiaregystės požymis, tačiau tuo dažniausiai nepatikima ir jo spėjimai pasidaro nerealūs. Gerai išmano matematiką, techniką, bet kaip taisyklė pasirenka labai siaurą specialybę, kurią labai kruopščiai įsisavina",
    "Beveik neklysta prognozėse. Gali pranašauti ateitį", "Beveik neklysta prognozėse. Gali pranašauti ateitį",
    "Beveik neklysta prognozėse. Gali pranašauti ateitį"]
Fizinis = [
    "Neturi jokio potraukio fiziniam darbui. Tai meno žmogus ir gryno mokslo. Fizinio darbo nemėgsta ir juo užsiima tik esant reikalui, arba jei jaučiasi skolingas",
    "Žmogus atėjo į šį pasaulį gauti žemišką profesiją, jam būtinas fizinis darbas. Tačiau juo užsiima tik tada, kai yra noras",
    "„Auksinės rankos“, daro bet kokius darbus, tačiau reikalingas intelektualinis vystymasis. Labai reikia vystyti susidomėjimą daile, mokslu arba energijos nereikalaujančiam verslui: juvelyrika, mezgimui, audimui ir t. t. Reikalingi geri pavyzdžiai, nes linkęs daug ką kopijuoti",
    "Magiškai patrauklus, su nepakartojimu temperamentui", "Jam nėra nežinomo fizinio darbo, viskas žinoma ir įprasta",
    "Jam nėra nežinomo fizinio darbo, viskas žinoma ir įprasta",
    "Jam nėra nežinomo fizinio darbo, viskas žinoma ir įprasta"]
Sekme = [
    "„Laisvas menininkas“, savęs neapkrauna konkrečiais uždaviniais, kuriuos prieš jį pateikia gyvenimas. Nėra konkretaus talento, kuris reikalauja realizacijos, pats pasirenka vystymosi kryptį ir realizuojasi šiose sferoje",
    "Nedidelis pasisekimas, talentas yra, tačiau nelabai išryškintas. Žmogus dalinai apsaugotas nuo nesėkmių ir atsitiktinumo",
    "Žmogus, kuriam „sekasi“. Likimas jį stumia reikiama kryptimi. Jis turi galimybę rizikuoti ir prieš save stato gana aukštus tikslus",
    "Ypatingai talentingas žmogus, kurį galima pavadinti gyvenimo „inžinieriumi“ arba „konstruktoriumi“. Patys to nežinodami, daro įtaką kitiems per pageidavimus, pojūčius, nuojautą. Apie save surenka aktyvius, stiprius žmones, analizuoja situacijas, daro išvadas ir mintyse priima sprendimus. Turint daug septintukų geriausiai užsiimti mokslu arba pasirinkti profesijas, kurios surištos su žmonėmis – gydytojo, mokytojo, psichologo",
    "Ypatingai talentingas žmogus, kurį galima pavadinti gyvenimo „inžinieriumi“ arba „konstruktoriumi“. Patys to nežinodami, daro įtaką kitiems per pageidavimus, pojūčius, nuojautą. Apie save surenka aktyvius, stiprius žmones, analizuoja situacijas, daro išvadas ir mintyse priima sprendimus. Turint daug septintukų geriausiai užsiimti mokslu arba pasirinkti profesijas, kurios surištos su žmonėmis – gydytojo, mokytojo, psichologo",
    "Ypatingai talentingas žmogus, kurį galima pavadinti gyvenimo „inžinieriumi“ arba „konstruktoriumi“. Patys to nežinodami, daro įtaką kitiems per pageidavimus, pojūčius, nuojautą. Apie save surenka aktyvius, stiprius žmones, analizuoja situacijas, daro išvadas ir mintyse priima sprendimus. Turint daug septintukų geriausiai užsiimti mokslu arba pasirinkti profesijas, kurios surištos su žmonėmis – gydytojo, mokytojo, psichologo"]
Pareiga = ["Neturi pareigos jausmo, nepakenčia iš kitų spaudimo",
           "Labai stipriai pasireiškia nuosavybės jausmas. Pareigos ir kantrybės jausmas yra, tačiau silpnai išvystytas. Labai dažnai turi nuoskaudą tėvams",
           "Labai didelis atsakingumo jausmas, visada stengiasi padėti kitiems. Juo galima naudotis, tačiau neapgauti. Visada jaučia melą ir apie tai nekalba tik dėl to, kad yra kantrus ir gailestingas. Geriausiai pasirinkti tokią profesiją, kuri surišta su žmogumi",
           "Liaudžiai tarnaujančio ženklas. Žmogus pasiaukojantis, nuoširdus, kantrus, visada prisimenantis tėvus, tačiau tuo pačiu gali būti nuožmus teisybės ieškotojas, einantis „per lavonus“ (pareiga aukščiau už nuoširdumą)",
           "Gebėjimas studijuoti tiksliuosius mokslus", "Gebėjimas studijuoti tiksliuosius mokslus",
           "Gebėjimas studijuoti tiksliuosius mokslus"]
Protas = ["Užmirštukas, reikia pastoviai lavinti atmintį, padėti priimti sprendimus, nes jie gali būti neprotingi",
          "Užmirštukas, nepiktybinis. Turi atkreipti dėmesį į savo sugebėjimų vystymą",
          "Gera atmintis, nuo gimimo protinga galva, bet to maža, reikia mokytis",
          "Puiki, tačiau nestabili atmintis. Šiam žmogui viskas sekasi",
          "Labai gerai jaučia pasaulį, turi labai retą protą ir atmintį, tačiau jam priskiriamas grubumas",
          "Labai gerai jaučia pasaulį, turi labai retą protą ir atmintį, tačiau jam priskiriamas grubumas",
          "Labai gerai jaučia pasaulį, turi labai retą protą ir atmintį, tačiau jam priskiriamas grubumas"]
Nuomone = [
    "Žmogus neturi tikslų ir uždavinių, visada pasikliauja atsitiktinumu arba kitais žmonėmis, jį labai lengva priversti atsisakyti savo planų  ir pakeisti savo nuomonę",
    "Labai silpnas tikslo siekimas. Žmogus gali įsiterpti į ginčą, tačiau tai nereiškia, kad jis nori pasiekti kažkokio rezultato, tai tik noras pasiekti pergalę ginče. Pasikliauja atsitiktinumu ir draugais",
    "Normalus tikslo siekimas. Žmogus palengva „įsibėgėja“ gyvenime. Pradžioje sužino savo galimybes ir tik po to sau pradeda kelti tikslus",
    "Žmogus gali keisti savo tikslus nenuspėjamai. Labai dažnai pasirinkimas nepateisinamas ir nepaaiškinamas",
    "Stiprus tikslo siekimas. Pradžioje pastatomas tikslas, tik po to pradeda palyginti savo galimybes ir interesą tam tikslui. Dažniausiai pasiekia tuos tikslus, kurie neatitinka jo interesus arba galimybes",
    "Labai stiprus tikslo siekimas. Tai reiškia, kad turėdamas prieš save tikslus, jis gali užmiršti, kad su juo yra žmonės, artimieji, giminės – jis gali daug daugiau prarasti, tačiau tikslą pasieks. Būtina kontroliuoti veiksmus siekiant tikslo",
    "Žmogus sau stato užaukštintus tikslus arba keletą tikslų vienu metu, o tai stabdo jo ėjimą į priekį"]
Seima = [
    "Ne šeimos žmogus, tai reiškia, kad jam šeima paskutinėje vietoje. Tokius žmones labiausiai domina karjera, draugai, darbas",
    "Žmogus supranta, kad šeimą reikia sukurti, tačiau jokių pastangų tam neteikia, laukia, kad tai įvyktų savaime",
    "Žmogus supranta, kad šeimą reikia sukurti, tačiau jokių pastangų tam neteikia, laukia, kad tai įvyktų savaime",
    "Žmogus mėtosi tarp didelio noro bet kokia kaina sukurti šeimą ir nenoru to daryti",
    "Žmogus nori sukurti šeimą ir tai daro nedelsdamas",
    "Labai stipri šeimos žmogaus savybė. Tokie žmonės stengiasi sukurti idealią savo šeimą, ko pasėkoje kelia per didelius jai reikalavimus. Be šeimos neįsivaizduoja savo egzistavimo",
    "Labai ilgai ieško savo idealo, o tai priveda prie stabdymo šeimos kūrimo"]
Stabilumas = ["Stengiasi visus ir viską aplink (aplinką, darbo vietą) save keisti",
              "Stengiasi visus ir viską aplink (aplinką, darbo vietą) save keisti",
              "Labai lengvai pakyla, bet sugeba (esant norui) suvaldyti savo revoliucinius išsišokimus",
              "Nestabilus įpročiuose: gali inicijuoti daugelį įpročių ir prisirišimų, sukurdamas tuo pačiu stabilumą, tačiau labai lengvai nuo jų atsisako, nenurodydamas priežasčių. Po kiek laiko vėl gali reanimuoti užmirštus prisirišimus",
              "Labai stabilus, save apgaubdamas įvairiais prisirišimais ir įpročiais, tuo pačių susikuria sau stabilią aplinką. Gali būti truputį įkyrus. Labai sunkiai susitaiko su pasikeitimais",
              "Labai stabilus, save apgaubdamas įvairiais prisirišimais ir įpročiais, tuo pačių susikuria sau stabilią aplinką. Gali būti truputį įkyrus. Labai sunkiai susitaiko su pasikeitimais.",
              "Stengiasi save apgaubti pertekliniais įpročiais, kuriuos pats pradeda keisti, kai jie jam pradeda maišyti"]
Vertinimas = ["Savęs įvertinimas žemas, labai dažnai nepasitiki savimi",
              "Savęs įvertinimas žemas, labai dažnai nepasitiki savimi",
              "Savęs įvertinimas žemas, labai dažnai nepasitiki savimi",
              "Savęs įvertinimas žemas, labai dažnai nepasitiki savimi",
              "Stiprus savęs vertinimas, stengiasi išsiskirti iš bendros masės, tam skirdamas daug jėgos",
              "Labai stiprus savęs vertinimas, gali būti per didelis, jei žmogus netobulėja, o save vertina tik pagal potencialias galimybes, hiperbolizuojant jas",
              "Pervertinimas, priveda prie to, kad norėdamas save parodyti, užmiršta tikrąsias savo galimybes, užsiima išorine forma, nekreipdamas dėmesio į vidinį turinį. Tokie žmonės, kaip taisyklė, nepasiekia savo tikslų, išnaudoja savo jėgas norėdami pasirodyti miniai, kuri žavisi jo išore"]
Aprupinimas = ["Nesistengia savęs apsirūpinti, gali sėdėti ant ko nors (tėvų, žmonos, vyro, valstybės) „sprando“",
               "Nesistengia savęs apsirūpinti, gali sėdėti ant ko nors (tėvų, žmonos, vyro, valstybės) „sprando“",
               "Žino, kad reikia maitinti šeimą, ir to bijodamas, profesijos ieško pagal atlyginimą. Gali atsisakyti svajonės, dėl stabilaus uždarbio. Jeigu yra galimybė to nedaryti, tai visai nesispyrioja, kadangi visai netrokšta maitinti save ir šeimą",
               "Materialiniu aprūpinimu užsiima impulsyviai. Jo principas – greitai užsidirbti ir kažkurį laiką tuo nesirūpinti. Ir taip nuo vienos progos prie kitos progos",
               "Labai didelę laiko dalį skiria materialiam šeimos aprūpinimui, labai dažnai tai lieka viso gyvenimo tikslu",
               "Labai didelę laiko dalį skiria materialiam šeimos aprūpinimui, labai dažnai tai lieka viso gyvenimo tikslu",
               "Pradeda labai intensyviai dirbti, kas priveda prie greito susidėvėjimo ir pilno nusišalinimo nuo darbo. Dirba daug įvairių darbų, persitempia ir kuria iliuziją, kad dirba"]
Talentas = ["Talentu nepasižymi, todėl turi turėti mėgstamą užsiėmimą",
            "Talentu nepasižymi, todėl turi turėti mėgstamą užsiėmimą", "Talentą privalo vystyti",
            "Talentą privalo vystyti", "Talentą privalo vystyti", "Talento per daug, reikia turėti kelis pomėgius",
            "Talento per daug, reikia turėti kelis pomėgius"]
Dvasingumas = ["Neturi jokio dvasingumo. Reikia stengtis vystyti", "Neturi jokio dvasingumo. Reikia stengtis vystyti",
               "Dvasingumą reikia vystyti", "Dvasingumą reikia vystyti", "Dvasingumą reikia vystyti",
               "Labai dažnai linksta į fanatizmą ir nepripažįsta kitokio požiūrio",
               "Labai dažnai linksta į fanatizmą ir nepripažįsta kitokio požiūrio"]
Temperamentas = ["„Šaltas“ žmogus. Nesijaudina dėl smulkmenų", "„Šaltas“ žmogus. Nesijaudina dėl smulkmenų",
                 "Normalus temperamentas", "Normalus temperamentas", "Stiprus temperamentas",
                 "Temperamento pikas, reikalingas susižavėjimas",
                 "Persitempimas, stengiamasis siekti įvairumo labai aktyviai, pametant nuovoką ir saiką. Tai priveda prie šaltumo dėl pastovaus nepasitenkinimo"]
viskas = [Charakteris, Energija, Mokslai, Vertinimas, Sveikata, Logika, Fizinis, Aprupinimas, Sekme, Pareiga, Protas,
          Talentas, Nuomone, Seima, Stabilumas, Dvasingumas, Temperamentas]
for m in range(len(viskas)):
    for n in range(len(viskas[m])):
        viskas[m][n] = wrapper.fill(text=viskas[m][n] + ".")

Pitagoromasyvas = []
pg = Tk();
ilgis = pg.winfo_screenwidth();
plotis = pg.winfo_screenheight();
pg.geometry("%dx%d" % (ilgis, plotis));
pg.config(background="#FFFFFE");
pg.resizable(False, False);
pg.attributes("-fullscreen", True)
d2 = Button(pg, text="X", font=("Arial", "17", "bold"), bg="red", command=isejimas)
d2.place(x=ilgis - 36, y=0)
Label(pg, text="Pitagoro kvadratai", bg="#FFFFFE", font=("Times", "36", "bold underline")).pack(pady=plotis / 20)
drobe = Canvas(pg, bg="#FFFFFE", bd=0, highlightthickness=0)
drobe.pack(expand=1, fill=BOTH)
dydis = 38
Koordinates1 = []
for x in range(1, 6):
    labas = []
    labas.append((ilgis / 2 + dydis - dydis * 2 * (x - 1)) - (x - 1) * 20)
    labas.append(dydis * 2 * (x - 1) + x * 20)
    labas.append(ilgis / 2 + dydis - dydis * 2 * x - (x - 1) * 20)
    labas.append(dydis * 2 * x + x * 20)
    Koordinates1.append(labas)
for x in range(1, 5):
    mas = []
    k = 0
    for x1 in range(4):
        if k == 0:
            mas.append(Koordinates1[x][x1] + (ilgis / 2 - Koordinates1[x][x1]) * 2)
        elif k == 2:
            mas.append(Koordinates1[x][x1] + (ilgis / 2 - Koordinates1[x][x1]) * 2)
        else:
            mas.append(Koordinates1[x][x1])
        k += 1
    Koordinates1.append(mas)
visas = 7
for x in [[1, 5], [2, 6], [3, 7]]:
    visas -= 2
    for x2 in x:
        mas = []
        k = 0
        for x1 in range(4):
            if k == 1:
                mas.append(Koordinates1[x2][x1] + 20 * (visas + 1) + dydis * 2 * visas + dydis * 2)
            elif k == 3:
                mas.append(Koordinates1[x2][x1] + 20 * (visas + 1) + dydis * 2 * visas + dydis * 2)
            else:
                mas.append(Koordinates1[x2][x1])
            k += 1
        Koordinates1.append(mas)
mas = []
k = 0
for x in Koordinates1[0]:
    if k == 1:
        mas.append(x + 20 * (7 + 1) + dydis * 2 * 7 + dydis * 2)
    elif k == 3:
        mas.append(x + 20 * (7 + 1) + dydis * 2 * 7 + dydis * 2)
    else:
        mas.append(x)
    k += 1
Koordinates1.append(mas)
Koordinates1[0], Koordinates1[1], Koordinates1[2], Koordinates1[3], Koordinates1[4], Koordinates1[5], Koordinates1[6], \
Koordinates1[7], Koordinates1[8], Koordinates1[9], Koordinates1[10], Koordinates1[11], Koordinates1[12], Koordinates1[
    13], Koordinates1[14], Koordinates1[15] = Koordinates1[0], Koordinates1[5], Koordinates1[6], Koordinates1[7], \
                                              Koordinates1[8], Koordinates1[14], Koordinates1[12], Koordinates1[10], \
                                              Koordinates1[15], Koordinates1[9], Koordinates1[11], Koordinates1[13], \
                                              Koordinates1[4], Koordinates1[3], Koordinates1[2], Koordinates1[1]
info = PhotoImage(file="output_XXsKbL.gif")
info1 = PhotoImage(file="ezgif.com-gif-maker.gif")
info = info.subsample(4)
info1 = info1.subsample(2)
a1 = IntVar()
d1 = Button(pg, image=info, bd=0, highlightthickness=0, command=dirbame)
d1.pack()
d1.image = info
a5 = StringVar()
button1_window = drobe.create_window(Koordinates1[11][0] + dydis * 2.5, Koordinates1[3][1], anchor=NW, window=d1)
d2 = Button(pg, image=info1, bd=0, highlightthickness=0, command=kasvyksta)
d2.pack()
d2.image = info1
button2_window = drobe.create_window(ilgis / 2 - dydis * 1.25, Koordinates1[3][1] - dydis * 2, anchor=NW, window=d2)
d3 = Entry(pg, font=("Arial", 25, "bold"), textvariable=a5, relief=RIDGE, bd=5, width=4, justify=CENTER, )
d3.pack()
d3.bind("<KeyRelease>", tikrinuimas)
entry_window = drobe.create_window(ilgis / 2 - dydis * 1.25, Koordinates1[3][1] + dydis * 6.25, anchor=NW, window=d3)
a2 = IntVar()
d4 = OptionMenu(pg, a2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
d4.config(font=("Arial", 25, "bold"), textvariable=a2, relief=RIDGE, bd=5)
d4.pack()
option_window = drobe.create_window(ilgis / 2 - dydis * 6.5, Koordinates1[3][1] + dydis * 2, anchor=NW, window=d4)
d5 = OptionMenu(pg, a1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29, 30, 31)
d5.config(font=("Arial", 25, "bold"), textvariable=a1, relief=RIDGE, bd=5)
d5.pack()
option_window1 = drobe.create_window(ilgis / 2 + dydis * 4.25, Koordinates1[3][1] + dydis * 2, anchor=NW, window=d5)
a1.set("1")
a2.set("1")
k = 0
for x in [0, 8, 9, 10, 11, 12, 13, 14, 15]:
    Koordinates1[x][0], Koordinates1[x][2] = Koordinates1[x][0] - dydis * 2, Koordinates1[x][2] + dydis * 2
namespace = globals()
Tekstokoord = []
Pitagoras = ["Charakteris", "Sveikata", "Sėkmė", "Tikslas", "Energija", "Logika", "Pareiga", "Šeima", "Mokslas",
             "Darbštumas", "Protas", "Įpročiai", "Savęs\nįvertinimas", "Darbas", "Talentas", "Dvasingumas"]
# Žinau reikėjo perdaryti tą patį, tačiau tą reikėjo suprasti anksčiau, ne tada kai programa beveik padaryta.
Pitagoras1 = ["Charakteris", "Energija", "Mokslas", "Savęs\nįvertinimas", "Sveikata", "Logika", "Darbštumas", "Darbas",
              "Sėkmė", "Pareiga", "Protas", "Talentas", "Tikslas", "Šeima", "Įpročiai", "Dvasingumas"]

for x in range(16):
    Tekstokoord.append([Koordinates1[x][0] + (Koordinates1[x][2] - Koordinates1[x][0]) / 2,
                        Koordinates1[x][1] + (Koordinates1[x][3] - Koordinates1[x][1]) / 2])
for x in range(1, 17):
    namespace['Kvadratas_%d' % x] = drobe.create_rectangle(Koordinates1[x - 1], width=3, fill=(
                "#%02x%02x%02x" % (randint(130, 255), randint(130, 255), randint(130, 255))))
    namespace['Tekstas_%d' % x] = drobe.create_text(Tekstokoord[x - 1], justify=CENTER, text=Pitagoras[x - 1],
                                                    font=("Arial", 9))
x = 0
af = True
while af == True:
    for y in range(1000):
        if af == False:
            break
        drobe.move(Kvadratas_1,
                   (Koordinates1[(x + 1) % len(Koordinates1)][0] - Koordinates1[x % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 1) % len(Koordinates1)][1] - Koordinates1[x % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_1,
                   (Tekstokoord[(x + 1) % len(Tekstokoord)][0] - Tekstokoord[x % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 1) % len(Tekstokoord)][1] - Tekstokoord[x % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_2,
                   (Koordinates1[(x + 2) % len(Koordinates1)][0] - Koordinates1[(x + 1) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 2) % len(Koordinates1)][1] - Koordinates1[(x + 1) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_2,
                   (Tekstokoord[(x + 2) % len(Tekstokoord)][0] - Tekstokoord[(x + 1) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 2) % len(Tekstokoord)][1] - Tekstokoord[(x + 1) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_3,
                   (Koordinates1[(x + 3) % len(Koordinates1)][0] - Koordinates1[(x + 2) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 3) % len(Koordinates1)][1] - Koordinates1[(x + 2) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_3,
                   (Tekstokoord[(x + 3) % len(Tekstokoord)][0] - Tekstokoord[(x + 2) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 3) % len(Tekstokoord)][1] - Tekstokoord[(x + 2) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_4,
                   (Koordinates1[(x + 4) % len(Koordinates1)][0] - Koordinates1[(x + 3) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 4) % len(Koordinates1)][1] - Koordinates1[(x + 3) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_4,
                   (Tekstokoord[(x + 4) % len(Tekstokoord)][0] - Tekstokoord[(x + 3) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 4) % len(Tekstokoord)][1] - Tekstokoord[(x + 3) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_5,
                   (Koordinates1[(x + 5) % len(Koordinates1)][0] - Koordinates1[(x + 4) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 5) % len(Koordinates1)][1] - Koordinates1[(x + 4) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_5,
                   (Tekstokoord[(x + 5) % len(Tekstokoord)][0] - Tekstokoord[(x + 4) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 5) % len(Tekstokoord)][1] - Tekstokoord[(x + 4) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_6,
                   (Koordinates1[(x + 6) % len(Koordinates1)][0] - Koordinates1[(x + 5) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 6) % len(Koordinates1)][1] - Koordinates1[(x + 5) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_6,
                   (Tekstokoord[(x + 6) % len(Tekstokoord)][0] - Tekstokoord[(x + 5) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 6) % len(Tekstokoord)][1] - Tekstokoord[(x + 5) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_7,
                   (Koordinates1[(x + 7) % len(Koordinates1)][0] - Koordinates1[(x + 6) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 7) % len(Koordinates1)][1] - Koordinates1[(x + 6) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_7,
                   (Tekstokoord[(x + 7) % len(Tekstokoord)][0] - Tekstokoord[(x + 6) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 7) % len(Tekstokoord)][1] - Tekstokoord[(x + 6) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_8,
                   (Koordinates1[(x + 8) % len(Koordinates1)][0] - Koordinates1[(x + 7) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 8) % len(Koordinates1)][1] - Koordinates1[(x + 7) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_8,
                   (Tekstokoord[(x + 8) % len(Tekstokoord)][0] - Tekstokoord[(x + 7) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 8) % len(Tekstokoord)][1] - Tekstokoord[(x + 7) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_9,
                   (Koordinates1[(x + 9) % len(Koordinates1)][0] - Koordinates1[(x + 8) % len(Koordinates1)][0]) / 1000,
                   (Koordinates1[(x + 9) % len(Koordinates1)][1] - Koordinates1[(x + 8) % len(Koordinates1)][1]) / 1000)
        drobe.move(Tekstas_9,
                   (Tekstokoord[(x + 9) % len(Tekstokoord)][0] - Tekstokoord[(x + 8) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 9) % len(Tekstokoord)][1] - Tekstokoord[(x + 8) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_10, (
                    Koordinates1[(x + 10) % len(Koordinates1)][0] - Koordinates1[(x + 9) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 10) % len(Koordinates1)][1] - Koordinates1[(x + 9) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_10,
                   (Tekstokoord[(x + 10) % len(Tekstokoord)][0] - Tekstokoord[(x + 9) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 10) % len(Tekstokoord)][1] - Tekstokoord[(x + 9) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_11, (
                    Koordinates1[(x + 11) % len(Koordinates1)][0] - Koordinates1[(x + 10) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 11) % len(Koordinates1)][1] - Koordinates1[(x + 10) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_11,
                   (Tekstokoord[(x + 11) % len(Tekstokoord)][0] - Tekstokoord[(x + 10) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 11) % len(Tekstokoord)][1] - Tekstokoord[(x + 10) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_12, (
                    Koordinates1[(x + 12) % len(Koordinates1)][0] - Koordinates1[(x + 11) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 12) % len(Koordinates1)][1] - Koordinates1[(x + 11) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_12,
                   (Tekstokoord[(x + 12) % len(Tekstokoord)][0] - Tekstokoord[(x + 11) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 12) % len(Tekstokoord)][1] - Tekstokoord[(x + 11) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_13, (
                    Koordinates1[(x + 13) % len(Koordinates1)][0] - Koordinates1[(x + 12) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 13) % len(Koordinates1)][1] - Koordinates1[(x + 12) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_13,
                   (Tekstokoord[(x + 13) % len(Tekstokoord)][0] - Tekstokoord[(x + 12) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 13) % len(Tekstokoord)][1] - Tekstokoord[(x + 12) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_14, (
                    Koordinates1[(x + 14) % len(Koordinates1)][0] - Koordinates1[(x + 13) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 14) % len(Koordinates1)][1] - Koordinates1[(x + 13) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_14,
                   (Tekstokoord[(x + 14) % len(Tekstokoord)][0] - Tekstokoord[(x + 13) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 14) % len(Tekstokoord)][1] - Tekstokoord[(x + 13) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_15, (
                    Koordinates1[(x + 15) % len(Koordinates1)][0] - Koordinates1[(x + 14) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 15) % len(Koordinates1)][1] - Koordinates1[(x + 14) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_15,
                   (Tekstokoord[(x + 15) % len(Tekstokoord)][0] - Tekstokoord[(x + 14) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 15) % len(Tekstokoord)][1] - Tekstokoord[(x + 14) % len(Tekstokoord)][1]) / 1000)
        drobe.move(Kvadratas_16, (
                    Koordinates1[(x + 16) % len(Koordinates1)][0] - Koordinates1[(x + 15) % len(Koordinates1)][
                0]) / 1000, (Koordinates1[(x + 16) % len(Koordinates1)][1] - Koordinates1[(x + 15) % len(Koordinates1)][
            1]) / 1000)
        drobe.move(Tekstas_16,
                   (Tekstokoord[(x + 16) % len(Tekstokoord)][0] - Tekstokoord[(x + 15) % len(Tekstokoord)][0]) / 1000,
                   (Tekstokoord[(x + 16) % len(Tekstokoord)][1] - Tekstokoord[(x + 15) % len(Tekstokoord)][1]) / 1000)
        pg.update()

    x = x + 1
# Pagal rezoliucija
# Normaliai susidaro keiciant dydi(Neissikyria entri ir t.t)
# Programos restartavimas
# Programos aprasymas
# Kiekviena imanoma galimybe
mainloop()
