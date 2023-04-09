import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Millix is an open-source cryptocurrency that operates in a fully decentralized manner, facilitating fast and large-scale transactions with a focus on simplicity.', ['What', 'is', 'a', 'millix' , 'project' ], required_words=['project', 'millix'])
    response('Im a milliy. How can I help you?', ['who are you', 'who you are', 'hey', 'of you', 'wssup'], single_response=True)
    response('In the spring of 2018, a diverse group of developers and business professionals started working on a project to create a cryptocurrency protocol with the potential use case of Millix. Their inspiration for this project stemmed from their past experiences building various technologies.!', ['tall me about millix', 'who is Millix', 'millix', 'project millix', 'tell' , 'me'], single_response=True)
    response('wmlx smart contract address : 0x77d0cb0ab54f9e74b9405a5b3f60da06a78f1aad', ['wmlx', 'smart contract address', 'give', 'i need smart contract' , 'me', 'smart contract millix'], single_response=True)
    response('DAG stands for Directed Acyclic Graph. It is a data structure used in computer science and mathematics to represent relationships between objects or events. In the context of blockchain technology, DAG is used as an alternative to the traditional blockchain data structure. Instead of having a linear chain of blocks, DAG allows for multiple transactions to occur simultaneously and be verified independently, which can result in faster and more efficient transactions. DAG-based cryptocurrencies, such as IOTA and Nano, have gained popularity in recent years for their innovative approach to distributed ledger technology.', ['DAG', 'dag', 'technology millix',], single_response=True)
    response('Millix is an open-source project designed to offer a fast, scalable, and decentralized cryptocurrency network. It aims to provide utility through a peer-to-peer system without any centralization in terms of organization or function.', ['millix network  ', 'who is millix'], single_response=True)
    response('MLX is the cryptocurrency designated for the millix project.', ['what is MLX?', 'mlx', 'MLX', ], single_response=True)
    response('millix community : https://twitter.com/MillixOrg', ['millix community', 'community','twitter'], single_response=True)
    response('Eriksson Monteiro, a PhD holder in Computer Science, is an accomplished software developer and researcher in the field of Artificial Intelligence and Distributed Systems. He has won several international competitions and applied his AI innovations to various industries such as medicine, logistics, environment, advertising, finance, and fraud. Eriksson is originally from Cabo Verde and has been focusing on cryptography and cryptocurrencies since 2012. He is passionate about democratizing technology and improving access to modern financial services in developing countries.', ['who is Eriksson Monteiro', 'Eriksson ',], single_response=True)
    response('Emmanuel is a highly accomplished individual who started his university studies at age 13. He has a background in medicine, mathematics, and computer science. Since 2013, he has focused on blockchain and cryptocurrency, with a specific interest in using these technologies to solve health and medical issues. In addition to his academic achievements, Emmanuel is fluent in three spoken languages, has lived in a monastery, and has traveled extensively around the world for volunteering and studying purposes.', ['who is Emmanuel Braden', 'Emmanuel ', 'Braden',], single_response=True)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Milliy: ' + get_response(input('You: ')))
