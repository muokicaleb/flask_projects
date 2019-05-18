from cred import consumer_key, consumer_secret, access_token, access_secret
from twitter import Api
import networkx as nx
import os

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

graph = nx.DiGraph()

print("")
print(".....................................................")
print("FRIENDSHIPS OF A TWITTER USER")
print("")

username = "Muoki_Caleb"


# Log in
api = Api(consumer_key=consumer_key,
          consumer_secret=consumer_secret,
          access_token_key=access_token,
          access_token_secret=access_secret)

# Load data
print("Loading users who follow" + username + "...")
followers = []
followers.extend(api.GetFollowers(screen_name=username))

print("Loading users that" + username + "follows...")
friends = []
friends.extend(api.GetFriends(screen_name=username))

# Create graph
print("Adding followers relationships...")
for user in followers:
    graph.add_edge(user.name, username)

print("Adding following relationships...")
for user in friends:
    graph.add_edge(username, user.name)

# Save graph
print("")
print("The personal profile was analyzed succesfully.")
print("")
print("Saving the file as " + username + "-personal-network.gexf...")
nx.write_gexf(graph, username + "-personal-network.gexf")
