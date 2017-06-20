
class interpreter:

    def damage_upper(self, cut_spell):

        dain = cut_spell.count("dain")
        aine = cut_spell.count("aine")
        ain = cut_spell.count("ain") - dain
        jee = cut_spell.count("jee")
        dai = cut_spell.count("dai")
        fe = cut_spell.count("fe")
        je = cut_spell.count("je") - jee
        ne = cut_spell.count("ne") - aine
        ai = cut_spell.count("ai") - ain - dai

        minus = len(cut_spell) - ain * 3 - jee * 3 - dai * 3 - fe * 2 - je * 2 - ne * 2 - ai * 2
        count = ain * 3 + jee * 3 + dai * 5 + fe + je * 2 + ne * 2 + ai * 2 - minus
        if fe > 1:
            count = 0
        if count < 0:
            count = 0
        return count

    def damage_lower(self, cut_spell):

        dain2 = cut_spell.count("dain")
        aine2 = cut_spell.count("aine")
        fe2 = cut_spell.count("fe")
        je2 = cut_spell.count("je")
        ne2 = cut_spell.count("ne")
        ai2 = cut_spell.count("ai")
        ain2 = cut_spell.count("ain") - dain2 - aine2
        if ai2 > ain2:
            ain2 = 0
        dai2 = cut_spell.count("dai") - ai2
        if ai2 > dai2:
            dai2 = 0
        jee2 = cut_spell.count("jee") - je2
        if je2 > jee2:
            jee2 = 0

        minus2 = len(cut_spell) - ain2 * 3 - jee2 * 3 - dai2 * 3 - fe2 * 2 - je2 * 2 - ne2 * 2 - ai2 * 2
        count2 = ain2 * 3 + jee2 * 3 + dai2 * 5 + fe2 + je2 * 2 + ne2 * 2 + ai2 * 2 - minus2
        if fe2 > 1:
            count2 = 0
        if count2 < 0:
            count2 = 0
        return count2

    def final_damage(self, count, count2):

        print('Point of upper damage =', count)
        print('Point of lower damage =', count2)
        print("final")
        if count2 > count:
            print('Point of final damage =', count2)
        else:
            print('Point of final damage =', count)


print('Spellbook')
print('fe  - damage 1''\n''je  - damage 2''\n''jee - damage 3''\n''ain - damage 3''\n''dai - damage 5''\n''ne  - damage 2''\n''ai  - damage 2''\n'"Spell must begin by 'fe' and end by 'ai'")
print('\n''Enter a spell')
spell = input('')
spell.find("fe")
spell.find("ai")
cut_spell = spell[spell.find("fe"):spell.rfind("ai") + 2]
print('Spell', cut_spell)
dmgu = interpreter().damage_upper(cut_spell)
dmgl = interpreter().damage_lower(cut_spell)
interpreter().final_damage(dmgu, dmgl)