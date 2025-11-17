from modules.query_generator import generate_search_query
from modules.web_search import perform_web_search, select_relevant_articles

# ---------------------------------------------
# Test Input Topic
# ---------------------------------------------
topic = "Artificial Intelligence"

print("\n🔵 Testing Module 1: Query Generation")
refined_query = generate_search_query(topic)
print("Generated Query:", refined_query)

print("\n🔵 Testing Module 2: Tavily Search")
results = perform_web_search(refined_query)
print("Number of Results:", len(results))

# Print first 3 results
for i, r in enumerate(results[:3]):
    print(f"\nResult {i+1}:")
    print("Title:", r.get("title"))
    print("URL:", r.get("url"))

print("\n🔵 Testing Module 2: Article Selection")
selected_urls = select_relevant_articles(results)
print("Final Selected URLs:")
for url in selected_urls:
    print("-", url)
