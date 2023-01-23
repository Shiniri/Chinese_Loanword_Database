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

    word_matrix = [['象', 'xiàng', 'n\\a', 'elephant', 'n\\a', 'animals', 'from WOLD, probably entered Sino-Tibetan from Austroasiatic'],
                   ['骆驼', 'luòtuo', 'dada', 'camel', 'Xiongnu', 'animals', 'from WOLD'],
                   ['龜', 'guī', '*dwii', 'turtle', 'Proto-Austroasiatic', 'animals', 'from WOLD'],
                   ['貘', 'mò', 'n\\a', 'tapir', 'n\\a', 'animals', 'from WOLD, very controversial & no proposed origin'],
                   ['頭', 'tóu', '> /-dool/', 'head', 'Proto-Austroasiatic', 'body', 'from WOLD, quite controversial'],
                   ['頷', 'hàn', '*tga(a)m', 'chin', 'Proto-Mon-Khmer', 'body', 'from WOLD, quite controversial'],
                   ['牙', 'yá', 'n\\a', 'tooth', 'Proto-Austroasiatic', 'body', 'from WOLD, quite controversial'],
                   ['爪', 'zhuǎ', '*čiŭru', 'claw', 'Proto-Altaic', 'body', 'from WOLD'],
                   ['腿', 'tuǐ', '*dɯl', 'leg', 'Proto-Mon-Khmer', 'body', 'from WOLD'],
                   ['飯', 'fàn', '*pVŋ', 'food', 'Proto-Austroasiatic', 'food_drink', 'from WOLD, quite controversial'],
                   ['吞', 'tūn', '*kl-', 'swallow', 'Proto-Tai', 'food_drink', 'from WOLD, quite controversial'],
                   ['壶', 'hú', 'n\\a', 'kettle', 'Proto-Tai', 'food_drink', 'from WOLD, donor unclear'],
                   ['叉', 'chā', 'n\\a', 'fork', 'Proto-Austroasiatic', 'food_drink', 'from WOLD, unidentifiable original form'],
                   ['葡萄', 'pútao', '*būdawa', 'grape', 'Elamite', 'agriculture_vegetation', 'from WOLD, original form contested, but clearly borrowed'],
                   ['橄欖', 'gǎnlǎn', 'k(a)lam', 'olive', 'n\\a', 'agriculture_vegetation', 'from WOLD, unidentified origin language, contested original form, but clearly borrowed'],
                   ['布', 'bù', '*k-rn-pa:s', 'cloth', 'Proto-Austroasiatic', 'clothing_grooming', 'from WOLD'],
                   ['染', 'rǎn', 'n\\a', 'dye', 'Proto-Tai', 'clothing_grooming', 'from WOLD, direction of borrowing unclear'],
                   ['床', 'chuáng', 'n\\a', 'bed', 'Austro-Asiatic', 'house', 'from WOLD, unclear original form or exact donor'],
                   ['鋤', 'chú', '> /crās/', 'hoe', 'Proto-Austroasiatic', 'agriculture_vegetation', 'from WOLD'],
                   ['耙', 'pá', '> /baar/', 'rake', 'Proto-Austroasiatic', 'agriculture_vegetation', 'from WOLD, quite controversial'],
                   ['米', 'mǐ', 'n\\a', 'rice', 'n\\a', 'food_drink', 'from WOLD, very unclear if borrowed at all'],
                   ['根', 'gēn', '*kǝl', 'root', 'Austro-Asiatic', 'agriculture_vegetation', 'from WOLD'],
                   ['花', 'huā', '/pkaa/', 'flower', 'Old Khmer', 'agriculture_vegetation', 'from WOLD, exact origin unclear'],
                   ['槟榔', 'bīnglang', 'n\\a', 'palm tree', 'Austronesian', 'agriculture_vegetation', 'from WOLD, unclear origin but clearly borrowed'],
                   ['檸檬', 'níngméng', 'lemon', 'lemon', 'English', 'agriculture_vegetation', 'from WOLD, various origins, also from Arabic / Persian'],
                   ['榖', 'gǔ', 'n\\a', 'sorghum millet', 'Proto-Austroasiatic', 'agriculture_vegetation', 'from WOLD'],
                   ['葫蘆', 'húlu', 'n\\a', 'pumpkin', 'n\\a', 'agriculture_vegetation', 'from WOLD, but no donor or original form given, quite controversial']]

    for word in word_matrix:
        db_interaction.add_word(word)
    
    #               #
    #   Script end  #
    #               #

    db_interaction.update_txt_from_database()