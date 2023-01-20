#
#   TO-DO:
#       . list categories somewhere:    physical_world, kinship, animals, body, food_drink, clothing_grooming, house,
#                                       agriculture_vegetation, actions_technology, motion, possession, spatial_relations,
#                                       quantity, time, sense_perception, emotions_values, cognition, speech_language,
#                                       social_political_relations, warfare_hunting, law, religion_belief, modern_world,
#                                       miscellaneous_function_words

from database_tools import *


if __name__ == "__main__":

    db_interaction = Database_Tools()
    db_interaction.create_table()

    #                       #
    #   Script from here    #
    #                       #

    word_matrix = [['土', 'tǔ', '*tiʔ', 'earth', 'Proto-Austroasiatic', 'agriculture_vegetation', 'from the WOLD, donor language controversial and if it is borrowed at al.'],
                   ['河', 'hé', 'ᠭᠣᠣᠯ', '(yellow) river', 'Mongolian', 'physical_world', 'from the WOLD, controverial origin'],
                   ['川', 'chuān', 'n\\a', 'river', 'n\\a', 'pyhsical_world', 'from the WOLD, but with no donor language given, controversial'],
                   ['凍', 'dòng', '*tuŋa', 'to freeze', 'Proto-Altaic', 'physical_world', 'from WOLD'],
                   ['爸爸', 'bàba', 'n\\a', 'father', 'n\\a', 'kinship', 'from WOLD, no donor or original form given'],
                   ['公', 'gōng', '*klooɲ', 'male', 'Mon-Khmer', 'body', 'from WOLD, controversial e.g. Schuessler 2007 other origin'],
                   ['牛', 'niú', '*ŋwue', 'cattle', 'Proto-Tai', 'animals', 'from WOLD, very controversial'],
                   ['馬', 'mǎ', '? > morin', 'horse', 'Manchu', 'animals', 'from WOLD, very controversial'],
                   ['騾', 'luó', 'n\\a', 'mule', 'n\\a', 'animals', 'from WOLD, but with no donor language or original form given'],
                   ['雞', 'jī', '*r-kaa', 'chicken', 'Proto-Vietic', 'animals', 'from WOLD, mulitple proposed origins'],
                   ['巢', 'cháo', '*rau2', 'nest', 'Proto-Hmong-Mien', 'animals', 'from WOLD'],
                   ['鼠', 'shǔ', '*kn₁(i)ʔ', 'rat', 'Proto-Mon-Khmer', 'animals', 'from WOLD, multiple proposed origins'],
                   ['鯊魚', 'shāyú', 'n\\a', 'shark', 'n\\a', 'animals', 'from WOLD, no donor or original form, very controversial'],
                   ['獅子', 'shīzi', 'šer', 'lion', 'Old Persian', 'animals', 'from WOLD']]

    for word in word_matrix:
        db_interaction.add_word(word)
    
    #               #
    #   Script end  #
    #               #

    db_interaction.update_txt_from_database()