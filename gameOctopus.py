print(''' 
            _                        
           | |                       
  ___   ___| |_ ___  _ __  _   _ ___ 
 / _ \ / __| __/ _ \| '_ \| | | / __|
| (_) | (__| || (_) | |_) | |_| \__ 
 \___/ \___|\__\___/| .__/ \__,_|___/
                    | |              
                    |_|   
''')

print("Vítej ve hře Octopus. Jsi málá chobotnice, kterou chce sežrat žralok a tvým úkolem je utéct do bezpečí.")

storyLine = input("Nacházíš se uprostřed oceánu a před sebou vidíš korálový útes a chaluhový les.\nKam se vydáš? 'útes' nebo 'les' ").lower()

if storyLine == "útes":
    chapter1 = input("Jsi na korálovém útesu. Zaplaval jsi za roh, ale žralok ti je těsně v patách. Máš dvě možnosti, buď použiješ svojí schopnost maskování a budeš doufat, že tě žralok neuvidí nebo se schováš do malé skuliny mezi korály, kde tě žralok uvidí, ale nemusel by se k tobě dostat.\nCo uděláš 'maskovat' nebo 'schovat'? ").lower()
    if chapter1 == "maskovat":
        print("Perfektně si splynul s povrchem korálů a žralok tě nemůže najít. Celou honičku, ale z dálky pozoroval Nemo a žralokovi tě prásknul, protože mu už půl roku dlužíš dvě kila.\nProhrál si, žralok tě sežral.")
    if chapter1 == "schovat":
        print("Nasoukal si se do skuliny mezi korály, ale žralok tě vidí a řítí se na tebe. Skulina je pro něj moc malá a nemůže se k tobě dostat. Po chvíli to vzdá, ty mu chrstneš do ksichtu inkoust a jseš v chillu.\nVyhrál si, úspěšně si utekl.")

if storyLine == "les":
    chapter1 = input("Zaplul jsi do chaluhového lesa a po žralokovi ani stopy, ale zabloudil jsi a nevíš kudy se dostat ven. Narazíš na podezřelého kraba, který ti poradil kudy ven. Věřit krabovi nebo najít cestu sám?\n 'věřit' 'sám' ").lower()
    if chapter1 == "věřit":
        print("Kraba sníš na posilněnou a vydáš se jeho cestou. Krab byl dobrej týpek a poradil ti správně.\nVyhrál si, dostal si se do bezpečí.")
    if chapter1 == "sám":
        print("Nedaří se ti najít cestu ven, začínáš panikařit a plaveš jako zběsilej. Vidíš cestu ven z chaluh a řítíš se tam. Ze samé nepozornosti zapomeneš na žraloka, který tam na tebe čeká a ty mu vplaveš přímo do huby.\nProhrál si, žralok tě sežral.")
    

 




