#
#   TO-DO:
#       . list categories somewhere:    physical_world, kinship, animals, body, food_drink, clothing_grooming, house,
#                                       agriculture_vegetation, actions_technology, motion, possession, spatial_relations,
#                                       quantity, time, sense_perception, emotions_values, cognition, speech_language,
#                                       social_political_relations, warfare_hunting, law, religion_belief, modern_world,
#                                       miscellaneous_function_words
#       . normalize
#       . check if all Hanzi in traditional Chinese
#       . add citations
#

from database_tools import *


if __name__ == "__main__":

    db_interaction = Database_Tools()
    db_interaction.create_table()

    #                       #
    #   Script from here    #
    #                       #
    
    word_matrix = [[]]

    for word in word_matrix:
        db_interaction.add_word(word)
    
    
    #               #
    #   Script end  #
    #               #

    db_interaction.update_txt_from_database()