from persistence_demo.document import Document

def load_old_version():
    json_v1 = '{"title": "My Doc", "content": "This is v1"}'
    doc = Document.from_json(json_v1)
    print(f"Loaded Document - Title: {doc.title}, Content: {doc.content}")

if __name__ == "__main__":
    load_old_version()
