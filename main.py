
import database_tools


if __name__ == "__main__":
    connection = database_tools.create_connection('loanwords.db')

    #                       #
    #   Script from here    #
    #                       #

    # comment out if txt update not needed
    database_tools.update_txt_from_database(connection)