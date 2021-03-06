import re


def get_landline_patterns(numberings):
    return re.compile("^(\\+?95)?{0}$".format(numberings[0])), numberings[1]


_patterns = list(
    map(get_landline_patterns, [
        ['1424\\d{4}', "FortuneInternational"],
        ['1429\\d{4}', "HorizonTelecomInternational"],
        ['1462\\d{4}', "GoldenTMHTelecom"],
        ['1465\\d{4}', "AGBCommunication"],
        ['1468\\d{4}', "VoIPMyanmarGroup"],
        ['1470\\d{4}', "TelecomInternationalMyanmar"],
        ['2422\\d{4}', "MyanmarAPN"],
        ['2424\\d{4}', "FortuneInternational"],
        ['2462\\d{4}', "GoldenTMHTelecom"],
        ['2468\\d{4}', "VoIPMyanmarGroup"],
        ['2470\\d{4}', "TelecomInternationalMyanmar"],
        ['42480\\d{4}', "TelecomInternationalMyanmar"],
        ['43470\\d{4}', "TelecomInternationalMyanmar"],
        ['45470\\d{4}', "TelecomInternationalMyanmar"],
        ['52470\\d{4}', "TelecomInternationalMyanmar"],
        ['54470\\d{4}', "TelecomInternationalMyanmar"],
        ['57480\\d{4}', "TelecomInternationalMyanmar"],
        ['58470\\d{4}', "TelecomInternationalMyanmar"],
        ['59470\\d{4}', "TelecomInternationalMyanmar"],
        ['63470\\d{4}', "TelecomInternationalMyanmar"],
        ['67460\\d{4}', "MyanmarAPN"],
        ['67470\\d{4}', "TelecomInternationalMyanmar"],
        ['70470\\d{4}', "TelecomInternationalMyanmar"],
        ['71470\\d{4}', "TelecomInternationalMyanmar"],
        ['74470\\d{4}', "TelecomInternationalMyanmar"],
        ['75470\\d{4}', "TelecomInternationalMyanmar"],
        ['81470\\d{4}', "TelecomInternationalMyanmar"],
        ['83470\\d{4}', "TelecomInternationalMyanmar"],
        ['1422\\d{4}', "MyanmarAPN"],
        ['1423\\d{4}', "ShweThamLwinMedia"],
        ['1426\\d{4}', "MyanmarSpeedNet"],
        ['2426\\d{4}', "MyanmarSpeedNet"],
        ['1439\\d{4}', "OoredooMyanmar"],
        ['2439\\d{4}', "OoredooMyanmar"],
        ['67439\\d{4}', "OoredooMyanmar"],
        ['43202\\d{4}', "MyanmarPostsandTelecommunications"],
        ['1471\\d{4}', "Frontiir"],
        ['1446\\d{4}', "YatanarponTelepor"],
        ['1472\\d{4}', "GlobalTechnology"],
        ['2471\\d{4}', "Frontiir"],
        ['2446\\d{4}', "YatanarponTelepor"],
        ['2472\\d{4}', "GlobalTechnology"],
        ['42481\\d{4}', "GlobalTechnology"],
        ['42482\\d{4}', "FortuneTelecom"],
        ['52472\\d{4}', "GlobalTechnology"],
        ['52473\\d{4}', "FortuneTelecom"],
        ['53472\\d{4}', "GlobalTechnology"],
        ['53473\\d{4}', "FortuneTelecom"],
        ['57481\\d{4}', "GlobalTechnology"],
        ['57482\\d{4}', "FortuneTelecom"],
        ['59471\\d{4}', "FortuneTelecom"],
        ['62472\\d{4}', "GlobalTechnology"],
        ['62473\\d{4}', "FortuneTelecom"],
        ['64472\\d{4}', "GlobalTechnology"],
        ['64473\\d{4}', "FortuneTelecom"],
        ['67471\\d{4}', "FortuneTelecom"],
        ['85446\\d{4}', "YatanarponTelepor"],
        ['85472\\d{4}', "GlobalTechnology"],
    ]))
