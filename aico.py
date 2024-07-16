import wikipediaapi
import cohere

# Initialize Wikipedia API with a custom user agent
user_agent = 'MyWikipediaApp/1.0 (myemail@example.com)'  # Replace with your information
wiki_wiki = wikipediaapi.Wikipedia('en', headers={'User-Agent': user_agent})

# Function to fetch a Wikipedia page summary
def fetch_wikipedia_summary(page_title):
    page = wiki_wiki.page(page_title)
    if page.exists():
        return page.summary
    else:
        return None

# Initialize Cohere API
co = cohere.Client('BJCvZcjRzusRT9YHrTMr9fvwF0v9PbrhcTNzVBqo')

# Function to generate text or summarize using Cohere
def cohere_generate_or_summarize(text, task='generate'):
    if task == 'generate':
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=text,
            max_tokens=100
        )
        return response.generations[0].text
    elif task == 'summarize':
        response = co.summarize(
            model='summarize-xlarge',
            text=text
        )
        return response.summary

# Example usage
page_title = "Natural language processing"
summary = fetch_wikipedia_summary(page_title)

if summary:
    print("Wikipedia Summary:")
    print(summary)
    
    # Generate additional text based on the summary
    generated_text = cohere_generate_or_summarize(summary, task='generate')
    print("\nGenerated Text:")
    print(generated_text)
    
    # Summarize the Wikipedia summary (meta-summarization)
    summarized_text = cohere_generate_or_summarize(summary, task='summarize')
    print("\nSummarized Text:")
    print(summarized_text)
else:
    print("Page not found on Wikipedia.")