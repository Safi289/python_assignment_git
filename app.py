import search


topic = search.LearnedTopics()
data_log = search.Topic()

topicSearch = input("Search Topic Name: ")

topic.search(topicSearch)
data_log.data_log(topicSearch)